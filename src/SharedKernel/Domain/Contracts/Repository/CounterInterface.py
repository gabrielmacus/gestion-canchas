from abc import ABC, abstractmethod
from typing import Generic, TypeVar
from src.SharedKernel.Domain.Criteria.Criteria import Criteria

T = TypeVar('T')

class CounterInterface(ABC, Generic[T]):
    @abstractmethod
    def count_matching(self, criteria: Criteria) -> int:
        pass