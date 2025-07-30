from src.SharedKernel.Domain.Criteria.Criteria import Criteria
from src.Administracion.Jugadores.Domain.Contracts.JugadorRepositoryInterface import JugadorRepositoryInterface
from src.SharedKernel.Domain.Criteria.Filter.Filters import Filters
from src.SharedKernel.Domain.Criteria.Order.Orders import Orders
from src.SharedKernel.Domain.Criteria.Pagination.PageNumber import PageNumber
from src.SharedKernel.Domain.Criteria.Pagination.PageSize import PageSize
from src.SharedKernel.Domain.Criteria.Fields.Fields import Fields


class ListarJugadoresUseCase:
    _repository: JugadorRepositoryInterface
    
    def __init__(self, repository: JugadorRepositoryInterface):
        self._repository = repository
    
    def execute(self):
        return self._repository.matching(Criteria(
            filters=Filters([]),
            orders=Orders([]),
            page_size=PageSize(10),
            page_number=PageNumber(1),
            fields=Fields([])
        ))