from dataclasses import dataclass
from src.SharedKernel.Domain.ValueObjects.StringValueObject import StringValueObject

@dataclass(frozen=True)
class RequiredStringValueObject(StringValueObject):
    value:str
    
    def __post_init__(self):
        self._ensure_is_not_empty()
        
    def _ensure_is_not_empty(self):
        if not self.value or not self.value.strip():
            raise ValueError("Value cannot be empty")

