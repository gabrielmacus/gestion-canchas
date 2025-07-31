from apps.API.Controllers.BaseFindRequestHandler import BaseFindRequestHandler
from src.Administracion.Jugadores.Application.UseCases.PaginarJugadoresUseCase import PaginarJugadoresUseCase
from src.SharedKernel.Domain.Criteria.Criteria import Criteria
from src.SharedKernel.Domain.Pagination.PagedResult import PagedResult
from src.Administracion.Jugadores.Domain.Entities.Jugador import Jugador
from apps.API.DTOs.JugadorDTO import JugadorDTO
from src.SharedKernel.Infraestructure.Services.SAConnection import SAConnection
from src.SharedKernel.Domain.Services.PaginationService import PaginationService
from src.Administracion.Jugadores.Infraestructure.Services.SAJugadorRepository import SAJugadorRepository
from apps.API.Mappings.JugadorMappings import JugadorMappings

class JugadorFindHandler(BaseFindRequestHandler):
    def __init__(self):
        self._repository = SAJugadorRepository(SAConnection().get_engine())
        self._paginar_jugadores_usecase = PaginarJugadoresUseCase(
            PaginationService(self._repository, self._repository)
        )

    def _paginate(self, criteria: Criteria):
        return self._paginar_jugadores_usecase.execute(criteria)
    
    def _map_to_response(self, result: PagedResult[Jugador]):
        return JugadorMappings.to_paged_response_dto(result)