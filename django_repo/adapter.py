from itertools import imap

from .models import Book as DjangoBook, Author as DjangoAuthor
from model.entities.author import Author
from model.entities.book import Book
from model.interfaces.book_repo import BookRepoInterface


def _model_to_entity(book_model):
    authors = {}

    def get_author(model_author):
        assert model_author.id
        if model_author.id not in authors:
            authors[model_author.id] = Author(
                name=model_author.title,
                website=model_author.website,
            )
        return authors[model_author.id]
    return Book(
        title=book_model.title,
        author=get_author(book_model.author),
        published=book_model.published,
        isbn=book_model.isbn,
    )


class BookRepo(BookRepoInterface):
    def iter_by_title(self, title):
        queryset = DjangoBook.objects.filter(title=title)
        return imap(_model_to_entity, queryset.iterator())

    def iter_by_author(self, author):
        queryset = DjangoBook.objects.filter(author__title=author.name)
        return imap(_model_to_entity, queryset.iterator())

    def iter_all(self):
        queryset = DjangoBook.objects.all()
        return imap(_model_to_entity, queryset.iterator())

    def count(self):
        return DjangoBook.objects.count()

    def add_book(self, book):
        author, _ = DjangoAuthor.objects.get_or_create(
            title=book.author.name,
            defaults={
                'website': book.author.website,
            }
        )
        DjangoBook.objects.create(
            title=book.title,
            author=author,
            isbn=book.isbn,
            published=book.published,
        )
