from pydantic import BaseModel
from src.SharedKernel.Domain.Criteria.Filter.FilterOperator import FilterOperators

class FilterDTO(BaseModel):
    field: str
    operator: FilterOperators
    value: str
    
    
    
    