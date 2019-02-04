import attr


class SearchService(object):
    class SearchException(Exception):
        pass

    class NoResults(SearchException):
        pass

    class MultipleResults(SearchException):
        pass

    def _one_from_iterator(self, iterator):
        try:
            return iterator.next()
        except StopIteration:
            raise self.NoResults
        finally:
            try:
                iterator.next()
            except StopIteration:
                pass
            else:
                raise self.MultipleResults


@attr.s
class BookSearchService(SearchService):
    book_repo = attr.ib()

    def get_by_title(self, title):
        books = self.book_repo.iter_by_title(title=title)
        return self._one_from_iterator(books)

    def list_by_author(self, author):
        return self.book_repo.iter_by_author(author)

    def all(self):
        return self.book_repo.iter_all()

    def get_count(self):
        return self.book_repo.count()
