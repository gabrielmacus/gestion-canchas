from apps.API.Controllers.BaseFindRequestHandler import BaseFindRequestHandler
from src.Administracion.Reservas.Application.UseCases.PaginarReservasUseCase import PaginarReservasUseCase
from src.SharedKernel.Domain.Criteria.Criteria import Criteria
from src.SharedKernel.Domain.Pagination.PagedResult import PagedResult
from src.Administracion.Reservas.Domain.Entities.Reserva import Reserva
from apps.API.DTOs.ReservaDTO import ReservaDTO
from src.SharedKernel.Infraestructure.Services.SAConnection import SAConnection
from src.SharedKernel.Domain.Services.PaginationService import PaginationService
from src.Administracion.Reservas.Infraestructure.Services.SAReservaRepository import SAReservaRepository
from apps.API.Mappings.ReservaMappings import ReservaMappings

class ReservaFindHandler(BaseFindRequestHandler):
    def __init__(self):
        self._repository = SAReservaRepository(SAConnection().get_engine())
        self._paginar_reservas_usecase = PaginarReservasUseCase(
            PaginationService(self._repository, self._repository)
        )

    def _paginate(self, criteria: Criteria):
        return self._paginar_reservas_usecase.execute(criteria)
    
    def _map_to_response(self, result: PagedResult[Reserva]):
        return ReservaMappings.to_paged_response_dto(result) 