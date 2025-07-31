from src.Administracion.Jugadores.Domain.Services.JugadorFinder import JugadorFinder
from src.Administracion.Jugadores.Application.UseCases.EditarJugadorUseCase import EditarJugadorUseCase
from src.Administracion.Jugadores.Application.DTOs.EditarJugadorDTO import EditarJugadorDTO
from src.SharedKernel.Infraestructure.Services.SAConnection import SAConnection
from src.Administracion.Jugadores.Infraestructure.Services.SAJugadorRepository import SAJugadorRepository



class JugadorUpdateHandler():
    def __init__(self):
        self._repository = SAJugadorRepository(SAConnection().get_engine())
        self._editar_jugador_usecase = EditarJugadorUseCase(
            self._repository,
            JugadorFinder(self._repository)
        )
    
    def update(self, id: str, request: EditarJugadorDTO):
        self._editar_jugador_usecase.execute(id, request)