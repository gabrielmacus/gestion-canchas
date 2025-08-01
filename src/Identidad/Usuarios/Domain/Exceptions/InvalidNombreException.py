from src.SharedKernel.Domain.Exceptions.DomainException import DomainException

class InvalidNombreException(DomainException):
    def __init__(self, nombre: str):
        super().__init__(f"El nombre {nombre} no es válido")    