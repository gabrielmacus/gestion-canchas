from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Boolean
from src.SharedKernel.Infraestructure.Models.BaseSQLAlchemyModel import BaseSQLAlchemyModel

# Solución al conflicto de metaclases: invertir el orden de herencia
class CanchaModel(BaseSQLAlchemyModel):
    __tablename__ = "canchas"
    
    nombre: Mapped[str] = mapped_column(String, nullable=False)
    techada: Mapped[bool] = mapped_column(Boolean, nullable=False)