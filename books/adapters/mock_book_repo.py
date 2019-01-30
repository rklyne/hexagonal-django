from ..interfaces.book_repo import BookRepoInterface


class BookRepo(BookRepoInterface):
    def __init__(self):
        self._assert_interface_complete()
        self.books = []

    def add_book(self, book):
        self.books.append(book)

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
