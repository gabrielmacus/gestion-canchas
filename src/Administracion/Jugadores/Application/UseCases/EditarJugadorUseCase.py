from src.Administracion.Jugadores.Domain.Contracts.JugadorRepositoryInterface import JugadorRepositoryInterface
from src.Administracion.Jugadores.Domain.Entities.Jugador import Jugador
from src.Administracion.Jugadores.Application.DTOs.EditarJugadorDTO import EditarJugadorDTO
from src.Administracion.Jugadores.Domain.Exceptions.JugadorNotFound import JugadorNotFound
from src.Administracion.Jugadores.Domain.Services.JugadorFinder import JugadorFinder

class EditarJugadorUseCase:
    def __init__(self, jugador_repository: JugadorRepositoryInterface, jugador_finder: JugadorFinder):
        self._jugador_repository = jugador_repository
        self._jugador_finder = jugador_finder
    
    def execute(self, id: str, request: EditarJugadorDTO) -> Jugador:
        jugador = self._jugador_finder.find_by_id(id)
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
    