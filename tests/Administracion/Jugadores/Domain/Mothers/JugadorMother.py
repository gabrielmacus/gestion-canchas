from src.Administracion.Jugadores.Domain.Entities.Jugador import Jugador
from tests.SharedKernel.Domain.Mothers.IdMother import IdMother
from tests.Administracion.Jugadores.Domain.Mothers.JugadorNombreMother import JugadorNombreMother
from tests.Administracion.Jugadores.Domain.Mothers.JugadorApellidoMother import JugadorApellidoMother
from tests.Administracion.Jugadores.Domain.Mothers.JugadorEmailMother import JugadorEmailMother
from tests.Administracion.Jugadores.Domain.Mothers.JugadorTelefonoMother import JugadorTelefonoMother

class JugadorMother:
    @staticmethod
    def create(id:str | None = None, 
               nombre:str | None = None, 
               apellido:str | None = None, 
               email:str | None = None, 
               telefono:str | None = None):
        return Jugador(
            id=id or IdMother.create(),
            nombre=nombre or JugadorNombreMother.create(),
            apellido=apellido or JugadorApellidoMother.create(),
            email=email or JugadorEmailMother.create(),
            telefono=telefono or JugadorTelefonoMother.create())