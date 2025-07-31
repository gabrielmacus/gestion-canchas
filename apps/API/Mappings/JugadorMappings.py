from apps.API.DTOs.JugadorDTO import JugadorDTO
from src.SharedKernel.Infraestructure.DTOs.PagedResponseDTO import PagedResponseDTO
from src.SharedKernel.Domain.Pagination.PagedResult import PagedResult
from src.Administracion.Jugadores.Domain.Entities.Jugador import Jugador

class JugadorMappings:
    
    @staticmethod
    def to_paged_response_dto(result: PagedResult[Jugador]) -> PagedResponseDTO:
        return PagedResponseDTO(
            items=[JugadorMappings.to_dto(item) for item in result.items],
            total=result.total.value,
            page_size=result.page_size.value,
            page_number=result.page_number.value
        )
    @staticmethod
    def to_dto(jugador: Jugador) -> JugadorDTO:
        return JugadorDTO(
            id=jugador.id.value,
            nombre=jugador.nombre.value,
            apellido=jugador.apellido.value,
            telefono=jugador.telefono.value,
            email=jugador.email.value
        )