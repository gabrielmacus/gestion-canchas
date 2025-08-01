from dataclasses import dataclass
from src.SharedKernel.Domain.Entities.AggregateRoot import AggregateRoot
from src.Identidad.Usuarios.Domain.ValueObjects.UsuarioId import UsuarioId
from src.Identidad.Usuarios.Domain.ValueObjects.UsuarioNombre import UsuarioNombre
from src.Identidad.Usuarios.Domain.ValueObjects.UsuarioEmail import UsuarioEmail
from src.Identidad.Usuarios.Domain.ValueObjects.UsuarioPassword import UsuarioPassword

@dataclass
class Usuario(AggregateRoot):
    def __init__(self, id: str, nombre: str, email: str, password: str):
        self.id = UsuarioId(id)
        self.nombre = UsuarioNombre(nombre)
        self.email = UsuarioEmail(email)
        self.password = UsuarioPassword(password)

