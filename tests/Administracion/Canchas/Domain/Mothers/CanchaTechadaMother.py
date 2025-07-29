import random

class CanchaTechadaMother:
    @staticmethod
    def create(techada: bool | None = None) -> bool:
        if techada is None:
            return random.choice([True, False])
        return techada 