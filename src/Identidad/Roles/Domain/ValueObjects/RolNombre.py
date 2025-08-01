from dataclasses import dataclass
from src.Identidad.Roles.Domain.Exceptions.InvalidRolNombreException import InvalidRolNombreException
from src.SharedKernel.Domain.ValueObjects.RequiredStringValueObject import RequiredStringValueObject

@dataclass(frozen=True)
class RolNombre(RequiredStringValueObject):
    def __post_init__(self):
        super().__post_init__()
        self._ensure_is_between_2_and_50_characters()
        self._ensure_has_valid_format()
    
    def _ensure_is_between_2_and_50_characters(self) -> None:
        if len(self.value) < 2 or len(self.value) > 50:
            raise InvalidRolNombreException("El nombre del rol debe tener entre 2 y 50 caracteres")
    
    def _ensure_has_valid_format(self) -> None:
        # El nombre del rol debe ser alfanumérico con espacios y guiones permitidos
        import re
        if not re.match(r'^[a-zA-ZáéíóúÁÉÍÓÚñÑ0-9\s\-_]+$', self.value):
            raise InvalidRolNombreException("El nombre del rol solo puede contener letras, números, espacios, guiones y guiones bajos") 