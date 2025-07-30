import uuid

class IdMother:
    @staticmethod
    def create(id: str | None = None) -> str:
        if id is None:
            id = str(uuid.uuid4())
        return id
