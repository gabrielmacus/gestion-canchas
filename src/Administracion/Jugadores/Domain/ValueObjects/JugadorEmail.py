from dataclasses import dataclass
import re
from src.SharedKernel.Domain.ValueObjects.StringValueObject import StringValueObject
from src.Administracion.Jugadores.Domain.Exceptions.InvalidEmailException import InvalidEmailException

@dataclass(frozen=True)
class JugadorEmail(StringValueObject):
    def __post_init__(self):
        self._ensure_is_valid()
    
    def _ensure_is_valid(self) -> None:
        if self.value is not None and not re.match(r"[^@]+@[^@]+\.[^@]+", self.value):
            raise InvalidEmailException("El email no es válido")