from abc import ABC, abstractmethod
from typing import TypeVar, Generic, Type, Any
from sqlalchemy.orm import Session, DeclarativeBase
from sqlalchemy import Engine, delete, update
from src.SharedKernel.Domain.Contracts.Repository.RepositoryInterface import RepositoryInterface
from src.SharedKernel.Domain.Criteria.Criteria import Criteria
from src.SharedKernel.Domain.Criteria.CountCriteria import CountCriteria
from src.SharedKernel.Infraestructure.Criteria.CriteriaToSQLAlchemyConverter import CriteriaToSQLAlchemyConverter

T = TypeVar('T')  # Domain Entity
M = TypeVar('M', bound=DeclarativeBase)  # SQLAlchemy Model

class BaseSQLAlchemyRepository(RepositoryInterface[T], ABC, Generic[T, M]):
    
    def __init__(self, engine: Engine, model_class: Type[M]):
        self.engine = engine
        self.model_class = model_class
        self.criteria_converter = CriteriaToSQLAlchemyConverter()
    
    def count_matching(self, criteria: Criteria) -> int:
        with Session(self.engine) as session:
            count_criteria = CountCriteria.from_criteria(criteria)
            query = self.criteria_converter.convert_count(self.model_class, count_criteria)
            return session.execute(query).scalar_one()
    
    def matching(self, criteria: Criteria) -> list[T]:
        with Session(self.engine) as session:
            query = self.criteria_converter.convert(self.model_class, criteria)
            results = session.execute(query).scalars().all()
            return [self.model_to_entity(model) for model in results]
    
    def update_by_id(self, id: str, entity: T) -> None:
        with Session(self.engine) as session:
            update_values = self.entity_to_update_values(entity)
            # type: ignore en la siguiente línea es necesario debido a limitaciones del sistema de tipos con genéricos
            update_query = update(self.model_class).where(self.model_class.id == id).values(**update_values)  # type: ignore
            session.execute(update_query)
            session.commit()
    
    def delete_by_id(self, id: str) -> None:
        with Session(self.engine) as session:
            # type: ignore en la siguiente línea es necesario debido a limitaciones del sistema de tipos con genéricos
            delete_query = delete(self.model_class).where(self.model_class.id == id)  # type: ignore
            session.execute(delete_query)
            session.commit()
    
    def add(self, entity: T) -> None:
        with Session(self.engine) as session:
            model_instance = self.entity_to_model(entity)
            session.add(model_instance)
            session.commit()
    
    @abstractmethod
    def model_to_entity(self, model: M) -> T:
        """Convierte un modelo SQLAlchemy a entidad de dominio"""
        pass
    
    @abstractmethod
    def entity_to_model(self, entity: T) -> M:
        """Convierte una entidad de dominio a modelo SQLAlchemy"""
        pass
    
    @abstractmethod
    def entity_to_update_values(self, entity: T) -> dict[str, Any]:
        """Convierte una entidad a un diccionario de valores para update"""
        pass 