from unittest import TestCase

from .crud import BasicDatum, CrudError


def contract_test(crud_repo_generator, base_class=TestCase):
    class ContractTest(base_class):
        def test_create_one(self):
            instance = crud_repo_generator()
            instance.create(BasicDatum())
            self.assertEqual(1, instance.count())

        def test_create_returns_id(self):
            instance = crud_repo_generator()
            thing = BasicDatum()
            thing_id = instance.create(thing)
            thing2 = instance.get(thing_id)
            self.assertEqual(thing, thing2)

        def test_create_duplicate(self):
            instance = crud_repo_generator()
            thing = BasicDatum()
            instance.create(thing)
            with self.assertRaises(CrudError):
                instance.create(thing)

        def test_delete(self):
            instance = crud_repo_generator()
            thing = BasicDatum()
            instance.create(thing)
            instance.delete(thing)
            self.assertEqual(0, instance.count())

        def test_delete_missing(self):
            instance = crud_repo_generator()
            thing = BasicDatum()
            with self.assertRaises(CrudError):
                instance.delete(thing)

        def test_get(self):
            instance = crud_repo_generator()
            thing = BasicDatum()
            instance.create(thing)
            thing2 = instance.get(thing.id)
            self.assertEqual(thing, thing2)

        def test_get_missing(self):
            instance = crud_repo_generator()
            thing = BasicDatum()
            with self.assertRaises(CrudError):
                instance.get(thing.id)

        def test_update(self):
            instance = crud_repo_generator()
            thing = BasicDatum()
            instance.create(thing)
            thing2 = BasicDatum(id=thing.id)
            thing.test_value = 100
            thing2.test_value = 200
            instance.update(thing2)
            actual = instance.get(thing.id)
            self.assertEqual(thing2.test_value, actual.test_value)

        def test_update_missing(self):
            instance = crud_repo_generator()
            thing = BasicDatum()
            with self.assertRaises(CrudError):
                instance.update(thing)

    return ContractTest
