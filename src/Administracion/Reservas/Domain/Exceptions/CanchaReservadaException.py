from datetime import datetime
from src.SharedKernel.Domain.Exceptions.DomainException import DomainException

class CanchaReservadaException(DomainException):
    def __init__(self, cancha_id: str, fecha_hora: datetime):
        super().__init__(f"La cancha {cancha_id} ya tiene una reserva en el horario {fecha_hora}")