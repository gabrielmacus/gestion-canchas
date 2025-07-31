from src.SharedKernel.Domain.Exceptions.DomainException import DomainException

class ReservaNotFound(DomainException):
    def __init__(self, id: str):
        self.id = id
        super().__init__(f"Reserva con id {id} no encontrada") 