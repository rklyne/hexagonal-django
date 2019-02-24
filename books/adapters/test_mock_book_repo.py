from ..interfaces.book_repo_contract import contract_test
from .mock_book_repo import BookRepo


class TestMockBookRepo(contract_test(BookRepo)):
    pass
