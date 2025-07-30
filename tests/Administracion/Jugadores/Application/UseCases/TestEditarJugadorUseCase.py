from src.Administracion.Jugadores.Application.UseCases.EditarJugadorUseCase import EditarJugadorUseCase
from unittest.mock import Mock
import pytest
from src.Administracion.Jugadores.Application.DTOs.EditarJugadorDTO import EditarJugadorDTO
from src.Administracion.Jugadores.Domain.Entities.Jugador import Jugador
from tests.Administracion.Jugadores.Domain.Mothers.JugadorMother import JugadorMother

class TestEditarJugadorUseCase:
    
    @pytest.fixture(autouse=True)
    def setup(self):
        self.__jugador_repository = Mock()
        self.__use_case = EditarJugadorUseCase(self.__jugador_repository)
    
    def __given_repository_returns_jugador(self, jugador: Jugador):
        self.__jugador_repository.get_by_id.return_value = jugador
    
    def __then_jugador_is_updated(self, jugador: Jugador):
        self.__jugador_repository.update_by_id.assert_called_once_with(jugador.id.value, jugador)
    
    def test_editar_jugador(self):
        # Given
        jugador = JugadorMother.create()
        data = EditarJugadorDTO(
            nombre="Juan",
            apellido="Perez",
            telefono="1234567890",
            email="juan.perez@example.com"
        )
        self.__given_repository_returns_jugador(jugador)
        
        # When
        self.__use_case.execute(jugador.id.value, data)
        
        # Then
        self.__then_jugador_is_updated(jugador)