from apps.API.Controllers.BaseFindRequestHandler import BaseFindRequestHandler
from src.Administracion.Canchas.Application.UseCases.PaginarCanchasUseCase import PaginarCanchasUseCase
from src.SharedKernel.Domain.Criteria.Criteria import Criteria
from src.SharedKernel.Domain.Pagination.PagedResult import PagedResult
from src.Administracion.Canchas.Domain.Entities.Cancha import Cancha
from apps.API.DTOs.CanchaDTO import CanchaDTO
from src.SharedKernel.Infraestructure.Services.SAConnection import SAConnection
from src.SharedKernel.Domain.Services.PaginationService import PaginationService
from src.Administracion.Canchas.Infraestructure.Services.SACanchaRepository import SACanchaRepository
from apps.API.Mappings.CanchaMappings import CanchaMappings

class CanchaFindHandler(BaseFindRequestHandler):
    def __init__(self):
        self._repository = SACanchaRepository(SAConnection().get_engine())
        self._paginar_canchas_usecase = PaginarCanchasUseCase(
            PaginationService(self._repository, self._repository)
        )

    def _paginate(self, criteria: Criteria):
        return self._paginar_canchas_usecase.execute(criteria)
    
    def _map_to_response(self, result: PagedResult[Cancha]):
        return CanchaMappings.to_paged_response_dto(result) 