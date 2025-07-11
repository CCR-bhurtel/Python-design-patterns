import weakref
from abc import ABC, abstractmethod


class Observer(ABC):
    @abstractmethod
    def update(self, msg: str):
        pass


class Subject:
    def __init__(self):
        self._obsevers = weakref.WeakSet()

    def attach(self, observer: Observer):
        self._obsevers.add(observer)

    def detach(self, observer: Observer):
        self._obsevers.remove(observer)

    def notify(self, message: str):
        for observer in list(self._obsevers):
            observer.update(message)
