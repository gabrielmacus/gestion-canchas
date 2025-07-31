from src.Administracion.Reservas.Domain.Services.BookingService import BookingService
from src.SharedKernel.Domain.Contracts.TimeProviderInterface import TimeProviderInterface
import pytest
from src.Administracion.Reservas.Domain.Contracts.ReservaRepository import ReservaRepositoryInterface
from datetime import datetime
from unittest.mock import Mock
from src.Administracion.Reservas.Domain.Entities.Reserva import Reserva
from src.Administracion.Reservas.Domain.Exceptions.CanchaReservadaException import CanchaReservadaException
from tests.Administracion.Reservas.Domain.Mothers.ReservaMother import ReservaMother
from tests.SharedKernel.Domain.Mothers.IdMother import IdMother
from src.SharedKernel.Domain.Criteria.Criteria import Criteria
from src.SharedKernel.Domain.Criteria.Filter.Filter import Filter
from src.SharedKernel.Domain.Criteria.Filter.FilterField import FilterField
from src.SharedKernel.Domain.Criteria.Filter.FilterOperator import FilterOperator
from src.SharedKernel.Domain.Criteria.Filter.FilterOperator import FilterOperators
from src.SharedKernel.Domain.Criteria.Filter.FilterValue import FilterValue
from src.SharedKernel.Domain.Criteria.Filter.Filters import Filters
from src.SharedKernel.Domain.Criteria.Order.Order import Order
from src.SharedKernel.Domain.Criteria.Order.OrderBy import OrderBy
from src.SharedKernel.Domain.Criteria.Order.OrderType import OrderType, OrderTypes
from src.SharedKernel.Domain.Criteria.Order.Orders import Orders
from src.SharedKernel.Domain.Criteria.Fields.Fields import Fields
import parametrize_from_file as pff

class TestBookingService:
    __time_provider: Mock | None = None
    __reserva_repository: Mock | None = None
    __booking_service: BookingService | None = None
    
    @pytest.fixture(autouse=True)
    def setup(self):
        self.__time_provider =  Mock(spec=TimeProviderInterface)
        self.__reserva_repository = Mock(spec=ReservaRepositoryInterface)
        self.__booking_service = BookingService(
            self.__time_provider,  # pyright: ignore[reportAny]
            self.__reserva_repository # pyright: ignore[reportAny]
        ) 
    
    def __given_date_time_is(self, date_time: datetime):
        assert self.__time_provider is not None
        self.__time_provider.now_utc.return_value = date_time # pyright: ignore[reportAny]
    
    def __given_actives_reservas_are(self, reservas: list[Reserva]):
        assert self.__reserva_repository is not None
        self.__reserva_repository.matching.return_value = reservas # pyright: ignore[reportAny]
    
    def __then_actives_reservas_are_searched(self, cancha_id: str):
        assert self.__reserva_repository is not None
        assert self.__time_provider is not None
        self.__reserva_repository.matching.assert_called_once_with(Criteria( # pyright: ignore[reportAny]
            filters=Filters([
                Filter(
                    field=FilterField("cancha_id"),
                    operator=FilterOperator(FilterOperators.EQ),
                    value=FilterValue(cancha_id)
                ),
                Filter(
                    field=FilterField("fecha_hora"),
                    operator=FilterOperator(FilterOperators.GTE),
                    value=FilterValue(self.__time_provider.now_utc().isoformat()) # pyright: ignore[reportAny]
                )
            ]),
            orders=Orders([
                Order(
                    order_by=OrderBy("id"),
                    order_type=OrderType(OrderTypes.DESC)
                )]),
            pagination=None,
            fields=Fields(None)
        ))

    def __then_reserva_is_added(self, reserva: Reserva):
        assert self.__reserva_repository is not None
        self.__reserva_repository.add.assert_called_once_with(reserva) # pyright: ignore[reportAny]
    
    def __then_reserva_is_not_added(self):
        assert self.__reserva_repository is not None
        self.__reserva_repository.add.assert_not_called() # pyright: ignore[reportAny]

    @pff #pyright: ignore[reportCallIssue, reportUntypedFunctionDecorator]
    def test_succesful_booking(self, 
                               expected_fecha_hora:datetime,
                               expected_duracion:int,
                               reserva_1_fecha:datetime,
                               reserva_1_duracion:int,
                               reserva_2_fecha:datetime,
                               reserva_2_duracion:int,
                               ):
        # Given
        now = datetime(2025, 1, 1, 12, 0)
        self.__given_date_time_is(now)
        cancha_id = IdMother.create()
        self.__given_actives_reservas_are([
            ReservaMother.create(
                now=now,
                fecha_hora=reserva_1_fecha,
                duracion=reserva_1_duracion,
                cancha_id=cancha_id
            ),
            ReservaMother.create(
                now=now,
                fecha_hora=reserva_2_fecha,
                duracion=reserva_2_duracion,
                cancha_id=cancha_id
            ),
        ])
        expected_reserva = ReservaMother.create(
            now=now,
            fecha_hora=expected_fecha_hora,
            duracion=expected_duracion,
            cancha_id=cancha_id
        )
        
        # When
        assert self.__booking_service is not None
        reserva = self.__booking_service.book(
            id=expected_reserva.id.value,
            fecha_hora=expected_reserva.fecha_hora.value,
            duracion=expected_reserva.duracion.value,
            cancha_id=expected_reserva.cancha_id.value
        )
        
        # Then
        self.__then_actives_reservas_are_searched(cancha_id)
        self.__then_reserva_is_added(reserva)
    @pff #pyright: ignore[reportCallIssue, reportUntypedFunctionDecorator]
    def test_booking_with_colliding_datetime(self, 
                               expected_fecha_hora:datetime,
                               expected_duracion:int,
                               reserva_1_fecha:datetime,
                               reserva_1_duracion:int,
                               reserva_2_fecha:datetime,
                               reserva_2_duracion:int,
                               ):
        # Given
        now = datetime(2025, 1, 1, 12, 0)
        self.__given_date_time_is(now)
        cancha_id = IdMother.create()
        self.__given_actives_reservas_are([
            ReservaMother.create(
                now=now,
                fecha_hora=reserva_1_fecha,
                duracion=reserva_1_duracion,
                cancha_id=cancha_id
            ),
            ReservaMother.create(
                now=now,
                fecha_hora=reserva_2_fecha,
                duracion=reserva_2_duracion,
                cancha_id=cancha_id
            ),
        ])
        
        # When
        assert self.__booking_service is not None
        with pytest.raises(CanchaReservadaException):
            _ = self.__booking_service.book(
                id=IdMother.create(),
                fecha_hora=expected_fecha_hora,
                duracion=expected_duracion,
                cancha_id=cancha_id
            )
        
        # Then
        self.__then_reserva_is_not_added()