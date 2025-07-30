from abc import ABC, abstractmethod
from typing import Generic, TypeVar

T = TypeVar('T')

class UpdaterInterface(ABC, Generic[T]):
    @abstractmethod
    def update_by_id(self, id: str, entity: T) -> None:
        pass