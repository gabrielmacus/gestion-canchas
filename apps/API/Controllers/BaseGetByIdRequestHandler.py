from abc import ABC, abstractmethod
from typing import TypeVar, Generic

T = TypeVar('T')
R = TypeVar('R')

class BaseGetByIdRequestHandler(ABC, Generic[T, R]):
    def get_by_id(self, id: str) -> R:
        result = self._find_by_id(id)
        return self._map_to_response(result)
    
    @abstractmethod
    def _find_by_id(self, id: str) -> T:
        pass
    
    @abstractmethod
    def _map_to_response(self, result: T) -> R:
        pass