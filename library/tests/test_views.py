from django.test import TestCase
from django.test.client import RequestFactory
from ..models import Library
from ..views import LibraryList


class TestListView(TestCase):
    def test_get(self):
        Library.objects.create(name='asd123')
        view = LibraryList.as_view()
        request = RequestFactory().get('/library')
        response = view(request)
        self.assertTrue(response)
        self.assertContains(response, 'asd123')
