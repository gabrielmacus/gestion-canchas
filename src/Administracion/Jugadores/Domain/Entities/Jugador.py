from src.SharedKernel.Domain.Entities.AggregateRoot import AggregateRoot
from src.Administracion.Jugadores.Domain.ValueObjects.JugadorId import JugadorId
from src.Administracion.Jugadores.Domain.ValueObjects.JugadorNombre import JugadorNombre
from src.Administracion.Jugadores.Domain.ValueObjects.JugadorApellido import JugadorApellido
from src.Administracion.Jugadores.Domain.ValueObjects.JugadorTelefono import JugadorTelefono
from src.Administracion.Jugadores.Domain.ValueObjects.JugadorEmail import JugadorEmail

class Jugador(AggregateRoot):
    _id: JugadorId
    _nombre: JugadorNombre
    _apellido: JugadorApellido
    _telefono: JugadorTelefono
    _email: JugadorEmail
    
    def __init__(self, id:str, nombre:str, apellido:str, telefono:str, email:str | None = None):
        self._id = JugadorId(id)
        self._nombre = JugadorNombre(nombre)
        self._apellido = JugadorApellido(apellido)
        self._telefono = JugadorTelefono(telefono)
        self._email = JugadorEmail(email)
        
        super().__init__()
    
    @property
    def id(self):
        return self._id
    
    @property
    def nombre(self):
        return self._nombre
    
    @property
    def apellido(self):
        return self._apellido
    
    @property
    def telefono(self):
        return self._telefono
    
    @property
    def email(self):
        return self._email
    
    @staticmethod
    def create(id:str, nombre:str, apellido:str, telefono:str, email:str | None = None):
        # TODO: Domain event
        return Jugador(id, nombre, apellido, telefono, email)
    
    
    def set_apellido(self, apellido:str):
        self._apellido = JugadorApellido(apellido)
    