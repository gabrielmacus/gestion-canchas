from pydantic import BaseModel, EmailStr, model_validator, field_validator
from typing import Optional
import re
from pydantic_core import PydanticCustomError

class CrearJugadorDTO(BaseModel):
    id: str
    nombre: str
    apellido: str
    email: Optional[EmailStr] = None
    telefono: str
    
    @field_validator('nombre')
    @classmethod
    def validar_nombre(cls, v: str) -> str:
        v = v.strip()
        if len(v) < 3 or len(v) > 100:
            raise PydanticCustomError(
                'nombre_length',
                'El nombre del jugador debe tener entre 3 y 100 caracteres'
            )
        return v
    
    @field_validator('apellido')
    @classmethod
    def validar_apellido(cls, v: str) -> str:
        v = v.strip()
        if len(v) < 3 or len(v) > 100:
            raise PydanticCustomError(
                'apellido_length',
                'El apellido del jugador debe tener entre 3 y 100 caracteres'
            )
        return v
    
    @field_validator('telefono')
    @classmethod
    def validar_telefono(cls, v: str) -> str:
        # Remover espacios en blanco si los hay
        v = v.strip()
        # Validar que solo contenga dígitos
        if not v.isdigit():
            raise PydanticCustomError(
                'telefono_format',
                'El teléfono debe contener solo dígitos'
            )
        # Validar longitud
        if not (7 <= len(v) <= 15):
            raise PydanticCustomError(
                'telefono_length',
                'El teléfono debe tener entre 7 y 15 dígitos'
            )
        return v
    
    @field_validator('email')
    @classmethod
    def validar_email(cls, v: EmailStr | None) -> EmailStr | None:
        if v is not None and not re.match(r"[^@]+@[^@]+\.[^@]+", str(v)):
            raise PydanticCustomError(
                'email_format',
                'El email no es válido'
            )
        return v
    
    @model_validator(mode='after')
    def validar_contacto(self):
        if not self.email and not self.telefono:
            raise PydanticCustomError( 'contacto_missing','Debe proporcionar al menos un email o un teléfono')
        return self
    
    