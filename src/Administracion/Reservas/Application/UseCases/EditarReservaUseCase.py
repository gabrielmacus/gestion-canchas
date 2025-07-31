from src.Administracion.Reservas.Application.DTOs.EditarReservaDTO import EditarReservaDTO
from src.Administracion.Reservas.Domain.Contracts.ReservaRepository import ReservaRepositoryInterface
from src.Administracion.Reservas.Domain.Entities.Reserva import Reserva
from src.Administracion.Reservas.Domain.Services.BookingService import BookingService
from src.Administracion.Reservas.Domain.Services.ReservaFinder import ReservaFinder
from src.SharedKernel.Domain.Contracts.TimeProviderInterface import TimeProviderInterface

class EditarReservaUseCase:
    def __init__(self, reserva_repository: ReservaRepositoryInterface, booking_service: BookingService, reserva_finder: ReservaFinder, time_provider: TimeProviderInterface):
        self._reserva_repository = reserva_repository
        self._booking_service = booking_service
        self._reserva_finder = reserva_finder
        self._time_provider = time_provider

    def execute(self, id: str, request: EditarReservaDTO) -> Reserva:
        reserva = self._reserva_finder.find_by_id(id)
        updated_reserva = self._update_reserva(reserva, request)
        self._booking_service.ensure_reserva_is_not_colliding(
            updated_reserva.fecha_hora.value,
            updated_reserva.duracion.value,
            updated_reserva.cancha_id.value,
            id
        )
        self._reserva_repository.update_by_id(id, updated_reserva)
        return updated_reserva
    
    def _update_reserva(self, reserva: Reserva, request: EditarReservaDTO) -> Reserva:
        """Crea una nueva instancia de Reserva con los valores actualizados, respetando inmutabilidad"""
        dump = request.model_dump(exclude_unset=True)
        return Reserva(
            id=reserva.id.value,
            fecha_hora=reserva.fecha_hora.value if 'fecha_hora' not in dump else dump['fecha_hora'],
            duracion=reserva.duracion.value if 'duracion' not in dump else dump['duracion'],
            cancha_id=reserva.cancha_id.value if 'cancha_id' not in dump else dump['cancha_id'],
            jugador_id=reserva.jugador_id.value if 'jugador_id' not in dump else dump['jugador_id'],
            now=self._time_provider.now_utc()
        )
        
        

