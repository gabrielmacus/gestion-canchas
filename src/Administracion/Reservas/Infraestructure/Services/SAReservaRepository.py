from sqlalchemy import Engine
from src.SharedKernel.Infraestructure.Repository.BaseSQLAlchemyRepository import BaseSQLAlchemyRepository
from src.Administracion.Reservas.Domain.Entities.Reserva import Reserva
from src.Administracion.Reservas.Domain.Contracts.ReservaRepository import ReservaRepositoryInterface
from src.Administracion.Reservas.Infraestructure.Models.ReservaModel import ReservaModel
from typing import Any
from src.SharedKernel.Domain.Criteria.Criteria import Criteria
from sqlalchemy.orm import Session

class SAReservaRepository(BaseSQLAlchemyRepository[Reserva, ReservaModel], ReservaRepositoryInterface):
    def __init__(self, engine: Engine):
        super().__init__(engine, ReservaModel)
        
    def matching(self, criteria: Criteria) -> list[Reserva]:
        with Session(self.engine) as session:
            query = self.criteria_converter.convert(self.model_class, criteria)
            results = session.execute(query).scalars().all()
            return [self.model_to_entity(model) for model in results]
    
    def model_to_entity(self, model: ReservaModel) -> Reserva:
        return Reserva(
            id=str(model.id),
            fecha_hora=model.fecha_hora,
            duracion=model.duracion,
            cancha_id=str(model.cancha_id),
            jugador_id=str(model.jugador_id),
            now=model.created_at
        )
    
    def entity_to_model(self, entity: Reserva) -> ReservaModel:
        return ReservaModel(
            id=entity.id.value,
            fecha_hora=entity.fecha_hora.value,
            duracion=entity.duracion.value,
            cancha_id=entity.cancha_id.value,
            jugador_id=entity.jugador_id.value
        )
    
    def entity_to_update_values(self, entity: Reserva) -> dict[str, Any]:
        return {
            "fecha_hora": entity.fecha_hora.value,
            "duracion": entity.duracion.value,
            "cancha_id": entity.cancha_id.value,
            "jugador_id": entity.jugador_id.value
        } 