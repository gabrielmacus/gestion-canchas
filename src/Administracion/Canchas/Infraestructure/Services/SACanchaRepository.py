from sqlalchemy import Engine
from src.SharedKernel.Infraestructure.Repository.BaseSQLAlchemyRepository import BaseSQLAlchemyRepository
from src.Administracion.Canchas.Domain.Entities.Cancha import Cancha
from src.Administracion.Canchas.Domain.Contracts.CanchaRepositoryInterface import CanchaRepositoryInterface
from src.Administracion.Canchas.Infraestructure.Models.CanchaModel import CanchaModel
from typing import Any

class SACanchaRepository(BaseSQLAlchemyRepository[Cancha, CanchaModel], CanchaRepositoryInterface):
    def __init__(self, engine: Engine):
        super().__init__(engine, CanchaModel)
    
    def model_to_entity(self, model: CanchaModel) -> Cancha:
        return Cancha(
            id=str(model.id),
            nombre=model.nombre,
            techada=model.techada
        )
    
    def entity_to_model(self, entity: Cancha) -> CanchaModel:
        return CanchaModel(
            id=entity.id.value,
            nombre=entity.nombre.value,
            techada=entity.techada.value
        )
    
    def entity_to_update_values(self, entity: Cancha) -> dict[str, Any]:
        return {
            "nombre": entity.nombre.value,
            "techada": entity.techada.value
        } 