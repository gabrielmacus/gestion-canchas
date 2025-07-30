from dataclasses import dataclass
from typing import TYPE_CHECKING
from src.SharedKernel.Domain.Criteria.Filter.Filters import Filters

if TYPE_CHECKING:
    from src.SharedKernel.Domain.Criteria.Criteria import Criteria

@dataclass(frozen=True)
class CountCriteria:
    """
    Criteria específica para consultas de count.
    Solo incluye filtros ya que paginación y orden no son relevantes para count.
    """
    filters: Filters
    
    @classmethod
    def from_criteria(cls, criteria: 'Criteria') -> 'CountCriteria':
        """
        Crea una CountCriteria a partir de una Criteria existente,
        extrayendo solo los filtros.
        """
        return cls(filters=criteria.filters)
    
    @classmethod
    def empty(cls) -> 'CountCriteria':
        """
        Crea una CountCriteria sin filtros para contar todos los registros.
        """
        return cls(filters=Filters(None))
    