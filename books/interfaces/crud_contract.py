from unittest import TestCase

from .crud import BasicDatum, CrudError


def contract_test(
        crud_repo_generator,
        item_generator=BasicDatum,
        test_attribute='test_value',
        test_class=TestCase):
    class ContractTest(test_class):
        def test_create_one(self):
            instance = crud_repo_generator()
            instance.create(item_generator())
            self.assertEqual(1, instance.count())

        def test_create_returns_id(self):
            instance = crud_repo_generator()
            thing = item_generator()
            thing_id = instance.create(thing)
            thing2 = instance.get(thing_id)
            self.assertEqual(thing, thing2)

        def test_create_duplicate(self):
            instance = crud_repo_generator()
            thing = item_generator()
            instance.create(thing)
            with self.assertRaises(CrudError):
                instance.create(thing)

        def test_delete(self):
            instance = crud_repo_generator()
            thing = item_generator()
            instance.create(thing)
            instance.delete(thing)
            self.assertEqual(0, instance.count())

        def test_delete_missing(self):
            instance = crud_repo_generator()
            thing = item_generator()
            with self.assertRaises(CrudError):
                instance.delete(thing)

        def test_get(self):
            instance = crud_repo_generator()
            thing = item_generator()
            instance.create(thing)
            thing2 = instance.get(thing.id)
            self.assertEqual(thing, thing2)

        def test_get_missing(self):
            instance = crud_repo_generator()
            thing = item_generator()
            with self.assertRaises(CrudError):
                instance.get(thing.id)

        def test_update(self):
            instance = crud_repo_generator()
            thing = item_generator()
            instance.create(thing)
            thing2 = item_generator(id=thing.id)
            setattr(thing, test_attribute, 'A')
            setattr(thing2, test_attribute, 'B')
            instance.update(thing2)
            actual = instance.get(thing.id)
            self.assertEqual(
                getattr(thing2, test_attribute),
                getattr(actual, test_attribute))

        def test_update_missing(self):
            instance = crud_repo_generator()
            thing = item_generator()
            with self.assertRaises(CrudError):
                instance.update(thing)

    return ContractTest
