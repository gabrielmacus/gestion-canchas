from typing import final
from src.Administracion.Jugadores.Infraestructure.Models.JugadorModel import JugadorModel
from src.SharedKernel.Infraestructure.Criteria.CriteriaToSQLAlchemyConverter import CriteriaToSQLAlchemyConverter
from src.Administracion.Jugadores.Domain.Contracts.JugadorRepositoryInterface import JugadorRepositoryInterface
from src.Administracion.Jugadores.Domain.Entities.Jugador import Jugador
from sqlalchemy.orm import Session
from src.SharedKernel.Domain.Criteria.Criteria import Criteria
from sqlalchemy import Engine

@final
class SAJugadorRepository(JugadorRepositoryInterface):
    
    def __init__(self, engine: Engine):
        self.engine = engine
        self.criteria_converter = CriteriaToSQLAlchemyConverter()

    #def add(self, jugador: Jugador):
    #    JugadorModel()
    #    #self.db.session.add(jugador)
    #    #self.db.session.commit()
    
    def matching(self, criteria: Criteria) -> list[Jugador]:
        with Session(self.engine) as session:
            query = self.criteria_converter.convert(JugadorModel, criteria)
            results = session.execute(query).scalars().all()
            return []
            '''
            return [
                Jugador.create(
                    jugador.id.v,
                    jugador.nombre.value,
                    jugador.apellido.value,
                    jugador.telefono.value,
                    jugador.email.value
                ) for jugador in results]
            '''
    
    def update(self, jugador: Jugador) -> None:
        pass
    
    def delete_by_id(self, id: str) -> None:
        pass
    
    def add(self, jugador: Jugador) -> None:
        pass