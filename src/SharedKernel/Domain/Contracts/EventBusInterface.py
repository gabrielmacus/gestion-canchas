from abc import ABC, abstractmethod
from src.SharedKernel.Domain.Events.DomainEvent import DomainEvent

class EventBusInterface(ABC):
    @abstractmethod
    def publish(self, events: list[DomainEvent]) -> None:
        pass