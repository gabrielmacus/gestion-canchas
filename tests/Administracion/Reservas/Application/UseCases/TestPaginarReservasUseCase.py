import random
from typing import Any
from src.Administracion.Reservas.Application.UseCases.PaginarReservasUseCase import PaginarReservasUseCase
from src.Administracion.Reservas.Domain.Contracts.ReservaRepository import ReservaRepositoryInterface
from unittest.mock import Mock
from src.SharedKernel.Domain.Pagination.PagedResult import PagedResult
from src.SharedKernel.Domain.Criteria.Filter.Filters import Filters
from src.SharedKernel.Domain.Criteria.Order.Orders import Orders
from src.SharedKernel.Domain.Criteria.Fields.Fields import Fields
from src.SharedKernel.Domain.Criteria.Pagination import Pagination
import pytest
from src.Administracion.Reservas.Domain.Entities.Reserva import Reserva
from tests.Administracion.Reservas.Domain.Mothers.ReservaMother import ReservaMother
from src.SharedKernel.Domain.Services.PaginationService import PaginationService
from src.SharedKernel.Domain.Criteria.Criteria import Criteria
from src.SharedKernel.Domain.Criteria.Filter.Filters import Filters
from src.SharedKernel.Domain.Criteria.Order.Order import Order

class TestPaginarReservasUseCase:
    __use_case: PaginarReservasUseCase
    __pagination_service: Mock
    
    @pytest.fixture(autouse=True)
    def setup(self):
        self.__pagination_service = Mock(PaginationService)
        self.__use_case = PaginarReservasUseCase(self.__pagination_service)

    def __then_criteria_is_used(self, criteria: Criteria):
        self.__pagination_service.paginate.assert_called_once_with(criteria)

    def test_should_paginate(self):
        # Given
        criteria = Criteria(
            filters=Filters([]),
            orders=Orders([]),
            pagination=Pagination(random.randint(1, 100), random.randint(1, 100)),
            fields=Fields([])
        )
        # When
        self.__use_case.execute(criteria)
        # Then
        self.__then_criteria_is_used(criteria)