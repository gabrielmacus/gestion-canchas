from pydantic import BaseModel, field_validator
from pydantic_core import PydanticCustomError

class CrearCanchaDTO(BaseModel):
    id: str
    nombre: str
    techada: bool
    
    @field_validator('nombre')
    @classmethod
    def validar_nombre(cls, v: str) -> str:
        v = v.strip()
        if len(v) < 3 or len(v) > 100:
            raise PydanticCustomError(
                'nombre_length',
                'El nombre de la cancha debe tener entre 3 y 100 caracteres'
            )
        return v