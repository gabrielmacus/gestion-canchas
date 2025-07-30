from src.Administracion.Jugadores.Domain.Contracts.JugadorRepositoryInterface import JugadorRepositoryInterface
from src.Administracion.Jugadores.Domain.Entities.Jugador import Jugador
from src.Administracion.Jugadores.Application.DTOs.EditarJugadorDTO import EditarJugadorDTO
from src.Administracion.Jugadores.Domain.Exceptions.JugadorNotFound import JugadorNotFound

class EditarJugadorUseCase:
    def __init__(self, jugador_repository: JugadorRepositoryInterface):
        self._jugador_repository = jugador_repository
    
    def execute(self, id: str, request: EditarJugadorDTO) -> Jugador:
        jugador = self._find_jugador(id)
        updated_jugador = self._update_jugador(jugador, request)
        self._jugador_repository.update_by_id(id, updated_jugador)
        return updated_jugador
    
    def _update_jugador(self, jugador: Jugador, request: EditarJugadorDTO) -> Jugador:
        """Crea una nueva instancia de Jugador con los valores actualizados, respetando inmutabilidad"""
        return Jugador(
            id=jugador.id.value,
            nombre=request.nombre or jugador.nombre.value,
            apellido=request.apellido or jugador.apellido.value,
            telefono=request.telefono or jugador.telefono.value,
            email=request.email or jugador.email.value
        )
    
    def _find_jugador(self, id: str) -> Jugador:
        jugador = self._jugador_repository.get_by_id(id)
        if not jugador:
            raise JugadorNotFound(id)
        return jugador