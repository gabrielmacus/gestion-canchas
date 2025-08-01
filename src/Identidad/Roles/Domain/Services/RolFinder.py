from src.Identidad.Roles.Domain.Contracts.RolRepositoryInterface import RolRepositoryInterface
from src.Identidad.Roles.Domain.Entities.Rol import Rol
from src.Identidad.Roles.Domain.Exceptions.RolNotFound import RolNotFound

class RolFinder:
    def __init__(self, rol_repository: RolRepositoryInterface):
        self._rol_repository = rol_repository
    
    def find_by_id(self, id: str) -> Rol:
        rol = self._rol_repository.get_by_id(id)
        self._ensure_rol_exists(rol, id)
        assert rol is not None
        return rol
    
    def _ensure_rol_exists(self, rol: Rol | None, id: str) -> None:
        if rol is None:
            raise RolNotFound(f"Rol con id {id} no encontrado")