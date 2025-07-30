from dataclasses import dataclass
from src.SharedKernel.Domain.Criteria.Order.Order import Order

@dataclass(frozen=True)
class Orders:
    value: list[Order] | None