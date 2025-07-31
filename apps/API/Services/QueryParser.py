import json
from apps.API.DTOs.Query.OrderDTO import OrderDTO
from apps.API.DTOs.Query.FilterDTO import FilterDTO
from src.SharedKernel.Domain.Criteria.Order.OrderType import OrderTypes
from src.SharedKernel.Domain.Criteria.Filter.FilterOperator import FilterOperators
from apps.API.DTOs.Query.PaginationDTO import PaginationDTO
from apps.API.DTOs.Query.QueryDTO import QueryDTO

class QueryParser:
    """
    Servicio para parsear las consultas de la API
    """
    def _parse_orders(self, orders: str) -> list[OrderDTO]:
        orders_list = orders.split(",") if orders else []
        orders_list = [
            OrderDTO(field=order.split(":")[0], direction=OrderTypes(order.split(":")[1])) 
            for order in orders_list
        ]
        return orders_list
        
    def _parse_fields(self, fields: str) -> list[str]:
        return fields.split(",") if fields else []
        
    def _parse_filters(self, filters: str) -> list[FilterDTO]:
        try:
            filters_list = json.loads(filters)
        except Exception:
            filters_list = []
        filters_list = [
            FilterDTO(
                field=filter["field"], 
                operator=FilterOperators(filter["operator"]), 
                value=filter["value"])
            for filter in filters_list
        ]   
        return filters_list
        
    def parse(
        self,
        page: int, 
        size: int, 
        orders: str,
        fields_csv: str,
        query_json:str) -> "QueryDTO":
        
        orders_list = self._parse_orders(orders)
        fields_list = self._parse_fields(fields_csv)
        pagination = PaginationDTO(number=page, size=size)
        filters = self._parse_filters(query_json)
        
        return QueryDTO(
            fields=fields_list,
            filters=filters,
            orders=orders_list,
            p=pagination
        )