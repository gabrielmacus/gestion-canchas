from dataclasses import dataclass
from enum import Enum
from src.SharedKernel.Domain.ValueObjects.StringValueObject import StringValueObject
from src.Identidad.Usuarios.Domain.Exceptions.InvalidEstadoException import InvalidEstadoException

class TipoEstadoUsuario(Enum):
    INACTIVO = 0
    ACTIVO = 1
    
@dataclass(frozen=True)
class UsuarioEstado():
    value: TipoEstadoUsuario
    