from dataclasses import dataclass
from src.SharedKernel.Domain.Criteria.Filter.Filters import Filters
from src.SharedKernel.Domain.Criteria.Order.Orders import Orders
from src.SharedKernel.Domain.Criteria.Fields.Fields import Fields
from src.SharedKernel.Domain.Criteria.Pagination import Pagination

@dataclass(frozen=True)
class Criteria:
    filters: Filters
    orders: Orders
    pagination: Pagination | None = None
    fields: Fields = Fields([])
    