import attr


@attr.s
class BasicDatum(object):
    id = attr.ib(default=None)


class CrudError(Exception):
    pass


class NotFoundError(CrudError):
    pass


class CrudInterface(object):
    def create(self, one):
        """
        Adds a book to the repo.
        If not possible, raises a BookRepoError
        """
        raise NotImplementedError

    def update(self, one):
        raise NotImplementedError

    def delete(self, one):
        raise NotImplementedError

    def get(self, uuid):
        raise NotImplementedError

    def count(self):
        raise NotImplementedError
