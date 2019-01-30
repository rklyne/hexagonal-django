from unittest import TestCase

from .author import Author
from .book import Book


class TestBook(TestCase):
    def setUp(self):
        self.author = Author("individual 1")

    def test_has_isbn_true(self):
        book = Book("my book", author=self.author, isbn="123")
        self.assertTrue(book.has_isbn())

    def test_has_isbn_false(self):
        book = Book("my book", author=self.author)
        self.assertFalse(book.has_isbn())
