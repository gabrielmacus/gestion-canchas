from typing import final
from uuid import UUID
from src.Administracion.Jugadores.Infraestructure.Models.JugadorModel import JugadorModel
from src.SharedKernel.Infraestructure.Repository.BaseSQLAlchemyRepository import BaseSQLAlchemyRepository
from src.Administracion.Jugadores.Domain.Contracts.JugadorRepositoryInterface import JugadorRepositoryInterface
from src.Administracion.Jugadores.Domain.Entities.Jugador import Jugador
from sqlalchemy import Engine

@final
class SAJugadorRepository(
    BaseSQLAlchemyRepository[Jugador, JugadorModel], JugadorRepositoryInterface):
    
    def __init__(self, engine: Engine):
        super().__init__(engine, JugadorModel)
    
    def model_to_entity(self, model: JugadorModel) -> Jugador:
        """Convierte un modelo SQLAlchemy a entidad de dominio"""
        return Jugador.create(
            str(model.id),
            str(model.nombre),
            str(model.apellido),
            str(model.telefono),
            None if model.email is None else str(model.email)
        )
    
    def entity_to_model(self, entity: Jugador) -> JugadorModel:
        """Convierte una entidad de dominio a modelo SQLAlchemy"""
        return JugadorModel(
            id=UUID(entity.id.value),
            nombre=entity.nombre.value,
            apellido=entity.apellido.value,
            telefono=entity.telefono.value,
            email= None if entity.email.value is None else entity.email.value # TODO: ejemplo de errores de IA: aca no me habia agregado el value
        )
    
    def entity_to_update_values(self, entity: Jugador) -> dict[str, str | None]:
        """Convierte una entidad a un diccionario de valores para update"""
        return {
            "nombre": entity.nombre.value,
            "apellido": entity.apellido.value,
            "telefono": entity.telefono.value,
            "email": entity.email.value if entity.email is not None else None
        }

