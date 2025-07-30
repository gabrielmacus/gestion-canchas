from src.Administracion.Canchas.Domain.Entities.Cancha import Cancha
from tests.SharedKernel.Domain.Mothers.IdMother import IdMother
from tests.Administracion.Canchas.Domain.Mothers.CanchaNombreMother import CanchaNombreMother
from tests.Administracion.Canchas.Domain.Mothers.CanchaTechadaMother import CanchaTechadaMother

class CanchaMother:
    @staticmethod
    def create(id: str | None = None, 
               nombre: str | None = None, 
               techada: bool | None = None):
        return Cancha(
            id=id or IdMother.create(),
            nombre=nombre or CanchaNombreMother.create(),
            techada=techada or CanchaTechadaMother.create()
        ) 