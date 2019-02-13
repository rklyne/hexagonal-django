from __future__ import absolute_import, unicode_literals

from django.test import TestCase

from ..entities.author import Author
from ..entities.book import Book
from ..adapter import BookRepo


class TestMockBookRepo(TestCase):
    def test_create_repo(self):
        repo = BookRepo()
        self.assertTrue(repo)

    def test_add_book(self):
        repo = BookRepo()
        book = Book("asd", Author("asd"))
        book2 = Book("asd2", Author("asdf2"))
        repo.add_book(book)
        repo.add_book(book2)
        self.assertEqual(2, repo.count())

    def test_iter_by_title(self):
        repo = BookRepo()
        book = Book("asd", Author("asdf"))
        book2 = Book("asd2", Author("asdf2"))
        repo.add_book(book)
        repo.add_book(book2)
        self.assertEqual([book], list(repo.iter_by_title("asd")))

    def test_iter_by_author(self):
        repo = BookRepo()
        book = Book("asd", Author("asdf"))
        book2 = Book("asd2", Author("asdf2"))
        repo.add_book(book)
        repo.add_book(book2)
        self.assertEqual([book], list(repo.iter_by_author(book.author)))

