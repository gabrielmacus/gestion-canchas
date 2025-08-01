from apps.API.Controllers.BaseGetByIdRequestHandler import BaseGetByIdRequestHandler
from src.Administracion.Jugadores.Domain.Services.JugadorFinder import JugadorFinder
from src.Administracion.Jugadores.Domain.Entities.Jugador import Jugador
from apps.API.DTOs.JugadorDTO import JugadorDTO
from src.SharedKernel.Infraestructure.Services.SAConnection import SAConnection
from src.Administracion.Jugadores.Infraestructure.Services.SAJugadorRepository import SAJugadorRepository
from apps.API.Mappings.JugadorMappings import JugadorMappings

class JugadorGetByIdHandler(BaseGetByIdRequestHandler[Jugador, JugadorDTO]):
    def __init__(self):
        self._repository = SAJugadorRepository(SAConnection().get_engine())
        self._jugador_finder = JugadorFinder(self._repository)

    def _find_by_id(self, id: str) -> Jugador:
        return self._jugador_finder.find_by_id(id)
    
    def _map_to_response(self, result: Jugador) -> JugadorDTO:
        return JugadorMappings.to_dto(result) 