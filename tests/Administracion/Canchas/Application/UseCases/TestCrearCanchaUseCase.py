from src.Administracion.Canchas.Application.UseCases.CrearCanchaUseCase import CrearCanchaUseCase
from src.Administracion.Canchas.Domain.Contracts.CanchaRepositoryInterface import CanchaRepositoryInterface
from unittest.mock import ANY, Mock # pyright: ignore[reportAny]
from src.Administracion.Canchas.Application.DTOs.CrearCanchaDTO import CrearCanchaDTO
from tests.SharedKernel.Domain.Mothers.IdMother import IdMother
from tests.Administracion.Canchas.Domain.Mothers.CanchaNombreMother import CanchaNombreMother
from tests.Administracion.Canchas.Domain.Mothers.CanchaTechadaMother import CanchaTechadaMother
import pytest

class TestCrearCanchaUseCase:
    __crear_cancha_use_case: CrearCanchaUseCase | None = None
    __cancha_repository: Mock | None = None

    @pytest.fixture(autouse=True)
    def setup(self):
        self.__cancha_repository = Mock(spec=CanchaRepositoryInterface)
        self.__crear_cancha_use_case = CrearCanchaUseCase(self.__cancha_repository) # pyright: ignore[reportAny]

    def __then_cancha_is_created(self, request: CrearCanchaDTO):
        assert self.__cancha_repository is not None
        self.__cancha_repository.add.assert_called_once_with(ANY) # pyright: ignore[reportAny]
        assert self.__cancha_repository.add.call_args_list[0][0][0].id.value == request.id # pyright: ignore[reportAny]
        assert self.__cancha_repository.add.call_args_list[0][0][0].nombre.value == request.nombre # pyright: ignore[reportAny]
        assert self.__cancha_repository.add.call_args_list[0][0][0].techada.value == request.techada # pyright: ignore[reportAny]

    def test_crear_cancha(self):
        # Given
        request = CrearCanchaDTO(
            id=IdMother.create(),
            nombre=CanchaNombreMother.create(),
            techada=CanchaTechadaMother.create()
        )
        
        # When
        assert self.__crear_cancha_use_case is not None
        _ = self.__crear_cancha_use_case.execute(request)

        # Then
        self.__then_cancha_is_created(request)