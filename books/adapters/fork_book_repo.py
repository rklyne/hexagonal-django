import attr

from ..interfaces.book_repo import BookRepoInterface


@attr.s
class ForkRepo(BookRepoInterface):
    main_repo = attr.ib()
    other_repo = attr.ib()

    def add_book(self, book):
        the_id = self.main_repo.add_book(book)
        book.id = the_id
        self.other_repo.add_book(book)
        return the_id

    create = add_book

    def iter_by_title(self, title):
        # TODO: Could iterate both and assert equivalence?
        return self.main_repo.iter_by_title(title)

    def count(self):
        count = self.main_repo.count()
        assert count == self.other_repo.count()
        return count

    def iter_by_author(self, author):
        return self.main_repo.iter_by_author(author)

    def iter_all(self):
        return self.main_repo.iter_all()

    def get(self, uuid):
        return self.main_repo.get(uuid)

    def delete(self, one):
        self.main_repo.delete(one)
        self.other_repo.delete(one)

    def update(self, one):
        self.main_repo.update(one)
        self.other_repo.update(one)
