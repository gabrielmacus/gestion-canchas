from datetime import datetime
from src.SharedKernel.Domain.Contracts.TimeProviderInterface import TimeProviderInterface

class TimeProvider(TimeProviderInterface):
    def now_utc(self) -> datetime:
        return datetime.utcnow()
    
    def now_local(self) -> datetime:
        return datetime.now() 