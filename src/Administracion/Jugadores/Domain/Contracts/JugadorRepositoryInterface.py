from abc import ABC
from src.Administracion.Jugadores.Domain.Entities.Jugador import Jugador
from src.SharedKernel.Domain.Contracts.Repository.RepositoryInterface import RepositoryInterface

class JugadorRepositoryInterface(RepositoryInterface[Jugador], ABC):
    pass