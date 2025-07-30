from src.SharedKernel.Domain.Criteria.Criteria import Criteria
from src.SharedKernel.Domain.Services.PaginationService import PaginationService

class PaginarCanchasUseCase:
    
    def __init__(self, pagination_service: PaginationService):
        self._pagination_service = pagination_service
    
    def execute(self, criteria: Criteria):
        return self._pagination_service.paginate(criteria)