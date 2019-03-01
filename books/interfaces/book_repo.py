from .crud import CrudInterface


class BookRepoError(Exception):
    pass


class BookRepoInterface(CrudInterface):
    def add_book(self, book):
        """
        Adds a book to the repo.
        If not possible, raises a BookRepoError
        """
        raise NotImplementedError

    def iter_by_title(self, title):
        raise NotImplementedError

    def iter_by_author(self, author):
        raise NotImplementedError

    def count(self):
        raise NotImplementedError

    def iter_all(self):
        raise NotImplementedError
