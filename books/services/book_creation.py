import attr

from ..interfaces.book_repo import BookRepoError, BookRepoInterface


class BookNotificationInterface(object):
    pass


@attr.s
class CreateBookCommand(object):
    book_repo = attr.ib(
        validator=attr.validators.instance_of(BookRepoInterface))
    notifications = attr.ib(
        validator=attr.validators.optional(
            attr.validators.instance_of(BookNotificationInterface)))

    def add_book(self, book):
        # Imagine that there are twenty of these rules
        if book.published and book.author.has_middle_name():
            raise BookRepoError(
                "Authors with middle names cnanot publish books")
        self.book_repo.add_book(book)
        if self.notifications:
            self.notifications.book_added(book)
