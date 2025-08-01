from dataclasses import dataclass
from datetime import datetime
from src.SharedKernel.Domain.ValueObjects.DateTimeValueObject import DateTimeValueObject

@dataclass(frozen=True)
class UsuarioFechaRegistro(DateTimeValueObject):
    def __post_init__(self):
        self._ensure_is_not_future()
    
    def _ensure_is_not_future(self) -> None:
        if self.value > datetime.utcnow():
            raise ValueError("La fecha de registro no puede ser en el futuro")
    
    @classmethod
    def now(cls) -> 'UsuarioFechaRegistro':
        return cls(datetime.utcnow()) 