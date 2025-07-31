from typing import Optional
from pydantic import BaseModel

class EditarCanchaDTO(BaseModel):
    nombre: Optional[str]
    techada: Optional[bool]