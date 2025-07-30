from dataclasses import dataclass

@dataclass(frozen=True)
class PagedPageNumber:
    value: int
    
    def __post_init__(self):
        self._ensure_positive()
    
    def _ensure_positive(self):
        if self.value <= 0:
            raise ValueError("El número de página debe ser mayor a 0")
    
    def __int__(self):
        return self.value