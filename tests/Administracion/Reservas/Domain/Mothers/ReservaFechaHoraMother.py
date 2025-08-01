from datetime import datetime, timedelta

class ReservaFechaHoraMother:
    @staticmethod
    def create(value: datetime | None = None) -> datetime:
        if value is None:
            value = datetime.now()
            value = (value  + timedelta(days=1))
            value = value.replace(hour=0, minute=0, second=0, microsecond=0)
        return value
    
    
    