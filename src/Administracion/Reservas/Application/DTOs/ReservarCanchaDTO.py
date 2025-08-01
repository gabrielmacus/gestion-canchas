from pydantic import BaseModel, field_validator
from datetime import datetime, timedelta
from pydantic_core import PydanticCustomError
from pydantic import BaseModel
from datetime import datetime

class ReservarCanchaDTO(BaseModel):
    id: str
class ReservarCanchaDTO(BaseModel):
    id_reserva: str
    fecha_hora: datetime
    duracion: int
    cancha_id: str
    jugador_id: str
    
    @field_validator('fecha_hora')
    @classmethod
    def validar_fecha_hora(cls, v: datetime) -> datetime:
        now = datetime.now()
        
        # Validar que sea mayor a ahora
        if v < now:
            raise PydanticCustomError(
                'fecha_hora_past',
                'La fecha de la reserva no puede ser menor a la fecha actual'
            )
        
        # Validar que sea menor a 3 meses desde ahora
        if v > now + timedelta(days=90):
            raise PydanticCustomError(
                'fecha_hora_future',
                'La fecha no puede ser mayor a 3 meses desde la fecha actual'
            )
        
        # Validar que sea hora exacta
        if v.minute != 0 or v.second != 0:
            raise PydanticCustomError(
                'fecha_hora_exact',
                'La hora de reserva debe ser exacta (minutos y segundos deben ser 0)'
            )
        
        return v
    
    @field_validator('duracion')
    @classmethod
    def validar_duracion(cls, v: int) -> int:
        # Validar que sea mayor a 0
        if v <= 0:
            raise PydanticCustomError(
                'duracion_positive',
                'La duración de la reserva no puede ser menor o igual a 0'
            )
        
        # Validar que sea múltiplo de 60 minutos
        if v % 60 != 0:
            raise PydanticCustomError(
                'duracion_multiple',
                'La duración de la reserva debe ser múltiplo de 60 minutos'
            )
        
        # Validar que sea mínimo 1 hora
        if v < 60:
            raise PydanticCustomError(
                'duracion_min',
                'La duración de la reserva debe ser al menos de 1 hora'
            )
        
        # Validar que sea máximo 4 horas
        if v > 240:
            raise PydanticCustomError(
                'duracion_max',
                'La duración de la reserva no puede ser mayor a 4 horas'
            )
        
        return v