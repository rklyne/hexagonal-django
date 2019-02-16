from contextlib import contextmanager
from .adapters.django import BookRepo
from .adapters.mock_book_repo import BookRepo as MockBookRepo
from .services.book_creation import CreateBookCommand
from .services.book_search import BookSearchService


class Application(object):
    def __init__(self, mock=False):
        if mock:
            self._books = MockBookRepo()
        else:
            self._books = BookRepo()
        self.book_search = BookSearchService(self._books)
        self.book_creation = CreateBookCommand(self._books, None)


app = Application()  # NOQA - This is a nicer API
