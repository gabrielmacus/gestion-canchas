from src.Administracion.Reservas.Domain.Exceptions.CanchaReservadaException import CanchaReservadaException
from src.Administracion.Reservas.Application.UseCases.EditarReservaUseCase import EditarReservaUseCase
from src.Administracion.Reservas.Application.DTOs.EditarReservaDTO import EditarReservaDTO
from src.Administracion.Reservas.Domain.Services.ReservaFinder import ReservaFinder
from src.Administracion.Reservas.Domain.Services.BookingService import BookingService
from src.SharedKernel.Infraestructure.Services.SAConnection import SAConnection
from src.Administracion.Reservas.Infraestructure.Services.SAReservaRepository import SAReservaRepository
from src.SharedKernel.Infraestructure.Services.TimeProvider import TimeProvider
from src.Administracion.Reservas.Domain.Exceptions.InvalidFechaHoraException import InvalidFechaHoraException
from fastapi import HTTPException, Response
from apps.API.DTOs.ErrorResponseDTO import ErrorResponseDTO
from apps.API.DTOs.CanchaReservadaErrorResponseDTO import CanchaReservadaErrorResponseDTO

class ReservaUpdateHandler():
    def __init__(self):
        self._repository = SAReservaRepository(SAConnection().get_engine())
        self._time_provider = TimeProvider()
        self._booking_service = BookingService(self._time_provider, self._repository)
        self._reserva_finder = ReservaFinder(self._repository)
        self._editar_reserva_usecase = EditarReservaUseCase(
            self._repository,
            self._booking_service,
            self._reserva_finder,
            self._time_provider
        )
    
    def update(self, id: str, request: EditarReservaDTO, response: Response):
        try:
            self._editar_reserva_usecase.execute(id, request) 
        except CanchaReservadaException as e:
            response.status_code = 400
            return CanchaReservadaErrorResponseDTO(
                    detail=str(e), 
                    cancha_colision_id=e.cancha_id
            )
        except InvalidFechaHoraException as e:
            raise HTTPException(status_code=400, detail=ErrorResponseDTO(detail=str(e)))