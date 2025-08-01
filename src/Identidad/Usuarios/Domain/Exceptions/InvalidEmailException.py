from src.SharedKernel.Domain.Exceptions.DomainException import DomainException

class InvalidEmailException(DomainException):
    def __init__(self, email: str):
        super().__init__(f"El email {email} no es válido") 