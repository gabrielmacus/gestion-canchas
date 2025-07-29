from src.SharedKernel.Infraestructure.Models.BaseSQLAlchemyModel import BaseSQLAlchemyModel

from sqlalchemy import Column, String

class JugadorModel(BaseSQLAlchemyModel):
    __tablename__:str = "jugadores"
    nombre: Column[str] = Column(String, nullable=False)
    apellido: Column[str] = Column(String, nullable=False)
    email: Column[str] = Column(String, nullable=True)
    telefono: Column[str] = Column(String, nullable=True)