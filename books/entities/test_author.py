from unittest import TestCase

from ..entities.author import Author


class TestAuthor(TestCase):
    def test_middle_name_one_name(self):
        author = Author(name="banana")
        self.assertFalse(author.has_middle_name())

    def test_middle_name_two_names(self):
        author = Author(name="banana apple")
        self.assertFalse(author.has_middle_name())

    def test_middle_name_three_names(self):
        author = Author(name="banana apple pear")
        self.assertTrue(author.has_middle_name())
