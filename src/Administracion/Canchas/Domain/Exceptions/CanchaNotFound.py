from src.SharedKernel.Domain.Exceptions.DomainException import DomainException

class CanchaNotFound(DomainException):
    def __init__(self, id: str):
        self.id = id
        super().__init__(f"Cancha con id {id} no encontrada") 