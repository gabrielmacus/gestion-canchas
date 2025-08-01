from typing import Optional
from pydantic import BaseModel, field_validator
from pydantic_core import PydanticCustomError

class EditarCanchaDTO(BaseModel):
    nombre: Optional[str]
    techada: Optional[bool]
    
    @field_validator('nombre')
    @classmethod
    def validar_nombre(cls, v: str | None) -> str | None:
        if v is None:
            return v
            
        v = v.strip()
        if len(v) < 3 or len(v) > 100:
            raise PydanticCustomError(
                'nombre_length',
                'El nombre de la cancha debe tener entre 3 y 100 caracteres'
            )
        return v