from enum import Enum
from dataclasses import dataclass


class OrderTypes(Enum):
    ASC = "asc"
    DESC = "desc"
    
@dataclass(frozen=True)
class OrderType:
    value: OrderTypes