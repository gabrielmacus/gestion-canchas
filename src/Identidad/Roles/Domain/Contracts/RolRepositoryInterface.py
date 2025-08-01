from abc import ABC
from Identidad.Roles.Domain.Entities.Rol import Rol
from src.SharedKernel.Domain.Contracts.Repository.RepositoryInterface import RepositoryInterface

class RolRepositoryInterface(RepositoryInterface[Rol]):
    pass