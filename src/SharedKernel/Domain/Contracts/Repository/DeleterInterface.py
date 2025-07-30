from abc import ABC, abstractmethod
from typing import Generic, TypeVar

T = TypeVar('T')

class DeleterInterface(ABC, Generic[T]):
    @abstractmethod
    def delete_by_id(self, id: str) -> None:
        pass