import json
from typing_extensions import Optional
from pydantic import BaseModel
from apps.API.DTOs.Query.FilterDTO import FilterDTO
from apps.API.DTOs.Query.OrderDTO import OrderDTO
from apps.API.DTOs.Query.PaginationDTO import PaginationDTO
from src.SharedKernel.Domain.Criteria.Filter.FilterOperator import FilterOperators
from src.SharedKernel.Domain.Criteria.Order.OrderType import OrderTypes


class QueryDTO(BaseModel):
    fields: list[str] = []
    filters: list[FilterDTO] = []
    orders: list[OrderDTO] = []
    p: Optional[PaginationDTO] = None
