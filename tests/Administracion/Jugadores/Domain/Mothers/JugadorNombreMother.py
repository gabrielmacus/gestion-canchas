from faker import Faker

class JugadorNombreMother:
    @staticmethod
    def create(nombre:str | None = None):
        return nombre or Faker().first_name()