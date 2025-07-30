from src.Administracion.Jugadores.Application.UseCases.ListarJugadoresUseCase import ListarJugadoresUseCase
from src.Administracion.Jugadores.Infraestructure.Services.SAJugadorRepository import SAJugadorRepository
from src.SharedKernel.Infraestructure.Services.SAConnection import SAConnection

class JugadorController:
    _listar_jugadores_usecase: ListarJugadoresUseCase
    
    def __init__(self):
        self._listar_jugadores_usecase = ListarJugadoresUseCase(
            SAJugadorRepository(SAConnection().get_engine())
        )
    
    def find(self):
        return self._listar_jugadores_usecase.execute()
        