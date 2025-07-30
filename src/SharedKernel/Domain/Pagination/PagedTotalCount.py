from dataclasses import dataclass

@dataclass(frozen=True)
class PagedTotalCount:
    value: int
        
    def __post_init__(self):
        self._ensure_value_is_zero_or_positive()
        
    def _ensure_value_is_zero_or_positive(self):
        if self.value < 0:
            raise ValueError("PagedTotalCount must be greater than 0")