from unittest import TestCase

from ..entities.author import Author
from ..entities.book import Book


def contract_test(repo_generator):
    class BookRepoInterfaceContract(TestCase):
        def test_create_repo(self):
            repo = repo_generator()
            self.assertTrue(repo)

        def test_add_book(self):
            repo = repo_generator()
            book = Book("asd", Author("asd"))
            repo.add_book(book)
            self.assertEqual(1, repo.count())

        def test_iter_all(self):
            repo = repo_generator()
            book = Book("asd", Author("asdf"))
            book2 = Book("asd2", Author("asdf2"))
            repo.add_book(book)
            repo.add_book(book2)
            self.assertEqual([book, book2], list(repo.iter_all()))

        def test_iter_by_title(self):
            repo = repo_generator()
            book = Book("asd", Author("asdf"))
            book2 = Book("asd2", Author("asdf2"))
            repo.add_book(book)
            repo.add_book(book2)
            self.assertEqual([book], list(repo.iter_by_title("asd")))

        def test_iter_by_author(self):
            repo = repo_generator()
            book = Book("asd", Author("asdf"))
            book2 = Book("asd2", Author("asdf2"))
            repo.add_book(book)
            repo.add_book(book2)
            self.assertEqual([book], list(repo.iter_by_author(book.author)))

    return BookRepoInterfaceContract
