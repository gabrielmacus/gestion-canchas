from src.SharedKernel.Domain.Entities.AggregateRoot import AggregateRoot
from src.Administracion.Canchas.Domain.ValueObjects.CanchaId import CanchaId
from src.Administracion.Canchas.Domain.ValueObjects.CanchaNombre import CanchaNombre
from src.Administracion.Canchas.Domain.ValueObjects.CanchaTechada import CanchaTechada
from dataclasses import dataclass

@dataclass
class Cancha(AggregateRoot):
    _id: CanchaId
    _nombre: CanchaNombre
    _techada: CanchaTechada
    
    def __init__(self, id:str, nombre:str, techada:bool):
        self._id = CanchaId(id)
        self._nombre = CanchaNombre(nombre)
        self._techada = CanchaTechada(techada)
        
        super().__init__()
    
    @property
    def id(self):
        return self._id
    
    @property
    def nombre(self):
        return self._nombre
    
    @property
    def techada(self):
        return self._techada
    
    @staticmethod
    def create(id:str, nombre:str, techada:bool):
        # TODO: Domain event
        return Cancha(id, nombre, techada)