from src.Administracion.Jugadores.Domain.Contracts.JugadorRepositoryInterface import JugadorRepositoryInterface
from src.Administracion.Jugadores.Application.DTOs.CrearJugadorDTO import CrearJugadorDTO
from src.Administracion.Jugadores.Domain.Entities.Jugador import Jugador

class CrearJugadorUseCase:
    def __init__(self, jugador_repository: JugadorRepositoryInterface):
        self.__jugador_repository = jugador_repository

    def execute(self, request: CrearJugadorDTO):
        jugador = Jugador.create(
            id = request.id, 
            nombre = request.nombre, 
            apellido = request.apellido, 
            telefono = request.telefono,
            email = request.email
        )
        self.__jugador_repository.add(jugador)
        # TODO: Domain Events