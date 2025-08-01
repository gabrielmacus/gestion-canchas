from apps.API.Controllers.BaseGetByIdRequestHandler import BaseGetByIdRequestHandler
from src.Administracion.Canchas.Domain.Services.CanchaFinder import CanchaFinder
from src.Administracion.Canchas.Domain.Entities.Cancha import Cancha
from apps.API.DTOs.CanchaDTO import CanchaDTO
from src.SharedKernel.Infraestructure.Services.SAConnection import SAConnection
from src.Administracion.Canchas.Infraestructure.Services.SACanchaRepository import SACanchaRepository
from apps.API.Mappings.CanchaMappings import CanchaMappings

class CanchaGetByIdHandler(BaseGetByIdRequestHandler[Cancha, CanchaDTO]):
    def __init__(self):
        self._repository = SACanchaRepository(SAConnection().get_engine())
        self._cancha_finder = CanchaFinder(self._repository)

    def _find_by_id(self, id: str) -> Cancha:
        return self._cancha_finder.find_by_id(id)
    
    def _map_to_response(self, result: Cancha) -> CanchaDTO:
        return CanchaMappings.to_dto(result) 