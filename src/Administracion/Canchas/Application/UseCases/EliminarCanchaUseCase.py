from src.Administracion.Canchas.Domain.Contracts.CanchaRepositoryInterface import CanchaRepositoryInterface
from src.Administracion.Canchas.Domain.Services.CanchaFinder import CanchaFinder

class EliminarCanchaUseCase:
    def __init__(self, cancha_repository: CanchaRepositoryInterface, cancha_finder: CanchaFinder):
        self._cancha_repository = cancha_repository
        self._cancha_finder = cancha_finder

    def execute(self, id: str):
        # Verificar que la cancha existe usando el finder
        self._cancha_finder.find_by_id(id)
        
        self._cancha_repository.delete_by_id(id) 