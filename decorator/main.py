# app.py
from logger import Logger
import time


@Logger
def greet(name: str) -> str:
    return f"Hello, {name}!"


@Logger(level=20, log_args=True, log_return=False)
def add(a, b):
    return a + b


@Logger(level=10, log_time=False)
def slow_function(n: int):
    time.sleep(n)
    return "Done"


if __name__ == "__main__":
    greet("Alice")
    print(add(2, 3))
    print(slow_function(1))
