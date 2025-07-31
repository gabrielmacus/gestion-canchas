from abc import ABC
from src.Administracion.Reservas.Domain.Entities.Reserva import Reserva
from src.SharedKernel.Domain.Contracts.Repository.RepositoryInterface import RepositoryInterface

class ReservaRepositoryInterface(RepositoryInterface[Reserva], ABC):
    pass