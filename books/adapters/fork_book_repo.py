import attr

from ..interfaces.book_repo import BookRepoInterface


@attr.s
class ForkRepo(BookRepoInterface):
    main_repo = attr.ib()
    other_repo = attr.ib()

    def add_book(self, book):
        self.main_repo.add_book(book)
        self.other_repo.add_book(book)

    def iter_by_title(self, title):
        # TODO: Could iterate both and assert equivalence?
        return self.main_repo.iter_by_title(title)

    # TODO: ... Incomplete, but you get the idea
