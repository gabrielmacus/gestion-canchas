from src.SharedKernel.Domain.Criteria.Order.Order import Order
from src.SharedKernel.Domain.Criteria.Order.OrderType import OrderType, OrderTypes
from src.SharedKernel.Domain.Criteria.Criteria import Criteria
from src.SharedKernel.Domain.Criteria.Filter.Filter import Filter
from src.SharedKernel.Domain.Criteria.Filter.FilterField import FilterField
from src.SharedKernel.Domain.Criteria.Filter.FilterOperator import FilterOperator
from src.SharedKernel.Domain.Criteria.Filter.FilterOperator import FilterOperators
from src.SharedKernel.Domain.Criteria.Filter.FilterValue import FilterValue
from src.SharedKernel.Domain.Criteria.Filter.Filters import Filters
from src.SharedKernel.Domain.Criteria.Order.OrderBy import OrderBy
from src.SharedKernel.Domain.Criteria.Order.Orders import Orders
from src.SharedKernel.Domain.Criteria.Pagination.PageSize import PageSize
from src.SharedKernel.Domain.Criteria.Pagination.PageNumber import PageNumber
from src.SharedKernel.Domain.Criteria.Fields.Fields import Fields
from src.SharedKernel.Domain.Contracts.TimeProviderInterface import TimeProviderInterface

class ReservasActivasQuery:
    """
    Query para obtener las reservas activas de una cancha.
    Se considera activa una reserva si la fecha y hora de la reserva es mayor o igual a la fecha y hora actual.

    Args:
        cancha_id (str): Id de la cancha.
        time_provider (TimeProviderInterface): Proveedor de tiempo.

    Returns:
        Criteria: Criteria para obtener las reservas activas de una cancha.
    """

    @staticmethod
    def create(cancha_id: str, time_provider: TimeProviderInterface) -> Criteria:
        # TODO: argumentos para paginar y seleccionar campos
        return Criteria(
            filters=Filters([
                Filter(
                    field=FilterField("cancha_id"),
                    operator=FilterOperator(FilterOperators.EQ),
                    value=FilterValue(cancha_id)
                ),
                Filter(
                    field=FilterField("fecha_hora"),
                    operator=FilterOperator(FilterOperators.GTE),
                    value=FilterValue(time_provider.now_utc().isoformat())
                )
            ]),
            orders=Orders([
                Order(
                    order_by=OrderBy("id"),
                    order_type=OrderType(OrderTypes.DESC)
                )]),
            page_size=PageSize(None),
            page_number=PageNumber(None),
            fields=Fields(None)
        )