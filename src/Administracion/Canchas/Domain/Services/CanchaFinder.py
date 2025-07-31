from src.Administracion.Canchas.Domain.Contracts.CanchaRepositoryInterface import CanchaRepositoryInterface
from src.Administracion.Canchas.Domain.Exceptions.CanchaNotFound import CanchaNotFound

class CanchaFinder:
    def __init__(self, cancha_repository: CanchaRepositoryInterface):
        self._cancha_repository = cancha_repository
    
    def find_by_id(self, id: str):
        cancha = self._cancha_repository.get_by_id(id)
        if not cancha:
            raise CanchaNotFound(id)
        return cancha
    
    def _ensure_cancha_exists(self, id: str):
        cancha = self.find_by_id(id)
        if not cancha:
            raise CanchaNotFound(id)
        return cancha 