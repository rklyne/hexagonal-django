from .adapter import BookRepo
from .services.book_search import BookSearchService


class Application(object):
    def __init__(self):
        self._books = BookRepo()
        self.book_search = BookSearchService(self._books)


app = Application()  # NOQA - This is a nicer API
