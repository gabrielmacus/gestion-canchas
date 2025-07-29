from dataclasses import dataclass
from .Filter import Filter


@dataclass(frozen=True)
class Filters:
    value: list[Filter] | None