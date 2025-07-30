from sqlalchemy.orm import Mapped, mapped_column
from src.SharedKernel.Infraestructure.Models.BaseSQLAlchemyModel import BaseSQLAlchemyModel
from sqlalchemy import  String

class JugadorModel(BaseSQLAlchemyModel):
    __tablename__:str = "jugadores"
    nombre: Mapped[str] = mapped_column(String, nullable=False)
    apellido: Mapped[str] = mapped_column(String, nullable=False)
    email: Mapped[str] = mapped_column(String, nullable=True)
    telefono: Mapped[str] = mapped_column(String, nullable=False)
