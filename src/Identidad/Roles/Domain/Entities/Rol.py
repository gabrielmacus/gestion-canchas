from src.SharedKernel.Domain.Entities.AggregateRoot import AggregateRoot
from src.Identidad.Roles.Domain.ValueObjects.RolId import RolId
from src.Identidad.Roles.Domain.ValueObjects.RolNombre import RolNombre
from src.Identidad.Roles.Domain.ValueObjects.RolPermisos import RolPermisos
from dataclasses import dataclass
from typing import List

@dataclass
class Rol(AggregateRoot):
    _id: RolId
    _nombre: RolNombre
    _permisos: RolPermisos
    
    def __init__(self, id: str, nombre: str, permisos: List[str]):
        self._id = RolId(id)
        self._nombre = RolNombre(nombre)
        self._permisos = RolPermisos(permisos)
        
        super().__init__()
    
    @property
    def id(self):
        return self._id
    
    @property
    def nombre(self):
        return self._nombre
    
    @property
    def permisos(self):
        return self._permisos
    
    @staticmethod
    def create(id: str, nombre: str, permisos: List[str]):
        # TODO: Domain event
        return Rol(id, nombre, permisos)
    
    def has_permission(self, permission: str) -> bool:
        """Verifica si el rol tiene un permiso específico"""
        return self._permisos.has_permission(permission)
    
    def has_any_permission(self, permissions: List[str]) -> bool:
        """Verifica si el rol tiene al menos uno de los permisos especificados"""
        return any(self.has_permission(permission) for permission in permissions)
    
    def has_all_permissions(self, permissions: List[str]) -> bool:
        """Verifica si el rol tiene todos los permisos especificados"""
        return all(self.has_permission(permission) for permission in permissions) 