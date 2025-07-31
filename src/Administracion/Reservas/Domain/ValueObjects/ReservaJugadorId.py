from dataclasses import dataclass
from src.SharedKernel.Domain.ValueObjects.GuidValueObject import GuidValueObject

@dataclass(frozen=True)
class ReservaJugadorId(GuidValueObject):
    pass 