from datetime import datetime, timedelta
from src.SharedKernel.Domain.Entities.AggregateRoot import AggregateRoot
from src.Administracion.Reservas.Domain.ValueObjects.ReservaFechaHora import ReservaFechaHora
from src.Administracion.Reservas.Domain.ValueObjects.ReservaDuracionMinutos import ReservaDuracionMinutos
from src.Administracion.Reservas.Domain.ValueObjects.ReservaCanchaId import ReservaCanchaId
from src.Administracion.Reservas.Domain.ValueObjects.ReservaId import ReservaId
from dataclasses import dataclass
from src.Administracion.Reservas.Domain.ValueObjects.ReservaJugadorId import ReservaJugadorId

@dataclass
class Reserva(AggregateRoot):
    _id: ReservaId
    _fecha_hora: ReservaFechaHora
    _duracion: ReservaDuracionMinutos
    _cancha_id: ReservaCanchaId
    _jugador_id: ReservaJugadorId # TODO: aca la IA habia importado un modulo (JugadorId) de otro dominio, violando DDD
    
    def __init__(self, id: str, fecha_hora:datetime, duracion:int, cancha_id:str, jugador_id:str, now:datetime):
        self._id = ReservaId(id)
        self._fecha_hora = ReservaFechaHora(fecha_hora, now)
        self._duracion = ReservaDuracionMinutos(duracion)
        self._cancha_id = ReservaCanchaId(cancha_id)
        self._jugador_id = ReservaJugadorId(jugador_id)
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
    
    @staticmethod
    def create(id: str, fecha_hora:datetime, duracion:int, cancha_id:str, jugador_id:str, now:datetime):
        # TODO: Domain event
        return Reserva(id, fecha_hora, duracion, cancha_id, jugador_id, now)
    
    def calculate_fecha_hora_fin(self) -> datetime:
        return self._fecha_hora.value + timedelta(minutes=self._duracion.value)