from src.Administracion.Jugadores.Application.UseCases.EliminarJugadorUseCase import EliminarJugadorUseCase
from unittest.mock import Mock
import pytest
from src.Administracion.Jugadores.Domain.Entities.Jugador import Jugador
from tests.Administracion.Jugadores.Domain.Mothers.JugadorMother import JugadorMother

class TestEliminarJugadorUseCase:
    
    @pytest.fixture(autouse=True)
    def setup(self):
        self.__jugador_finder = Mock()
        self.__jugador_repository = Mock()
        self.__use_case = EliminarJugadorUseCase(self.__jugador_repository, self.__jugador_finder)
    
    def __given_jugador_finder_returns_jugador(self, jugador: Jugador):
        self.__jugador_finder.find_by_id.return_value = jugador
    
    def __then_jugador_is_searched(self, id: str):
        self.__jugador_finder.find_by_id.assert_called_once_with(id)
    
    def __then_jugador_is_deleted(self, id: str):
        self.__jugador_repository.delete_by_id.assert_called_once_with(id)
    
    def test_eliminar_jugador(self):
        # Given
        jugador = JugadorMother.create()
        self.__given_jugador_finder_returns_jugador(jugador)
        
        # When
        self.__use_case.execute(jugador.id.value)
        
        # Then
        self.__then_jugador_is_searched(jugador.id.value)
        self.__then_jugador_is_deleted(jugador.id.value)
    