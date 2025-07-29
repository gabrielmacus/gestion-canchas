from dataclasses import dataclass
from src.Administracion.Jugadores.Domain.Exceptions.InvalidNombreException import InvalidNombreException
from src.SharedKernel.Domain.ValueObjects.RequiredStringValueObject import RequiredStringValueObject

@dataclass(frozen=True)
class JugadorNombre(RequiredStringValueObject):
    def __post_init__(self):
        self._ensure_is_between_3_and_100_characters()
    
    def _ensure_is_between_3_and_100_characters(self) -> None:
        if len(self.value) < 3 or len(self.value) > 100:
            raise InvalidNombreException("El nombre del jugador debe tener entre 3 y 100 caracteres")