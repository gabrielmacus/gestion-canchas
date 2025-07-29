from dataclasses import dataclass
from datetime import datetime, timedelta
from src.Administracion.Reservas.Domain.Exceptions.InvalidFechaHoraException import InvalidFechaHoraException
from src.SharedKernel.Domain.ValueObjects.DateTimeValueObject import DateTimeValueObject

@dataclass(frozen=True)
class ReservaFechaHora(DateTimeValueObject):
    now: datetime
    def __post_init__(self):
        self._ensure_is_greater_than_now()
        self._ensure_is_less_than_3_months_from_now()
    
    def _ensure_is_greater_than_now(self) -> None:
        # TODO: Verificar si es pertinente. Ej: llegan jugadores sobre la hora y aceptan jugar menos del tiempo pagado, pero deseo cargar igual la reserva.
        if self.value < self.now:
            raise InvalidFechaHoraException("La fecha de la reserva no puede ser menor a la fecha actual")
        
    def _ensure_is_less_than_3_months_from_now(self) -> None:
        if self.value > self.now + timedelta(days=90):
            raise InvalidFechaHoraException("La fecha no puede ser mayor a 3 meses desde la fecha actual")
        
    def _ensure_is_at_hour_start(self) -> None:
        if self.value.minute != 0:
            raise InvalidFechaHoraException("Los minutos deben ser 0")