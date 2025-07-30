
import random

class ReservaDuracionMinutosMother:
    @staticmethod
    def create(value: int  | None = None) -> int:
        if value is None:
            value = random.randint(60, 240)
            if value % 60 != 0:
                value = value - (value % 60)
        return value
    
    @staticmethod
    def create_invalid() -> int:
        value = random.randint(1,2000)
        if value % 60 == 0:
            value = value + 1
        return value