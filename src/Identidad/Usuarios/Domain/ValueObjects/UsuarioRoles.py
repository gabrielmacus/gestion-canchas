from dataclasses import dataclass
from src.Identidad.Roles.Domain.Entities.Rol import Rol

@dataclass
class UsuarioRoles:
    ids: list[str] = []