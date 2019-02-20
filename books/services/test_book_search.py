from unittest import TestCase

from ..adapters.mock_book_repo import BookRepo
from ..entities.author import Author
from ..entities.book import Book
from .book_search import BookSearchService


class TestBookSearch(TestCase):
    def setUp(self):
        self.repo = BookRepo()
        self.book = Book(
            "title",
            author=Author("author name"),
        )
        self.repo.add_book(self.book)
        self.book2 = Book(
            "title2",
            author=Author("author name"),
        )
        self.repo.add_book(self.book2)
        self.author2_book = Book(
            "title3",
            author=Author("author2 name"),
        )
        self.repo.add_book(self.author2_book)

    def test_book_get_by_name(self):
        search_service = BookSearchService(self.repo)
        book = search_service.get_by_title("title")
        self.assertEqual(self.book, book)

    def test_book_get_by_name_missing(self):
        search_service = BookSearchService(self.repo)
        with self.assertRaises(BookSearchService.NoResults):
            search_service.get_by_title("title missing")

    def test_list_by_author(self):
        search_service = BookSearchService(self.repo)
        books = search_service.list_by_author(Author("author name"))
        self.assertEqual([self.book, self.book2], list(books))

    def test_count(self):
        search_service = BookSearchService(self.repo)
        self.assertEqual(3, search_service.get_count())
