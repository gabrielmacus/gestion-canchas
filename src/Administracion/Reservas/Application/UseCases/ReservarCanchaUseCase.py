from src.Administracion.Reservas.Domain.Services.BookingService import BookingService
from src.Administracion.Reservas.Application.DTOs.ReservarCanchaDTO import ReservarCanchaDTO
from src.Administracion.Reservas.Domain.Entities.Reserva import Reserva

class ReservarCanchaUseCase:
    def __init__(self, booking_service: BookingService):
        self.__booking_service = booking_service

    def execute(self, request: ReservarCanchaDTO) -> Reserva:
        return self.__booking_service.book(
            id=request.id,
            fecha_hora=request.fecha_hora,
            duracion=request.duracion,
            cancha_id=request.cancha_id,
            jugador_id=request.jugador_id
        )
        # TODO: Domain Events