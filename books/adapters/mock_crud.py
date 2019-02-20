from ..interfaces.crud import CrudInterface, CrudError


class MockCrud(CrudInterface):
    def __init__(self):
        self.store = {}

    def create(self, one):
        if one.id in self.store:
            raise CrudError("Already exists")
        self.store[one.id] = one

    def update(self, one):
        if one.id not in self.store:
            raise CrudError("Does not exist")
        self.store[one.id] = one

    def delete(self, one):
        if one.id not in self.store:
            raise CrudError("Does not exist")
        del self.store[one.id]

    def get(self, uuid):
        try:
            return self.store[uuid]
        except KeyError:
            raise CrudError("Does not exist")

    def count(self):
        return len(self.store)
