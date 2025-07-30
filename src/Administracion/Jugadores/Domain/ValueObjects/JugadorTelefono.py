from dataclasses import dataclass
from src.SharedKernel.Domain.ValueObjects.RequiredStringValueObject import RequiredStringValueObject
from src.Administracion.Jugadores.Domain.Exceptions.InvalidTelefonoException import InvalidTelefonoException

@dataclass(frozen=True)
class JugadorTelefono(RequiredStringValueObject):
    def __post_init__(self):
        self._ensure_only_digits()
        self._ensure_between_7_and_15_digits()
        
    def _ensure_only_digits(self) -> None:
        if not self.value.isdigit():
            raise InvalidTelefonoException("El teléfono debe contener solo dígitos")
    
    def _ensure_between_7_and_15_digits(self) -> None:
        if len(self.value) < 7 or len(self.value) > 15:
            raise InvalidTelefonoException("El teléfono debe tener entre 7 y 15 dígitos")