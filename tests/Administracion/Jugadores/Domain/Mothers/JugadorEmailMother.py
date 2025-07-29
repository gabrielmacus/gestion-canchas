from faker import Faker

class JugadorEmailMother:
    @staticmethod
    def create(email:str | None = None):
        return email or Faker().email()