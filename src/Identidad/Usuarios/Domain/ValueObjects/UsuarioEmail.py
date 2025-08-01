from dataclasses import dataclass
import re
from src.SharedKernel.Domain.ValueObjects.RequiredStringValueObject import RequiredStringValueObject
from src.Identidad.Usuarios.Domain.Exceptions.InvalidEmailException import InvalidEmailException

@dataclass(frozen=True)
class UsuarioEmail(RequiredStringValueObject):
    def __post_init__(self):
        super().__post_init__()
        self._ensure_is_valid_email()
    
    def _ensure_is_valid_email(self) -> None:
        email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.match(email_pattern, self.value):
            raise InvalidEmailException("El formato del email no es válido") 