from datetime import datetime, timedelta
from src.SharedKernel.Domain.Entities.AggregateRoot import AggregateRoot
from src.Administracion.Reservas.Domain.ValueObjects.ReservaFechaHora import ReservaFechaHora
from src.Administracion.Reservas.Domain.ValueObjects.ReservaDuracionMinutos import ReservaDuracionMinutos
from src.Administracion.Reservas.Domain.ValueObjects.ReservaCanchaId import ReservaCanchaId
from src.Administracion.Reservas.Domain.ValueObjects.ReservaId import ReservaId
from dataclasses import dataclass
from src.Administracion.Reservas.Domain.ValueObjects.ReservaJugadorId import ReservaJugadorId
from src.Administracion.Reservas.Domain.ValueObjects.ReservaCanchaNombre import ReservaCanchaNombre
from src.Administracion.Reservas.Domain.ValueObjects.ReservaJugadorNombre import ReservaJugadorNombre

@dataclass
class Reserva(AggregateRoot):
    _id: ReservaId
    _fecha_hora: ReservaFechaHora
    _duracion: ReservaDuracionMinutos
    _cancha_id: ReservaCanchaId
    _jugador_id: ReservaJugadorId # TODO: aca la IA habia importado un modulo (JugadorId) de otro dominio, violando DDD
    _cancha_nombre: ReservaCanchaNombre | None
    _jugador_nombre: ReservaJugadorNombre | None
    
    
    
    def __init__(self, id: str, fecha_hora:datetime, duracion:int, cancha_id:str, jugador_id:str, now:datetime, cancha_nombre:str | None = None, jugador_nombre:str | None = None):
        self._id = ReservaId(id)
        self._fecha_hora = ReservaFechaHora(fecha_hora, now)
        self._duracion = ReservaDuracionMinutos(duracion)
        self._cancha_id = ReservaCanchaId(cancha_id)
        self._jugador_id = ReservaJugadorId(jugador_id)
        self._cancha_nombre = ReservaCanchaNombre(cancha_nombre) if cancha_nombre else None
        self._jugador_nombre = ReservaJugadorNombre(jugador_nombre) if jugador_nombre else None
        super().__init__()
    
    @property
    def id(self):
        return self._id
    
    @property
    def fecha_hora(self):
        return self._fecha_hora
    
    @property
    def duracion(self):
        return self._duracion
    
    @property
    def cancha_id(self):
        return self._cancha_id
    
    @property
    def jugador_id(self):
        return self._jugador_id
    
    @property
    def cancha_nombre(self):
        return self._cancha_nombre
    
    @property
    def jugador_nombre(self):
        return self._jugador_nombre
    
    @staticmethod
    def create(id: str, fecha_hora:datetime, duracion:int, cancha_id:str, jugador_id:str, now:datetime):
        # TODO: Domain event
        return Reserva(id, fecha_hora, duracion, cancha_id, jugador_id, now, cancha_nombre=None, jugador_nombre=None    )
    
    def calculate_fecha_hora_fin(self) -> datetime:
        return self._fecha_hora.value + timedelta(minutes=self._duracion.value)