from faker import Faker

class JugadorApellidoMother:
    @staticmethod
    def create(apellido:str | None = None):
        return apellido or Faker().last_name()