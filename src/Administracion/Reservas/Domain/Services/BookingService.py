from typing import final
from datetime import datetime, timedelta
from src.SharedKernel.Domain.Contracts.TimeProviderInterface import TimeProviderInterface
from src.Administracion.Reservas.Domain.Contracts.ReservaRepository import ReservaRepositoryInterface
from src.Administracion.Reservas.Domain.Exceptions.CanchaReservadaException import CanchaReservadaException
from src.Administracion.Reservas.Domain.Entities.Reserva import Reserva
from src.Administracion.Reservas.Domain.Queries.ReservasActivasQuery import ReservasActivasQuery

@final
class BookingService:
    def __init__(
        self,
        time_provider: TimeProviderInterface,
        reserva_repository: ReservaRepositoryInterface
    ):
        self._time_provider = time_provider
        self._reserva_repository = reserva_repository
    
    def book(self, id: str, fecha_hora:datetime, duracion:int, cancha_id:str):
        self._ensure_reserva_is_not_colliding(fecha_hora, duracion, cancha_id)
        reserva = Reserva.create(id, fecha_hora, duracion, cancha_id, self._time_provider.now_utc())
        self._reserva_repository.add(reserva)
        return reserva
        
    def _ensure_reserva_is_not_colliding(
        self, fecha_hora_inicio:datetime, duracion:int, cancha_id:str):
        """Verifica si la reserva colisiona con otras reservas activas.

        Args:
            fecha_hora (datetime): Fecha y hora de la reserva.
            duracion (int): Duración de la reserva.
            cancha_id (str): Id de la cancha.
        Raises:
            CanchaReservadaException: Si la reserva colisiona con otra reserva activa.
        """
        fecha_hora_fin = fecha_hora_inicio + timedelta(minutes=duracion)
        reservas_activas = self._reserva_repository.matching(
            ReservasActivasQuery.create(cancha_id, self._time_provider)
        )
        for reserva in reservas_activas:
            if fecha_hora_inicio >= reserva.fecha_hora.value and fecha_hora_inicio < reserva.calculate_fecha_hora_fin():
                raise CanchaReservadaException(cancha_id, fecha_hora_inicio)
            
            if fecha_hora_fin > reserva.fecha_hora.value and fecha_hora_fin <= reserva.calculate_fecha_hora_fin():
                 raise CanchaReservadaException(cancha_id, fecha_hora_inicio)