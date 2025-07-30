from src.Administracion.Jugadores.Domain.Contracts.JugadorRepositoryInterface import JugadorRepositoryInterface
from src.Administracion.Jugadores.Domain.Exceptions.JugadorNotFound import JugadorNotFound

class JugadorFinder:
    def __init__(self, jugador_repository: JugadorRepositoryInterface):
        self._jugador_repository = jugador_repository
    
    def find_by_id(self, id: str):
        jugador = self._jugador_repository.get_by_id(id)
        if not jugador:
            raise JugadorNotFound(id)
        return jugador
    
    def _ensure_jugador_exists(self, id: str):
        jugador = self.find_by_id(id)
        if not jugador:
            raise JugadorNotFound(id)
        return jugador