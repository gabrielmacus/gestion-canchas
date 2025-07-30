from dataclasses import dataclass
from .OrderBy import OrderBy
from .OrderType import OrderType


@dataclass(frozen=True)
class Order:
    order_by: OrderBy
    order_type: OrderType