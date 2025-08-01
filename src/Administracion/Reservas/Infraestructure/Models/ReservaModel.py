from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import DateTime, Integer, ForeignKey    
from src.SharedKernel.Infraestructure.Models.BaseSQLAlchemyModel import BaseSQLAlchemyModel
from datetime import datetime
from typing import TYPE_CHECKING
import uuid

if TYPE_CHECKING:
    from src.Administracion.Canchas.Infraestructure.Models.CanchaModel import CanchaModel
    from src.Administracion.Jugadores.Infraestructure.Models.JugadorModel import JugadorModel

class ReservaModel(BaseSQLAlchemyModel):
    __tablename__ = "reservas"
    
    fecha_hora: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    duracion: Mapped[int] = mapped_column(Integer, nullable=False)
    cancha_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("canchas.id"), nullable=False)
    jugador_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("jugadores.id"), nullable=False)
    
    # Relaciones
    cancha: Mapped["CanchaModel"] = relationship("CanchaModel", lazy="subquery")
    jugador: Mapped["JugadorModel"] = relationship("JugadorModel", lazy="subquery") 