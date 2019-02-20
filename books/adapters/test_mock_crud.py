from .mock_crud import MockCrud
from ..interfaces.crud_contract import test_contract


MockCrudTest = test_contract(MockCrud)
