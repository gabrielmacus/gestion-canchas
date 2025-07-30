from faker import Faker

class JugadorTelefonoMother:
    @staticmethod
    def create(telefono:str | None = None):
        return telefono or Faker().msisdn()