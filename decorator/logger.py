import time
import logging
from functools import wraps
from typing import Callable, Any, Optional


class Logger:
    def __init__(
        self,
        func: Optional[Callable] = None,
        *,
        level: int = logging.INFO,
        enabled: bool = True,
        log_args: bool = True,
        log_return: bool = True,
        log_time: bool = True,
    ):
        self.func = func
        self.level = level
        self.enabled = enabled
        self.log_args = log_args
        self.log_return = log_return
        self.log_time = log_time

        # Handle direct usage: @Logger
        if func is not None:
            wraps(func)(self)

    def __call__(self, *args, **kwargs):
        # If __call__ is called with a function (i.e., used as @Logger(...))
        if self.func is None and len(args) == 1 and callable(args[0]):
            self.func = args[0]
            wraps(self.func)(self)
            return self

        if not self.enabled:
            return self.func(*args, **kwargs)

        logger = logging.getLogger(self.func.__module__)
        logger.setLevel(self.level)

        if not logger.handlers:
            handler = logging.StreamHandler()
            formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
            handler.setFormatter(formatter)
            logger.addHandler(handler)

        logger.log(self.level, f"Called {self.func.__name__}")

        if self.log_args:
            logger.log(self.level, f"Arguments: args={args}, kwargs={kwargs}")

        start = time.time()
        result = self.func(*args, **kwargs)
        end = time.time()

        if self.log_return:
            logger.log(self.level, f"Returned: {result}")

        if self.log_time:
            logger.log(self.level, f"Execution time: {end - start:.4f} seconds")

        return result
