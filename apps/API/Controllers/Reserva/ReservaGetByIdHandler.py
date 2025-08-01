from apps.API.Controllers.BaseGetByIdRequestHandler import BaseGetByIdRequestHandler
from src.Administracion.Reservas.Domain.Services.ReservaFinder import ReservaFinder
from src.Administracion.Reservas.Domain.Entities.Reserva import Reserva
from apps.API.DTOs.ReservaDTO import ReservaDTO
from src.SharedKernel.Infraestructure.Services.SAConnection import SAConnection
from src.Administracion.Reservas.Infraestructure.Services.SAReservaRepository import SAReservaRepository
from apps.API.Mappings.ReservaMappings import ReservaMappings

class ReservaGetByIdHandler(BaseGetByIdRequestHandler[Reserva, ReservaDTO]):
    def __init__(self):
        self._repository = SAReservaRepository(SAConnection().get_engine())
        self._reserva_finder = ReservaFinder(self._repository)

    def _find_by_id(self, id: str) -> Reserva:
        return self._reserva_finder.find_by_id(id)
    
    def _map_to_response(self, result: Reserva) -> ReservaDTO:
        return ReservaMappings.to_dto(result) 