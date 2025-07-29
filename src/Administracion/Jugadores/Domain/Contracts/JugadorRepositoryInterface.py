from abc import ABC, abstractmethod
from src.Administracion.Jugadores.Domain.Entities.Jugador import Jugador
from src.SharedKernel.Domain.Criteria.Criteria import Criteria

class JugadorRepositoryInterface(ABC):
    @abstractmethod
    def add(self, jugador: Jugador) -> None:
        pass
    
    @abstractmethod
    def update(self, jugador: Jugador) -> None:
        pass
    
    @abstractmethod
    def matching(self, criteria: Criteria) -> list[Jugador]:
        pass

    @abstractmethod
    def delete_by_id(self, id: str) -> None:
        pass