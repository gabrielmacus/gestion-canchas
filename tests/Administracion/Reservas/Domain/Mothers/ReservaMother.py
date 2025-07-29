from src.Administracion.Reservas.Domain.Entities.Reserva import Reserva
from tests.Administracion.Reservas.Domain.Mothers.ReservaDuracionMinutosMother import ReservaDuracionMinutosMother
from tests.Administracion.Reservas.Domain.Mothers.ReservaFechaHoraMother import ReservaFechaHoraMother
from tests.SharedKernel.Domain.Mothers.IdMother import IdMother
from datetime import datetime

class ReservaMother:
    @staticmethod
    def create(
        now: datetime,
        id: str | None = None, 
        fecha_hora: datetime | None = None, 
        duracion: int | None = None,
        cancha_id: str | None = None
    ) -> Reserva:
        return Reserva(
            id=IdMother.create(id),
            fecha_hora=ReservaFechaHoraMother.create(fecha_hora),
            duracion=ReservaDuracionMinutosMother.create(duracion),
            cancha_id=IdMother.create(cancha_id),
            now=now,
        )