from src.Administracion.Jugadores.Application.UseCases.EliminarJugadorUseCase import EliminarJugadorUseCase
from src.SharedKernel.Infraestructure.Services.SAConnection import SAConnection
from src.Administracion.Jugadores.Infraestructure.Services.SAJugadorRepository import SAJugadorRepository
from src.Administracion.Jugadores.Domain.Services.JugadorFinder import JugadorFinder

class JugadorDeleteHandler():
    def __init__(self):
        self._repository = SAJugadorRepository(SAConnection().get_engine())
        self._eliminar_jugador_usecase = EliminarJugadorUseCase(
            self._repository,
            JugadorFinder(self._repository)
        )
    
    def delete(self, id: str):
        self._eliminar_jugador_usecase.execute(id)