try:
    # Python 2.6
    from itertools import imap
except ImportError:
    # Python 3+
    imap = map

from ..models import Book as DjangoBook, Author as DjangoAuthor
from ..entities.author import Author
from ..entities.book import Book
from ..interfaces.book_repo import BookRepoInterface


def _model_to_entity(book_model):
    authors = {}

    def get_author(model_author):
        assert model_author.id
        if model_author.id not in authors:
            authors[model_author.id] = Author(
                name=model_author.name or model_author.title,
                website=model_author.website,
            )
        return authors[model_author.id]
    return Book(
        title=book_model.title,
        author=get_author(book_model.author),
        published=book_model.published,
        isbn=book_model.isbn,
    )


def get_or_create_author_by_name(author):
    author, _ = DjangoAuthor.objects.get_or_create(
        title=author.name,
        defaults={
            'website': author.website,
        }
    )
    author.name = author.title
    author.save(update_fields=['name'])
    return author


class BookRepo(BookRepoInterface):
    def iter_by_title(self, title):
        queryset = DjangoBook.objects.filter(title=title)
        return imap(_model_to_entity, queryset.iterator())

    def iter_by_author(self, author):
        queryset = DjangoBook.objects.filter(author__name=author.name)
        return imap(_model_to_entity, queryset.iterator())

    def iter_all(self):
        queryset = DjangoBook.objects.all()
        return imap(_model_to_entity, queryset.iterator())

    def count(self):
        return DjangoBook.objects.count()

    def add_book(self, book):
        author = get_or_create_author_by_name(book.author)
        DjangoBook.objects.create(
            title=book.title,
            author=author,
            isbn=book.isbn,
            published=book.published,
        )
