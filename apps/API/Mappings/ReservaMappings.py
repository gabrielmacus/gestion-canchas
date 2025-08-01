from apps.API.DTOs.ReservaDTO import ReservaDTO
from src.SharedKernel.Infraestructure.DTOs.PagedResponseDTO import PagedResponseDTO
from src.SharedKernel.Domain.Pagination.PagedResult import PagedResult
from src.Administracion.Reservas.Domain.Entities.Reserva import Reserva

class ReservaMappings:
    
    @staticmethod
    def to_paged_response_dto(result: PagedResult[Reserva]) -> PagedResponseDTO:
        return PagedResponseDTO(
            items=[ReservaMappings.to_dto(item) for item in result.items],
            total=result.total.value,
            page_size=result.page_size.value,
            page_number=result.page_number.value
        )
    
    @staticmethod
    def to_dto(reserva: Reserva) -> ReservaDTO:
        return ReservaDTO(
            id=reserva.id.value,
            fecha_hora=reserva.fecha_hora.value,
            duracion=reserva.duracion.value,
            cancha_id=reserva.cancha_id.value,
            jugador_id=reserva.jugador_id.value,
            cancha_nombre=reserva.cancha_nombre.value if reserva.cancha_nombre else None,
            jugador_nombre=reserva.jugador_nombre.value if reserva.jugador_nombre else None
        ) 