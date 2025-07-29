from enum import Enum
from dataclasses import dataclass


class OrderTypes(Enum):
    ASC = "ASC"
    DESC = "DESC"
    
@dataclass(frozen=True)
class OrderType:
    value: OrderTypes