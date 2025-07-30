class JugadorNotFound(Exception):
    def __init__(self, id: str):
        self.id = id
        super().__init__(f"Jugador con id {id} no encontrado")