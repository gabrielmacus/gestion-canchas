from dataclasses import dataclass


@dataclass(frozen=True)
class FilterField:
    value: str
    