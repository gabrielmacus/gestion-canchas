from dataclasses import dataclass

@dataclass
class JugadorDTO:
    id: str
    nombre: str
    apellido: str
    telefono: str
    email: str | None