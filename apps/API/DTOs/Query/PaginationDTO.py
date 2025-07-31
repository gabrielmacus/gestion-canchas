from pydantic import BaseModel

class PaginationDTO(BaseModel):
    size: int
    number: int