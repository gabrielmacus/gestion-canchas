import pytest
from src.Administracion.Reservas.Application.UseCases.ReservarCanchaUseCase import ReservarCanchaUseCase
from src.Administracion.Reservas.Application.DTOs.ReservarCanchaDTO import ReservarCanchaDTO
from src.Administracion.Reservas.Domain.Services.BookingService import BookingService
from unittest.mock import Mock
from tests.SharedKernel.Domain.Mothers.IdMother import IdMother
from tests.Administracion.Reservas.Domain.Mothers.ReservaDuracionMinutosMother import ReservaDuracionMinutosMother
from tests.Administracion.Reservas.Domain.Mothers.ReservaFechaHoraMother import ReservaFechaHoraMother

class TestCrearReservaUseCase:
    __reservar_cancha_use_case: ReservarCanchaUseCase | None = None
    __booking_service: Mock | None = None

    @pytest.fixture(autouse=True)
    def setup(self):
        self.__booking_service = Mock(spec=BookingService)
        self.__reservar_cancha_use_case = ReservarCanchaUseCase(self.__booking_service) # pyright: ignore[reportAny]

    def __then_cancha_is_booked(self, request: ReservarCanchaDTO):
        assert self.__booking_service is not None
        self.__booking_service.book.assert_called_once_with( # pyright: ignore[reportAny]
            id=request.id_reserva,
            fecha_hora=request.fecha_hora,
            duracion=request.duracion,
            cancha_id=request.cancha_id
        )

    def test_crear_reserva(self):
        # Given
        request = ReservarCanchaDTO(
            id_reserva= IdMother.create(),
            fecha_hora=ReservaFechaHoraMother.create(),
            duracion=ReservaDuracionMinutosMother.create(),
            cancha_id= IdMother.create()
        )
        
        # When
        assert self.__reservar_cancha_use_case is not None
        _ = self.__reservar_cancha_use_case.execute(request)

        # Then
        self.__then_cancha_is_booked(request)