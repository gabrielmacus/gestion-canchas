from dataclasses import dataclass
from enum import Enum

class TipoEstadoUsuario(Enum):
    INACTIVO = 0
    ACTIVO = 1
    
@dataclass(frozen=True)
class UsuarioEstado():
    value: TipoEstadoUsuario
    