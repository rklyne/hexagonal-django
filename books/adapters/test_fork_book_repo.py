from .fork_book_repo import ForkRepo
from .mock_book_repo import BookRepo as MockRepo
from .test_mock_book_repo import contract_test


class TestForkRepo(contract_test(lambda: ForkRepo(MockRepo(), MockRepo()))):
    pass
