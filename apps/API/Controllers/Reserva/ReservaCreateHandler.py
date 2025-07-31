from src.Administracion.Reservas.Application.DTOs.ReservarCanchaDTO import ReservarCanchaDTO
from src.Administracion.Reservas.Application.UseCases.ReservarCanchaUseCase import ReservarCanchaUseCase
from src.Administracion.Reservas.Domain.Services.BookingService import BookingService
from src.SharedKernel.Infraestructure.Services.SAConnection import SAConnection
from src.Administracion.Reservas.Infraestructure.Services.SAReservaRepository import SAReservaRepository
from src.SharedKernel.Infraestructure.Services.TimeProvider import TimeProvider
from src.Administracion.Reservas.Domain.Exceptions.InvalidFechaHoraException import InvalidFechaHoraException
from fastapi import HTTPException, Response
from src.Administracion.Reservas.Domain.Exceptions.CanchaReservadaException import CanchaReservadaException
from apps.API.DTOs.ErrorResponseDTO import ErrorResponseDTO
from apps.API.DTOs.CanchaReservadaErrorResponseDTO import CanchaReservadaErrorResponseDTO

class ReservaCreateHandler():
    def __init__(self):
        self._repository = SAReservaRepository(SAConnection().get_engine())
        self._time_provider = TimeProvider()
        self._booking_service = BookingService(self._time_provider, self._repository)
        self._reservar_cancha_usecase = ReservarCanchaUseCase(self._booking_service)
    
    def create(self, request: ReservarCanchaDTO, response: Response):
        try:
            self._reservar_cancha_usecase.execute(request) 
        except CanchaReservadaException as e:
            response.status_code = 400
            return CanchaReservadaErrorResponseDTO(
                detail=str(e), 
                cancha_colision_id=e.cancha_id
            )
        except InvalidFechaHoraException as e:
            raise HTTPException(status_code=400, detail=ErrorResponseDTO(detail=str(e)))