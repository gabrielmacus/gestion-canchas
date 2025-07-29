from dataclasses import dataclass

@dataclass(frozen=True)
class OrderBy:
    value: str