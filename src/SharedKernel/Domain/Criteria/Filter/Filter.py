from dataclasses import dataclass
from src.SharedKernel.Domain.Criteria.Filter.FilterField import FilterField
from src.SharedKernel.Domain.Criteria.Filter.FilterOperator import FilterOperator
from src.SharedKernel.Domain.Criteria.Filter.FilterValue import FilterValue


@dataclass(frozen=True)
class Filter:
    field: FilterField
    operator: FilterOperator
    value: FilterValue