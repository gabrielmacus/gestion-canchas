from src.Administracion.Reservas.Domain.Contracts.ReservaRepository import ReservaRepositoryInterface
from src.Administracion.Reservas.Domain.Services.ReservaFinder import ReservaFinder

class EliminarReservaUseCase:
    def __init__(self, reserva_repository: ReservaRepositoryInterface, reserva_finder: ReservaFinder):
        self._reserva_repository = reserva_repository
        self._reserva_finder = reserva_finder

    def execute(self, id: str):
        # Verificar que la reserva existe usando el finder
        self._reserva_finder.find_by_id(id)
        
        self._reserva_repository.delete_by_id(id) 