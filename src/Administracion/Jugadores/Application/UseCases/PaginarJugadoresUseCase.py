from src.SharedKernel.Domain.Criteria.Criteria import Criteria
from src.Administracion.Jugadores.Domain.Contracts.JugadorRepositoryInterface import JugadorRepositoryInterface
from src.SharedKernel.Domain.Criteria.Filter.Filters import Filters
from src.SharedKernel.Domain.Criteria.Order.Orders import Orders
from src.SharedKernel.Domain.Criteria.Pagination.PageNumber import PageNumber
from src.SharedKernel.Domain.Criteria.Pagination.PageSize import PageSize
from src.SharedKernel.Domain.Criteria.Fields.Fields import Fields
from src.SharedKernel.Domain.Pagination.PagedResult import PagedResult
from src.SharedKernel.Domain.Pagination.PagedPageSize import PagedPageSize
from src.SharedKernel.Domain.Pagination.PagedPageNumber import PagedPageNumber

class PaginarJugadoresUseCase:
    _repository: JugadorRepositoryInterface
    
    def __init__(self, repository: JugadorRepositoryInterface):
        self._repository = repository
    
    def execute(self):
        criteria = Criteria(
            filters=Filters([]),
            orders=Orders([]),
            page_size=PageSize(10),
            page_number=PageNumber(1),
            fields=Fields([])
        )
        results = self._repository.matching(criteria)
        count = self._repository.count_matching(criteria)
        return PagedResult.from_result(results, count, PagedPageSize(10), PagedPageNumber(1))