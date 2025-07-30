from abc import ABC, abstractmethod
from typing import Generic, TypeVar
from src.SharedKernel.Domain.Contracts.Repository.CreatorInterface import CreatorInterface
from src.SharedKernel.Domain.Contracts.Repository.UpdaterInterface import UpdaterInterface
from src.SharedKernel.Domain.Contracts.Repository.DeleterInterface import DeleterInterface
from src.SharedKernel.Domain.Contracts.Repository.ReaderInterface import ReaderInterface
from src.SharedKernel.Domain.Contracts.Repository.CounterInterface import CounterInterface

T = TypeVar('T')

class RepositoryInterface(
    CreatorInterface[T], 
    UpdaterInterface[T], 
    DeleterInterface[T], 
    ReaderInterface[T], 
    CounterInterface[T], 
    ABC):
    pass