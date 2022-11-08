from abc import ABC, abstractproperty, abstractmethod


class BussinessRule(ABC):
    @abstractmethod
    def __init__(self, message: str):
        self.message: str = message

    @abstractmethod
    def isValid(self) -> bool:
        raise NotImplementedError
