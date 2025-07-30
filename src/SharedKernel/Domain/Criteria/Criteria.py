from dataclasses import dataclass
from src.SharedKernel.Domain.Criteria.Filter.Filters import Filters
from src.SharedKernel.Domain.Criteria.Order.Orders import Orders
from src.SharedKernel.Domain.Criteria.Pagination.PageSize import PageSize
from src.SharedKernel.Domain.Criteria.Pagination.PageNumber import PageNumber
from src.SharedKernel.Domain.Criteria.Fields.Fields import Fields
@dataclass(frozen=True)
class Criteria:
    filters: Filters
    orders: Orders
    page_size: PageSize
    page_number: PageNumber
    fields: Fields
    # TODO: default values for page size and page number?
    def __post_init__(self): 
        self._ensure_page_size_and_page_number_are_consistent()
            
    def _ensure_page_size_and_page_number_are_consistent(self):
        if self.page_number.value is not None and self.page_size.value is None:
            raise ValueError("Page size must be provided if page number is provided")
        if self.page_number.value is None and self.page_size.value is not None:
            raise ValueError("Page number must be provided if page size is provided")