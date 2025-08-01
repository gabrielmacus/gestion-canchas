from src.SharedKernel.Domain.Exceptions.DomainException import DomainException

class InvalidPasswordException(DomainException):
    def __init__(self, password: str):
        super().__init__(f"La contraseña {password} no es válida") 
        # Muestro la contraseña porque no es válida y no se utilizará