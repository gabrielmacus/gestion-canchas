from apps.API.DTOs.Query.QueryDTO import QueryDTO
from src.SharedKernel.Domain.Criteria.Criteria import Criteria
from src.SharedKernel.Domain.Criteria.Filter.Filter import Filter
from src.SharedKernel.Domain.Criteria.Order.Order import Order
from src.SharedKernel.Domain.Criteria.Fields.Fields import Fields,Field
from src.SharedKernel.Domain.Criteria.Filter.Filters import Filters
from src.SharedKernel.Domain.Criteria.Order.Orders import Orders
from src.SharedKernel.Domain.Criteria.Filter.FilterField import FilterField
from src.SharedKernel.Domain.Criteria.Filter.FilterOperator import FilterOperator
from src.SharedKernel.Domain.Criteria.Filter.FilterValue import FilterValue
from src.SharedKernel.Domain.Criteria.Order.OrderBy import OrderBy
from src.SharedKernel.Domain.Criteria.Order.OrderType import OrderType
from apps.API.DTOs.Query.FilterDTO import FilterDTO
from apps.API.DTOs.Query.OrderDTO import OrderDTO
from src.SharedKernel.Domain.Criteria.Pagination import Pagination
from apps.API.DTOs.Query.PaginationDTO import PaginationDTO

class QueryMappings:
    @staticmethod
    def to_criteria(query: QueryDTO | None) -> Criteria:
        if query is None:
            return Criteria(
                fields=Fields([]),
                filters=Filters([]),
                orders=Orders([])
            )
        return Criteria(
            pagination=QueryMappings.map_pagination(query.p),
            fields=QueryMappings.map_fields(query.fields),
            filters=QueryMappings.map_filters(query.filters),
            orders=QueryMappings.map_orders(query.orders)
        )
        
    @staticmethod
    def map_pagination(pagination: PaginationDTO | None) -> Pagination:
        if pagination is None:
            # TODO: default values from environment variables
            return Pagination(size=10, page=0)
        return Pagination(size=pagination.size, page=pagination.number)
    
    @staticmethod
    def map_orders(orders: list[OrderDTO]) -> Orders:
        return Orders([Order(OrderBy(order.field), OrderType(order.direction)) for order in orders])
    
    @staticmethod
    def map_fields(fields: list[str]) -> Fields:
        return Fields([Field(field) for field in fields])
    
    @staticmethod
    def map_filters(filters: list[FilterDTO]) -> Filters:
        return Filters([
            Filter(FilterField(filter.field), 
                   FilterOperator(filter.operator), 
                   FilterValue(filter.value)) for filter in filters])