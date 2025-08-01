from typing import  Any, TypeVar, Generic
from sqlalchemy import  UnaryExpression, column, select, Select, func
from sqlalchemy.orm import DeclarativeBase, load_only
from src.SharedKernel.Domain.Criteria.Criteria import Criteria
from src.SharedKernel.Domain.Criteria.Filter.Filter import Filter
from src.SharedKernel.Domain.Criteria.Filter.Filters import Filters
from src.SharedKernel.Domain.Criteria.Filter.FilterOperator import FilterOperators
from src.SharedKernel.Domain.Criteria.Order.Orders import Orders
from src.SharedKernel.Domain.Criteria.Order.OrderType import OrderTypes
from src.SharedKernel.Domain.Criteria.Pagination import Pagination
from src.SharedKernel.Domain.Criteria.Fields.Fields import Fields
from src.SharedKernel.Domain.Criteria.CountCriteria import CountCriteria

T = TypeVar('T', bound=DeclarativeBase)


class CriteriaToSQLAlchemyConverter():
    """
    Convierte objetos Criteria del dominio en consultas SQLAlchemy
    """
    def _apply_filter(self, query: Select[tuple[Any]], filter: Filter):
        """
        Aplica un filtro a la consulta SQLAlchemy
        """
        if filter.operator.value == FilterOperators.EQ:
            query = query.where(column(filter.field.value) == filter.value.value)
        elif filter.operator.value == FilterOperators.NEQ:
            query = query.where(column(filter.field.value) != filter.value.value)
        elif filter.operator.value == FilterOperators.GT:
            query = query.where(column(filter.field.value) > filter.value.value)
        elif filter.operator.value == FilterOperators.GTE:
            query = query.where(column(filter.field.value) >= filter.value.value)
        elif filter.operator.value == FilterOperators.LT:
            query = query.where(column(filter.field.value) < filter.value.value)
        elif filter.operator.value == FilterOperators.LTE:
            query = query.where(column(filter.field.value) <= filter.value.value)
        elif filter.operator.value == FilterOperators.CONTAINS:
            query = query.where(column(filter.field.value).ilike(f"%{filter.value.value}%"))
        elif filter.operator.value == FilterOperators.NOT_CONTAINS:
            query = query.where(column(filter.field.value).not_ilike(f"%{filter.value.value}%"))
        elif filter.operator.value == FilterOperators.STARTS_WITH:
            query = query.where(column(filter.field.value).ilike(f"{filter.value.value}%"))
        elif filter.operator.value == FilterOperators.ENDS_WITH:
            query = query.where(column(filter.field.value).ilike(f"%{filter.value.value}"))
        else:
            raise ValueError(f"Invalid filter operator: {filter.operator.value}")
        return query

    def _select_fields(self, entity: type[T], query: Select[tuple[T]], fields: Fields):
        if fields.value is None or len(fields.value) == 0:
            return query
        
        query = query.options(load_only(*[getattr(entity, field.value) for field in fields.value])) # pyright: ignore[reportAny]
        return query
    
    def _apply_filters(self, query: Select[tuple[Any]], filters: Filters):
        if filters.value is None:
            return query
        for filter in filters.value:
                query = self._apply_filter(query, filter)
        return query
    
    def _apply_pagination(self, query: Select[tuple[T]], pagination: Pagination | None):
        """
        Aplica una paginación a la consulta SQLAlchemy
        """
        if pagination is not None:
            query = query.limit(pagination.size)
            query = query.offset((pagination.page - 1) * pagination.size)
        return query
    
    def _apply_order(self, query: Select[tuple[T]], orders: Orders):
        """
        Aplica un orden a la consulta SQLAlchemy
        """
        order_by:list[UnaryExpression[Any]] = [] # pyright: ignore[reportExplicitAny]
        if orders.value is None:
            return query
        for order in orders.value:
            if order.order_type.value == OrderTypes.ASC:
                order_by.append(column(order.order_by.value).asc()) # pyright: ignore[reportUnknownArgumentType]
            elif order.order_type.value == OrderTypes.DESC:
                order_by.append(column(order.order_by.value).desc()) # pyright: ignore[reportUnknownArgumentType]
            else:
                raise ValueError(f"Invalid order type: {order.order_type.value}")
        if len(order_by) > 0:
            query = query.order_by(*order_by)
        return query
    
    def convert(self, entity: type[T], criteria: Criteria):
        query = select(entity)
        query = self._select_fields(entity,query, criteria.fields)
        query = self._apply_filters(query, criteria.filters)
        query = self._apply_pagination(query, criteria.pagination)
        query = self._apply_order(query, criteria.orders)
        return query

    def convert_count(self, entity: type[T], criteria: CountCriteria):
        query = select(func.count("*")).select_from(entity)
        query = self._apply_filters(query, criteria.filters)
        return query