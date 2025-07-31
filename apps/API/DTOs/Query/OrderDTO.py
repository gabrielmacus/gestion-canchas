from pydantic import BaseModel
from src.SharedKernel.Domain.Criteria.Order.OrderType import OrderTypes

class OrderDTO(BaseModel):
    field: str
    direction: OrderTypes