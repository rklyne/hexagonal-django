from .mock_crud import MockCrud
from ..interfaces.crud_contract import contract_test


MockCrudTest = contract_test(MockCrud)
