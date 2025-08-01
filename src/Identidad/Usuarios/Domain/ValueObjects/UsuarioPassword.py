from dataclasses import dataclass
import re
from src.SharedKernel.Domain.ValueObjects.RequiredStringValueObject import RequiredStringValueObject
from src.Identidad.Usuarios.Domain.Exceptions.InvalidPasswordException import InvalidPasswordException

@dataclass(frozen=True)
class UsuarioPassword(RequiredStringValueObject):
    def __post_init__(self):
        super().__post_init__()
        self._ensure_meets_security_requirements()
    
    # TODO: revisar
    def _ensure_meets_security_requirements(self) -> None:
        if len(self.value) < 8:
            raise InvalidPasswordException("La contraseña debe tener al menos 8 caracteres")
        
        if len(self.value) > 128:
            raise InvalidPasswordException("La contraseña no puede tener más de 128 caracteres")
        
        if not re.search(r'[A-Z]', self.value):
            raise InvalidPasswordException("La contraseña debe contener al menos una letra mayúscula")
        
        if not re.search(r'[a-z]', self.value):
            raise InvalidPasswordException("La contraseña debe contener al menos una letra minúscula")
        
        if not re.search(r'\d', self.value):
            raise InvalidPasswordException("La contraseña debe contener al menos un número")
        
        if not re.search(r'[!@#$%^&*(),.?":{}|<>]', self.value):
            raise InvalidPasswordException("La contraseña debe contener al menos un carácter especial") 