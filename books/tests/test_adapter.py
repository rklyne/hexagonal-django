from __future__ import absolute_import, unicode_literals

from django.test import TestCase

from ..adapters.django import BookRepo
from ..interfaces.book_repo_contract import contract_test


class TestDjangoBookRepo(contract_test(BookRepo, test_class=TestCase)):
    pass
