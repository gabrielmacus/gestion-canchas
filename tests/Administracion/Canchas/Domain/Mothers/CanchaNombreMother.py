from faker import Faker

class CanchaNombreMother:
    @staticmethod
    def create(nombre: str | None = None) -> str:
        return nombre or Faker().country()