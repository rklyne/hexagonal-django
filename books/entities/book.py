import attr

from .author import Author


@attr.s
class Book(object):
    title = attr.ib(type=unicode)
    author = attr.ib(validator=attr.validators.instance_of(Author))
    isbn = attr.ib(default=None)
    published = attr.ib(default=False, type=bool, cmp=False)

    def has_isbn(self):
        return bool(self.isbn)
