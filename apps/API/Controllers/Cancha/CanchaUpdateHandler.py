from src.Administracion.Canchas.Application.UseCases.EditarCanchaUseCase import EditarCanchaUseCase
from src.Administracion.Canchas.Application.DTOs.EditarCanchaDTO import EditarCanchaDTO
from src.Administracion.Canchas.Domain.Services.CanchaFinder import CanchaFinder
from src.SharedKernel.Infraestructure.Services.SAConnection import SAConnection
from src.Administracion.Canchas.Infraestructure.Services.SACanchaRepository import SACanchaRepository

class CanchaUpdateHandler():
    def __init__(self):
        self._repository = SACanchaRepository(SAConnection().get_engine())
        self._cancha_finder = CanchaFinder(self._repository)
        self._editar_cancha_usecase = EditarCanchaUseCase(self._repository, self._cancha_finder)
    
    def update(self, id: str, request: EditarCanchaDTO):
        self._editar_cancha_usecase.execute(id, request) 