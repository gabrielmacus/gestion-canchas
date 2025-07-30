from dataclasses import dataclass


@dataclass(frozen=True)
class FilterValue:
    value: str