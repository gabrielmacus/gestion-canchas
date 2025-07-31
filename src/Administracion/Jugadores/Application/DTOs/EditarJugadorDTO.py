from pydantic import BaseModel, EmailStr, field_validator
from typing import Optional
from pydantic_core import PydanticCustomError

class EditarJugadorDTO(BaseModel):
    nombre: Optional[str]
    apellido: Optional[str]
    telefono: Optional[str]
    email: Optional[EmailStr]
    
    @field_validator('telefono')
    @classmethod
    def validar_telefono(cls, v: str | None) -> str | None:
        if v is None:
            return v
            
        # Remover espacios en blanco si los hay
        v = v.strip()
        # Validar que solo contenga dígitos
        if not v.isdigit():
            raise PydanticCustomError(
                'telefono_format',
                'El teléfono debe contener solo dígitos numéricos'
            )
        # Validar longitud
        if not (7 <= len(v) <= 15):
            raise PydanticCustomError(
                'telefono_length',
                'El teléfono debe tener entre 7 y 15 dígitos'
            )
        return v