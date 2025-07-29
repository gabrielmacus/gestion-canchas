import pytest
from src.Administracion.Jugadores.Application.UseCases.CrearJugadorUseCase import CrearJugadorUseCase
from unittest.mock import ANY, Mock # pyright: ignore[reportAny]
from src.Administracion.Jugadores.Domain.Contracts.JugadorRepositoryInterface import JugadorRepositoryInterface
from src.Administracion.Jugadores.Application.DTOs.CrearJugadorDTO import CrearJugadorDTO
from tests.SharedKernel.Domain.Mothers.IdMother import IdMother
from tests.Administracion.Jugadores.Domain.Mothers.JugadorNombreMother import JugadorNombreMother
from tests.Administracion.Jugadores.Domain.Mothers.JugadorApellidoMother import JugadorApellidoMother
from tests.Administracion.Jugadores.Domain.Mothers.JugadorEmailMother import JugadorEmailMother
from tests.Administracion.Jugadores.Domain.Mothers.JugadorTelefonoMother import JugadorTelefonoMother

class TestCrearJugadorUseCase:
    __crear_jugador_use_case: CrearJugadorUseCase | None = None
    __jugador_repository: Mock | None = None

    @pytest.fixture(autouse=True)
    def setup(self):
        self.__jugador_repository = Mock(spec=JugadorRepositoryInterface)
        self.__crear_jugador_use_case = CrearJugadorUseCase(self.__jugador_repository) # pyright: ignore[reportAny]
    
    def __then_jugador_is_created(self, request: CrearJugadorDTO):
        assert self.__jugador_repository is not None
        self.__jugador_repository.add.assert_called_once_with(ANY) # pyright: ignore[reportAny]
        assert self.__jugador_repository.add.call_args_list[0][0][0].id.value == request.id # pyright: ignore[reportAny]
        assert self.__jugador_repository.add.call_args_list[0][0][0].nombre.value == request.nombre # pyright: ignore[reportAny]
        assert self.__jugador_repository.add.call_args_list[0][0][0].apellido.value == request.apellido # pyright: ignore[reportAny]
        assert self.__jugador_repository.add.call_args_list[0][0][0].telefono.value == request.telefono # pyright: ignore[reportAny]
        assert self.__jugador_repository.add.call_args_list[0][0][0].email.value == request.email # pyright: ignore[reportAny]
    
    def test_crear_jugador(self):
        # Given
        request = CrearJugadorDTO(
            id=IdMother.create(),
            nombre=JugadorNombreMother.create(),
            apellido=JugadorApellidoMother.create(),
            email=JugadorEmailMother.create(),
            telefono=JugadorTelefonoMother.create(),
        )
        
        # When
        assert self.__crear_jugador_use_case is not None
        _ = self.__crear_jugador_use_case.execute(request)

        # Then
        self.__then_jugador_is_created(request)