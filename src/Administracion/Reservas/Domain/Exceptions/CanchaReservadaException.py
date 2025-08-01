from datetime import datetime
from src.SharedKernel.Domain.Exceptions.DomainException import DomainException

class CanchaReservadaException(DomainException):
    def __init__(self, cancha_id: str, fecha_hora: datetime):
        self.cancha_id = cancha_id
        self.fecha_hora = fecha_hora
        super().__init__(f"Cancha no disponible en el horario seleccionado")