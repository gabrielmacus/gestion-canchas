from abc import ABC, abstractmethod
from typing import Generic, TypeVar

T = TypeVar('T')

class CreatorInterface(ABC, Generic[T]):
    @abstractmethod
    def add(self, entity: T) -> None:
        pass