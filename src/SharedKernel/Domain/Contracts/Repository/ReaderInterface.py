from abc import ABC, abstractmethod
from typing import Generic, TypeVar
from src.SharedKernel.Domain.Criteria.Criteria import Criteria

T = TypeVar('T')

class ReaderInterface(ABC, Generic[T]):
    @abstractmethod
    def matching(self, criteria: Criteria) -> list[T]:
        pass

    @abstractmethod
    def get_by_id(self, id: str) -> T | None:
        pass