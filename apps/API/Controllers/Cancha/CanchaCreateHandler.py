from src.Administracion.Canchas.Application.DTOs.CrearCanchaDTO import CrearCanchaDTO
from src.Administracion.Canchas.Application.UseCases.CrearCanchaUseCase import CrearCanchaUseCase
from src.SharedKernel.Infraestructure.Services.SAConnection import SAConnection
from src.Administracion.Canchas.Infraestructure.Services.SACanchaRepository import SACanchaRepository

class CanchaCreateHandler():
    def __init__(self):
        self._repository = SACanchaRepository(SAConnection().get_engine())
        self._crear_cancha_usecase = CrearCanchaUseCase(self._repository)
    
    def create(self, request: CrearCanchaDTO):
        self._crear_cancha_usecase.execute(request) 