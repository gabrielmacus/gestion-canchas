from dataclasses import dataclass

@dataclass(frozen=True)
class Pagination:
    size: int
    page: int
    
    def __post_init__(self):
        if self.size <= 0:
            raise ValueError("Size must be greater than 0")
        if self.page <= 0:
            raise ValueError("Page must be greater than 0")