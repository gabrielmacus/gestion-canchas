from abc import ABC, abstractmethod
from src.Administracion.Reservas.Domain.Entities.Reserva import Reserva
from src.SharedKernel.Domain.Criteria.Criteria import Criteria

class ReservaRepositoryInterface(ABC):
    @abstractmethod
    def add(self, reserva: Reserva) -> None:
        pass
    
    @abstractmethod
    def update(self, reserva: Reserva) -> None:
        pass
    
    @abstractmethod
    def matching(self, criteria: Criteria) -> list[Reserva]:
        pass
    
    @abstractmethod
    def delete_by_id(self, id: str) -> None:
        pass
    
    '''
    @abstractmethod
    def find_active_by_cancha(self, cancha_id: str) -> list[Reserva]:
        """Devuelve todas las reservas activas,
        es decir, cuya fecha sea mayor o igual a la fecha actual,
        correspondientes a una cancha.

        Args:
            cancha_id (str): Id de la cancha.

        Returns:
            list[Reserva]: Lista de reservas activas.
        """
        pass
    '''