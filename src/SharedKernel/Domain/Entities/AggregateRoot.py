from src.SharedKernel.Domain.Events.DomainEvent import DomainEvent

class AggregateRoot:
    domain_events: list[DomainEvent] = []
    
    def pull_domain_events(self) -> list[DomainEvent]:
        events = self.domain_events
        self.domain_events.clear()
        return events
    
    def record_domain_event(self, domain_event: DomainEvent) -> None:
        self.domain_events.append(domain_event)
        
        