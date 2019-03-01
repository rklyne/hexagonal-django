from itertools import count

from ..interfaces.book_repo import BookRepoInterface
from ..interfaces.crud import CrudError


class BookRepo(BookRepoInterface):
    def __init__(self):
        self.books = []
        self._next_id = count(1).next

    def create(self, one):
        try:
            self.get(one.id)
        except CrudError:
            pass
        else:
            raise CrudError
        self.books.append(one)
        one.id = self._next_id()
        return one.id

    add_book = create

    def count(self):
        return len(self.books)

    def iter_by_title(self, title):
        for book in self.books:
            if book.title == title:
                yield book

    def iter_by_author(self, author):
        for book in self.books:
            if book.author == author:
                yield book

    def iter_all(self):
        for book in self.books:
            yield book

    def delete(self, one):
        idx = -1
        for idx, book in enumerate(self.books):
            if book.id == one.id:
                break
        else:
            raise CrudError
        del self.books[idx]

    def get(self, uuid):
        for book in self.books:
            if book.id == uuid:
                return book
        raise CrudError

    def update(self, one):
        idx = -1
        for idx, book in enumerate(self.books):
            if book.id == one.id:
                break
        else:
            raise CrudError
        if idx < 0:
            raise CrudError
        self.books[idx] = one
