from src.Administracion.Jugadores.Application.DTOs.CrearJugadorDTO import CrearJugadorDTO
from src.Administracion.Jugadores.Domain.Entities.Jugador import Jugador
from src.Administracion.Jugadores.Application.UseCases.CrearJugadorUseCase import CrearJugadorUseCase
from src.Administracion.Jugadores.Application.UseCases.EditarJugadorUseCase import EditarJugadorUseCase
from src.Administracion.Jugadores.Application.UseCases.EliminarJugadorUseCase import EliminarJugadorUseCase
from src.SharedKernel.Infraestructure.Services.SAConnection import SAConnection
from src.Administracion.Jugadores.Infraestructure.Services.SAJugadorRepository import SAJugadorRepository

class JugadorCreateHandler():
    def __init__(self):
        self._crear_jugador_usecase = CrearJugadorUseCase(
            SAJugadorRepository(SAConnection().get_engine())
        )
    
    def create(self, request: CrearJugadorDTO):
        self._crear_jugador_usecase.execute(request)