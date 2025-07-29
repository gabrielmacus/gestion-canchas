from abc import ABC, abstractmethod
from src.Administracion.Canchas.Domain.Entities.Cancha import Cancha
from src.SharedKernel.Domain.Criteria.Criteria import Criteria

class CanchaRepositoryInterface(ABC):
    @abstractmethod
    def add(self, cancha: Cancha) -> Cancha:
        pass
    
    @abstractmethod
    def update(self, cancha: Cancha) -> Cancha:
        pass
    
    @abstractmethod
    def matching(self, criteria: Criteria) -> list[Cancha]:
        pass
    
    @abstractmethod
    def delete_by_id(self, id: str) -> None:
        pass