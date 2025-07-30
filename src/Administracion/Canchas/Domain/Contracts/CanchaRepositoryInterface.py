from abc import ABC
from src.Administracion.Canchas.Domain.Entities.Cancha import Cancha
from src.SharedKernel.Domain.Contracts.Repository.RepositoryInterface import RepositoryInterface


class CanchaRepositoryInterface(RepositoryInterface[Cancha], ABC):
    pass