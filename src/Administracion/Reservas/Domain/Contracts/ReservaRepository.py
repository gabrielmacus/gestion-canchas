from abc import ABC
from src.Administracion.Reservas.Domain.Entities.Reserva import Reserva
from src.SharedKernel.Domain.Contracts.Repository.RepositoryInterface import RepositoryInterface

class ReservaRepositoryInterface(RepositoryInterface[Reserva], ABC):
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