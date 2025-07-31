from apps.API.DTOs.CanchaDTO import CanchaDTO
from src.SharedKernel.Infraestructure.DTOs.PagedResponseDTO import PagedResponseDTO
from src.SharedKernel.Domain.Pagination.PagedResult import PagedResult
from src.Administracion.Canchas.Domain.Entities.Cancha import Cancha

class CanchaMappings:
    
    @staticmethod
    def to_paged_response_dto(result: PagedResult[Cancha]) -> PagedResponseDTO:
        return PagedResponseDTO(
            items=[CanchaMappings.to_dto(item) for item in result.items],
            total=result.total.value,
            page_size=result.page_size.value,
            page_number=result.page_number.value
        )
    
    @staticmethod
    def to_dto(cancha: Cancha) -> CanchaDTO:
        return CanchaDTO(
            id=cancha.id.value,
            nombre=cancha.nombre.value,
            techada=cancha.techada.value
        ) 