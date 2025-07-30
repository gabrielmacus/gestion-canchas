from abc import ABC, abstractmethod
from typing import Any, TypeVar, Generic

T = TypeVar('T')

class MappeableModelInterface(ABC):
    @abstractmethod
    def to_model(self) -> Any:
        pass
    
    @abstractmethod
    def from_model(self, model: Any) -> 'MappeableModelInterface':
        pass