from src.Administracion.Canchas.Application.DTOs.CrearCanchaDTO import CrearCanchaDTO
from src.Administracion.Canchas.Domain.Entities.Cancha import Cancha
from src.Administracion.Canchas.Domain.Contracts.CanchaRepositoryInterface import CanchaRepositoryInterface

class CrearCanchaUseCase:
    def __init__(self, cancha_repository: CanchaRepositoryInterface):
        self.__cancha_repository = cancha_repository

    def execute(self, request: CrearCanchaDTO) -> Cancha:
        cancha = Cancha.create(request.id, request.nombre, request.techada)
        _ = self.__cancha_repository.add(cancha)
        return cancha