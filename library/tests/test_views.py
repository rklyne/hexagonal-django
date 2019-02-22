from django.test import TestCase
from django.test.client import RequestFactory
from ..models import Library
from ..views import LibraryList, CreateLibrary


class TestListView(TestCase):
    def test_get(self):
        Library.objects.create(name='asd123')
        view = LibraryList.as_view()
        request = RequestFactory().get('/library')
        response = view(request)
        self.assertTrue(response)
        self.assertContains(response, 'asd123')


class TestCreateView(TestCase):
    def test_get(self):
        view = CreateLibrary.as_view()
        request = RequestFactory().get('/library')
        response = view(request)
        self.assertTrue(response)
        self.assertContains(response, 'value="Save"')

    def test_post(self):
        response = self.client.post(
            '/library/new',
            data={'name': 'asd', 'city_name': 'asdasd'})
        self.assertEquals(302, response.status_code)
        self.assertEqual('asdasd', Library.objects.get(name='asd').city_name)
