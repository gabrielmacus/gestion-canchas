from src.Administracion.Jugadores.Domain.Contracts.JugadorRepositoryInterface import JugadorRepositoryInterface
from src.Administracion.Jugadores.Domain.Services.JugadorFinder import JugadorFinder

class EliminarJugadorUseCase:
    def __init__(self, jugador_repository: JugadorRepositoryInterface, jugador_finder: JugadorFinder):
        self._jugador_repository = jugador_repository
        self._jugador_finder = jugador_finder
    
    def execute(self, id: str):
        self._jugador_finder.find_by_id(id)
        self._jugador_repository.delete_by_id(id)