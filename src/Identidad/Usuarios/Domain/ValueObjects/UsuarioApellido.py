from dataclasses import dataclass
from src.SharedKernel.Domain.ValueObjects.RequiredStringValueObject import RequiredStringValueObject
from src.Identidad.Usuarios.Domain.Exceptions.InvalidNombreException import InvalidNombreException

@dataclass(frozen=True)
class UsuarioApellido(RequiredStringValueObject):
    def __post_init__(self):
        super().__post_init__()
        self._ensure_is_between_2_and_50_characters()
        self._ensure_is_alphabetic()
    
    def _ensure_is_between_2_and_50_characters(self) -> None:
        if len(self.value) < 2 or len(self.value) > 50:
            raise InvalidNombreException("El apellido del usuario debe tener entre 2 y 50 caracteres")
    
    def _ensure_is_alphabetic(self) -> None:
        if not self.value.replace(" ", "").replace("-", "").isalpha():
            raise InvalidNombreException("El apellido solo puede contener letras, espacios y guiones") 