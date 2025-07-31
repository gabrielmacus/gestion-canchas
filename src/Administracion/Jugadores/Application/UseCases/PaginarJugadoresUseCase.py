from src.SharedKernel.Domain.Criteria.Criteria import Criteria
from src.SharedKernel.Domain.Services.PaginationService import PaginationService
from src.Administracion.Jugadores.Domain.Entities.Jugador import Jugador

class PaginarJugadoresUseCase:
    def __init__(self, pagination_service: PaginationService[Jugador]): # pyright: ignore[reportUnknownArgumentType]
        self._pagination_service = pagination_service
    
    def execute(self, criteria: Criteria):
        return self._pagination_service.paginate(criteria)