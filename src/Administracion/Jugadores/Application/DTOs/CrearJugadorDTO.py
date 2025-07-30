from pydantic import BaseModel, EmailStr, model_validator, field_validator
from typing import Optional

from pydantic_core import PydanticCustomError

class CrearJugadorDTO(BaseModel):
    id: str
    nombre: str
    apellido: str
    email: Optional[EmailStr] = None
    telefono: str
    
    @field_validator('telefono')
    @classmethod
    def validar_telefono(cls, v: str) -> str:
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
    
    @model_validator(mode='after')
    def validar_contacto(self):
        if not self.email and not self.telefono:
            raise PydanticCustomError( 'contacto_missing','Debe proporcionar al menos un email o un teléfono')
        return self
    
    