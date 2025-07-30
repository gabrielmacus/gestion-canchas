from src.SharedKernel.Domain.Criteria.Criteria import Criteria
from src.Administracion.Jugadores.Domain.Contracts.JugadorRepositoryInterface import JugadorRepositoryInterface
from src.SharedKernel.Domain.Criteria.Filter.Filters import Filters
from src.SharedKernel.Domain.Criteria.Order.Orders import Orders
from src.SharedKernel.Domain.Criteria.Pagination.PageNumber import PageNumber
from src.SharedKernel.Domain.Criteria.Pagination.PageSize import PageSize
from src.SharedKernel.Domain.Criteria.Fields.Fields import Fields
from src.SharedKernel.Domain.Pagination.PagedResult import PagedResult
from src.SharedKernel.Domain.Services.PaginationService import PaginationService

class PaginarJugadoresUseCase:
    
    def __init__(self, pagination_service: PaginationService):
        self._pagination_service = pagination_service
    
    def execute(self, criteria: Criteria):
        return self._pagination_service.paginate(criteria)