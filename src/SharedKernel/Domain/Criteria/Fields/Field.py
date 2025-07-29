from dataclasses import dataclass

@dataclass(frozen=True)
class Field:
    value: str