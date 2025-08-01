from abc import ABC, abstractmethod
from typing import Generic, TypeVar
from src.SharedKernel.Domain.Pagination.PagedResult import PagedResult
from apps.API.Services.QueryParser import QueryParser
from apps.API.Mappings.QueryMappings import QueryMappings
from src.SharedKernel.Domain.Criteria.Criteria import Criteria

T = TypeVar('T')
R = TypeVar('R')

class BaseFindRequestHandler(ABC, Generic[T, R]):
    def find(self, page: int, size: int, orders: str = "", fields: str = "", q: str  = ""):
        query = QueryParser().parse(page, size, orders, fields, q)
        criteria = QueryMappings.to_criteria(query)
        result = self._paginate(criteria)
        return self._map_to_response(result)
    
    @abstractmethod
    def _paginate(self, criteria: Criteria) -> PagedResult[T]:
        pass

    @abstractmethod
    def _map_to_response(self, result: PagedResult[T]) -> R:
        pass