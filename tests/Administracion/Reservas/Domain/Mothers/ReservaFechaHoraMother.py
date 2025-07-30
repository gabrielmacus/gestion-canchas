from datetime import datetime

class ReservaFechaHoraMother:
    @staticmethod
    def create(value: datetime | None = None) -> datetime:
        if value is None:
            value = datetime.now()
            value = value.replace(minute=0)
        return value
    
    