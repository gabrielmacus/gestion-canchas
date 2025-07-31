from typing import Generic, TypeVar
from src.SharedKernel.Domain.Criteria.Criteria import Criteria
from src.SharedKernel.Domain.Pagination.PagedResult import PagedResult
from src.SharedKernel.Domain.Contracts.Repository.ReaderInterface import ReaderInterface
from src.SharedKernel.Domain.Contracts.Repository.CounterInterface import CounterInterface

T = TypeVar('T')

# TODO: logging
class PaginationService(Generic[T]):
    def __init__(self, 
                 reader: ReaderInterface[T], 
                 counter: CounterInterface[T]
    ):
        self.__reader = reader
        self.__counter = counter
    
    def paginate(self, criteria: Criteria) -> PagedResult[T]:
        self._ensure_pagination_is_set(criteria)
        
        result = self.__reader.matching(criteria)
        total = self.__counter.count_matching(criteria)
        
        assert criteria.pagination is not None
        
        return PagedResult.from_result(
            result, 
            total, 
            criteria.pagination.size, 
            criteria.pagination.page
        )
        
    def _ensure_pagination_is_set(self, criteria: Criteria) -> None:
        if criteria.pagination is None:
            raise ValueError("La paginación debe tener un tamaño de página y un número de página")