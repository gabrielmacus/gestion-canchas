from dataclasses import dataclass

@dataclass(frozen=True)
class PagedPageSize:
    value: int
    
    def __post_init__(self):
        if self.value <= 0:
            raise ValueError("El tamaño de la página debe ser mayor a 0")
    
    def _ensure_positive(self):
        if self.value <= 0:
            raise ValueError("El tamaño de la página debe ser mayor a 0")
    