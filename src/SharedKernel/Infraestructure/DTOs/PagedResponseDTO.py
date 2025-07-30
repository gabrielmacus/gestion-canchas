from dataclasses import dataclass
from typing import Generic, TypeVar
T = TypeVar('T')

@dataclass(frozen=True)
class PagedResponseDTO(Generic[T]):
    items: list[T]
    total: int
    page_size: int
    page_number: int