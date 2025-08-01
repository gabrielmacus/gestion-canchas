from pydantic import BaseModel

class CanchaDTO(BaseModel):
    id: str
    nombre: str
    techada: bool 
    