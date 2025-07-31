from src.Administracion.Canchas.Application.DTOs.EditarCanchaDTO import EditarCanchaDTO
from src.Administracion.Canchas.Domain.Contracts.CanchaRepositoryInterface import CanchaRepositoryInterface
from src.Administracion.Canchas.Domain.Entities.Cancha import Cancha
from src.Administracion.Canchas.Domain.Services.CanchaFinder import CanchaFinder

class EditarCanchaUseCase:
    def __init__(self, cancha_repository: CanchaRepositoryInterface, cancha_finder: CanchaFinder):
        self._cancha_repository = cancha_repository
        self._cancha_finder = cancha_finder

    def execute(self, id: str, request: EditarCanchaDTO) -> Cancha:
        cancha = self._cancha_finder.find_by_id(id)
        updated_cancha = self._update_cancha(cancha, request)
        self._cancha_repository.update_by_id(id, updated_cancha)
        return updated_cancha
    
    def _update_cancha(self, cancha: Cancha, request: EditarCanchaDTO) -> Cancha:
        """Crea una nueva instancia de Cancha con los valores actualizados, respetando inmutabilidad"""
        dump = request.model_dump(exclude_unset=True)
        return Cancha(
            id=cancha.id.value,
            nombre=cancha.nombre.value if 'nombre' not in dump else dump['nombre'],
            techada=cancha.techada.value if 'techada' not in dump else dump['techada']
        ) 