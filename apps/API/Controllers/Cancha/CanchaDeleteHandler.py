from src.Administracion.Canchas.Application.UseCases.EliminarCanchaUseCase import EliminarCanchaUseCase
from src.Administracion.Canchas.Domain.Services.CanchaFinder import CanchaFinder
from src.SharedKernel.Infraestructure.Services.SAConnection import SAConnection
from src.Administracion.Canchas.Infraestructure.Services.SACanchaRepository import SACanchaRepository

class CanchaDeleteHandler():
    def __init__(self):
        self._repository = SACanchaRepository(SAConnection().get_engine())
        self._cancha_finder = CanchaFinder(self._repository)
        self._eliminar_cancha_usecase = EliminarCanchaUseCase(self._repository, self._cancha_finder)
    
    def delete(self, id: str):
        self._eliminar_cancha_usecase.execute(id) 