from dataclasses import dataclass
from src.Administracion.Reservas.Domain.Exceptions.InvalidDuracionException import InvalidDuracionException
from src.SharedKernel.Domain.ValueObjects.IntValueObject import IntValueObject

@dataclass(frozen=True)
class ReservaDuracionMinutos(IntValueObject):
    
    def __post_init__(self):
        self._ensure_is_greater_than_0()
        self._ensure_is_multiple_of_60_minutes()
        self._ensure_is_min_1_hour()
        self._ensure_is_up_to_4_hours()
    
    def _ensure_is_greater_than_0(self) -> None:
        if self.value <= 0:
            raise InvalidDuracionException("La duración de la reserva no puede ser menor o igual a 0")
        
    def _ensure_is_up_to_4_hours(self) -> None:
        if self.value > 240:
            raise InvalidDuracionException("La duración de la reserva no puede ser mayor a 4 horas")
    
    def _ensure_is_multiple_of_60_minutes(self) -> None:
        if self.value % 60 != 0:
            raise InvalidDuracionException("La duración de la reserva debe ser múltiplo de 60 minutos")
    
    def _ensure_is_min_1_hour(self) -> None:
        if self.value < 60:
            raise InvalidDuracionException("La duración de la reserva debe ser al menos de 1 hora")
    