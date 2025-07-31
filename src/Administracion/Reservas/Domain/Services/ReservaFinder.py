from src.Administracion.Reservas.Domain.Contracts.ReservaRepository import ReservaRepositoryInterface
from src.Administracion.Reservas.Domain.Exceptions.ReservaNotFound import ReservaNotFound

class ReservaFinder:
    def __init__(self, reserva_repository: ReservaRepositoryInterface):
        self._reserva_repository = reserva_repository
    
    def find_by_id(self, id: str):
        reserva = self._reserva_repository.get_by_id(id)
        if not reserva:
            raise ReservaNotFound(id)
        return reserva
    
    def _ensure_reserva_exists(self, id: str):
        reserva = self.find_by_id(id)
        if not reserva:
            raise ReservaNotFound(id)
        return reserva 