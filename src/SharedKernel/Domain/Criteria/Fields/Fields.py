from dataclasses import dataclass
from .Field import Field

@dataclass(frozen=True)
class Fields:
    value: list[Field] | None