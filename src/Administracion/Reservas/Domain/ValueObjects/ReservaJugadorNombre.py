from dataclasses import dataclass
from src.SharedKernel.Domain.ValueObjects.RequiredStringValueObject import RequiredStringValueObject

@dataclass(frozen=True)
class ReservaJugadorNombre(RequiredStringValueObject):
    pass 