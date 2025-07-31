from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, DateTime, Integer
from src.SharedKernel.Infraestructure.Models.BaseSQLAlchemyModel import BaseSQLAlchemyModel
from datetime import datetime

class ReservaModel(BaseSQLAlchemyModel):
    __tablename__ = "reservas"
    
    fecha_hora: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    duracion: Mapped[int] = mapped_column(Integer, nullable=False)
    cancha_id: Mapped[str] = mapped_column(String, nullable=False)
    jugador_id: Mapped[str] = mapped_column(String, nullable=False) 