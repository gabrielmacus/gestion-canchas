from dataclasses import dataclass

@dataclass(frozen=True)
class PageSize:
    value: int | None
    
    def __post_init__(self):
        if self.value is not None and self.value <= 0:
            raise ValueError("Page size must be greater than 0")