from typing import final
import pytest
from sqlalchemy import Select, Column, Integer, String
from sqlalchemy.orm import DeclarativeBase
from src.SharedKernel.Domain.Criteria.Order.OrderBy import OrderBy
from src.SharedKernel.Domain.Criteria.Filter.Filter import Filter
from src.SharedKernel.Domain.Criteria.Filter.FilterOperator import FilterOperator,FilterOperators
from src.SharedKernel.Infraestructure.Criteria.CriteriaToSQLAlchemyConverter import CriteriaToSQLAlchemyConverter
from src.SharedKernel.Domain.Criteria.Criteria import Criteria
from src.SharedKernel.Domain.Criteria.Filter.Filters import Filters
from src.SharedKernel.Domain.Criteria.Order.Order import Order
from src.SharedKernel.Domain.Criteria.Order.OrderType import OrderType,OrderTypes
from src.SharedKernel.Domain.Criteria.Order.Orders import Orders
from src.SharedKernel.Domain.Criteria.Pagination.PageSize import PageSize
from src.SharedKernel.Domain.Criteria.Pagination.PageNumber import PageNumber
from src.SharedKernel.Domain.Criteria.Filter.FilterField import FilterField
from src.SharedKernel.Domain.Criteria.Filter.FilterValue import FilterValue
from src.SharedKernel.Domain.Criteria.Fields.Fields import Fields
from src.SharedKernel.Domain.Criteria.Fields.Field import Field

class Base(DeclarativeBase):
    pass

@final
class Entity(Base):
    __tablename__ = "test"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    surname = Column(String)
    age = Column(Integer)


class TestCriteriaToSQLAlchemyConverter:
    __converter: CriteriaToSQLAlchemyConverter[Entity] | None = None
    
    @pytest.fixture(autouse=True)
    def setup(self):
        self.__converter = CriteriaToSQLAlchemyConverter[Entity]()
    
    def __then_compiled_query_is(self, query: Select[tuple[Entity]], expected_query: str):
        compiled_query = str(query.compile(compile_kwargs={"literal_binds": True}))\
            .replace('\n', ' ')\
            .replace('  ', ' ')\
            .strip()
        assert compiled_query == expected_query
    
    def test_select_id_and_name_only(self):
        # Given
        criteria = Criteria(
            filters=Filters([]),
            orders=Orders([]),
            page_size=PageSize(None),
            page_number=PageNumber(None),
            fields=Fields([
                Field("id")
            ])
        )
        
        # When
        assert self.__converter is not None
        query = self.__converter.convert(Entity, criteria)
        
        # Then
        expected_query = "SELECT test.id FROM test"
        self.__then_compiled_query_is(query, expected_query)
        
    def test_select_all_fields(self):
        # Given
        criteria = Criteria(
            filters=Filters(None),
            orders=Orders(None),
            page_size=PageSize(None),
            page_number=PageNumber(None),
            fields=Fields(None)
        )
        
        # When
        assert self.__converter is not None
        query = self.__converter.convert(Entity, criteria)
        
        # Then
        expected_query = "SELECT test.id, test.name, test.surname, test.age FROM test"
        self.__then_compiled_query_is(query, expected_query)
    
    def test_query_with_filter(self):
        # Given
        criteria = Criteria(
            filters=Filters([
                Filter(
                    field=FilterField("id"),
                    operator=FilterOperator(FilterOperators.EQ),
                    value=FilterValue("1")
                )
            ]),
            orders=Orders([]),
            page_size=PageSize(10),
            page_number=PageNumber(1),
            fields=Fields([])
        )
        
        # When
        assert self.__converter is not None
        query = self.__converter.convert(Entity, criteria)
        
        # Then
        expected_query = "SELECT test.id, test.name, test.surname, test.age FROM test WHERE id = '1' LIMIT 10 OFFSET 0"
        self.__then_compiled_query_is(query, expected_query)
        
    def test_query_with_filter_and_order(self):
        # Given
        criteria = Criteria(
            filters=Filters([
                Filter(
                    field=FilterField("id"),
                    operator=FilterOperator(FilterOperators.EQ),
                    value=FilterValue("1")
                )
            ]),
            orders=Orders([
                Order(
                    order_by=OrderBy("id"),
                    order_type=OrderType(OrderTypes.ASC)
                ),
                Order(
                    order_by=OrderBy("name"),
                    order_type=OrderType(OrderTypes.DESC)
                )
            ]),
            page_size=PageSize(None),
            page_number=PageNumber(None),
            fields=Fields([])
        )
        
        # When
        assert self.__converter is not None
        query = self.__converter.convert(Entity, criteria)
        
        # Then
        expected_query = "SELECT test.id, test.name, test.surname, test.age FROM test WHERE id = '1' ORDER BY id ASC, name DESC"
        self.__then_compiled_query_is(query, expected_query)
        
    def test_query_with_complex_filter_and_order_and_pagination(self):
        # Given
        criteria = Criteria(
            filters=Filters([
                Filter(
                    field=FilterField("id"),
                    operator=FilterOperator(FilterOperators.EQ),
                    value=FilterValue("1")
                ),
                Filter(
                    field=FilterField("name"),
                    operator=FilterOperator(FilterOperators.CONTAINS),
                    value=FilterValue("John")
                ),
                Filter(
                    field=FilterField("surname"),
                    operator=FilterOperator(FilterOperators.NOT_CONTAINS),
                    value=FilterValue("Doe")
                ),
                Filter(
                    field=FilterField("age"),
                    operator=FilterOperator(FilterOperators.GTE),
                    value=FilterValue("20")
                )
            ]),
            orders=Orders([
                Order(
                    order_by=OrderBy("id"),
                    order_type=OrderType(OrderTypes.ASC)
                ),
                Order(
                    order_by=OrderBy("name"),
                    order_type=OrderType(OrderTypes.DESC)
                )
            ]),
            page_size=PageSize(10),
            page_number=PageNumber(1),
            fields=Fields([])
        )
        
        # When
        assert self.__converter is not None
        query = self.__converter.convert(Entity, criteria)
        
        # Then
        expected_query = "SELECT test.id, test.name, test.surname, test.age FROM test WHERE id = '1' AND lower(name) LIKE lower('%John%') AND lower(surname) NOT LIKE lower('%Doe%') AND age >= '20' ORDER BY id ASC, name DESC LIMIT 10 OFFSET 0"
        self.__then_compiled_query_is(query, expected_query)