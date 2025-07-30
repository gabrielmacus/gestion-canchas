from src.Administracion.Jugadores.Application.UseCases.PaginarJugadoresUseCase import PaginarJugadoresUseCase
from src.Administracion.Jugadores.Infraestructure.Services.SAJugadorRepository import SAJugadorRepository
from src.SharedKernel.Infraestructure.Services.SAConnection import SAConnection
from apps.API.Mappings.JugadorMappings import JugadorMappings
from src.Administracion.Jugadores.Application.DTOs.CrearJugadorDTO import CrearJugadorDTO
from src.Administracion.Jugadores.Application.UseCases.CrearJugadorUseCase import CrearJugadorUseCase

class JugadorController:
    _paginar_jugadores_usecase: PaginarJugadoresUseCase
    _crear_jugador_usecase: CrearJugadorUseCase
    
    def __init__(self):
        self._paginar_jugadores_usecase = PaginarJugadoresUseCase(
            SAJugadorRepository(SAConnection().get_engine())
        )
        self._crear_jugador_usecase = CrearJugadorUseCase(
            SAJugadorRepository(SAConnection().get_engine())
        )
    
    def find(self):
        result = self._paginar_jugadores_usecase.execute()
        return JugadorMappings.to_paged_response_dto(result)
    
    def create(self, request: CrearJugadorDTO):
        self._crear_jugador_usecase.execute(request)