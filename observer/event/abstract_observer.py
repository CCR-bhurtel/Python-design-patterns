from abc import ABC, abstractmethod


class Observer(ABC):
    @abstractmethod
    def update(serlf, message: str):
        pass
