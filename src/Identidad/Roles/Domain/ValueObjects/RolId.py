from dataclasses import dataclass
from src.SharedKernel.Domain.ValueObjects.GuidValueObject import GuidValueObject

@dataclass(frozen=True)
class RolId(GuidValueObject):
    pass 