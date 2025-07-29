from dataclasses import dataclass

@dataclass
class CrearJugadorDTO:
    id: str
    nombre: str
    apellido: str
    email: str
    telefono: str