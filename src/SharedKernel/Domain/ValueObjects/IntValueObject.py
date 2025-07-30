from dataclasses import dataclass

@dataclass(frozen=True)
class IntValueObject:
    value: int
    