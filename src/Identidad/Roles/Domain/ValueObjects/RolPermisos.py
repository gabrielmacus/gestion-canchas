from dataclasses import dataclass
from typing import List
from src.Identidad.Roles.Domain.Exceptions.InvalidPermisosException import InvalidPermisosException

@dataclass(frozen=True)
class RolPermisos:
    value: List[str]
    
    def __post_init__(self):
        self._ensure_is_valid_list()
        self._ensure_no_empty_permissions()
        self._ensure_no_duplicate_permissions()
        self._ensure_valid_permission_format()
    
    def _ensure_is_valid_list(self) -> None:
        if not isinstance(self.value, list):
            raise InvalidPermisosException("Los permisos deben ser una lista")
    
    def _ensure_no_empty_permissions(self) -> None:
        if any(not permission or not permission.strip() for permission in self.value):
            raise InvalidPermisosException("Los permisos no pueden estar vacíos")
    
    def _ensure_no_duplicate_permissions(self) -> None:
        if len(self.value) != len(set(self.value)):
            raise InvalidPermisosException("No puede haber permisos duplicados")
    
    def _ensure_valid_permission_format(self) -> None:
        # Los permisos deben seguir el formato: modulo:accion (ej: "usuarios:crear", "reportes:leer")
        import re
        permission_pattern = r'^[a-zA-Z][a-zA-Z0-9_]*:[a-zA-Z][a-zA-Z0-9_]*$'
        
        for permission in self.value:
            if not re.match(permission_pattern, permission):
                raise InvalidPermisosException(f"El permiso '{permission}' debe seguir el formato 'modulo:accion' (ej: 'usuarios:crear')")
    
    def has_permission(self, permission: str) -> bool:
        """Verifica si el rol tiene un permiso específico"""
        return permission in self.value
    
    def add_permission(self, permission: str) -> 'RolPermisos':
        """Retorna un nuevo RolPermisos con el permiso agregado"""
        if permission in self.value:
            return self
        new_permissions = self.value + [permission]
        return RolPermisos(new_permissions)
    
    def remove_permission(self, permission: str) -> 'RolPermisos':
        """Retorna un nuevo RolPermisos sin el permiso especificado"""
        if permission not in self.value:
            return self
        new_permissions = [p for p in self.value if p != permission]
        return RolPermisos(new_permissions) 