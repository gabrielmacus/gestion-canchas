from enum import Enum
from dataclasses import dataclass

class FilterOperators(Enum):
    EQ = "="
    NEQ = "!="
    GT = ">"
    LT = "<"
    GTE = ">="
    LTE = "<="
    CONTAINS = "CONTAINS"
    NOT_CONTAINS = "NOT_CONTAINS"
    STARTS_WITH = "STARTS_WITH"
    ENDS_WITH = "ENDS_WITH"
    
@dataclass(frozen=True)
class FilterOperator:
    value: FilterOperators