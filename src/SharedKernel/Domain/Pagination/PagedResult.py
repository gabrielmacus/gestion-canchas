from dataclasses import dataclass
from typing import Generic, TypeVar
from src.SharedKernel.Domain.Pagination.PagedTotalCount import PagedTotalCount
from src.SharedKernel.Domain.Pagination.PagedPageSize import PagedPageSize
from src.SharedKernel.Domain.Pagination.PagedPageNumber import PagedPageNumber
        
T = TypeVar('T')

@dataclass(frozen=True)
class PagedResult(Generic[T]):
    """
    Clase que representa el resultado de una página.

    Args:
        items (list[T]): La lista de elementos de la página.
        total (int): El total de elementos.
        page_size (PagedPageSize): El tamaño de la página.
        page_number (PagedPageNumber): El número de página.
    """
    items: list[T]
    total: PagedTotalCount
    page_size: PagedPageSize
    page_number: PagedPageNumber
    
    @staticmethod
    def from_result(
        result: list[T], 
        count: int, 
        page_size: PagedPageSize, 
        page_number: PagedPageNumber
    ) -> 'PagedResult':
        return PagedResult(
            items=result,
            total=PagedTotalCount(count),
            page_size=page_size,
            page_number=page_number
        )
        
    def __str__(self) -> str:
        return f"PagedResult(items={self.items}, total={self.total}, page_size={self.page_size}, page_number={self.page_number})"
    
    def __repr__(self) -> str:
        return self.__str__()