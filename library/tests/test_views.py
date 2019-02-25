from django.test import TestCase
from django.test.client import RequestFactory
from ..models import Library
from ..views import LibraryList, LibraryCreate, LibraryBookAdd
from books.models import Book, Author


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
        view = LibraryCreate.as_view()
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


class TestBookAddView(TestCase):
    def test_get(self):
        author = Author.objects.create(name='author1')
        book = Book.objects.create(title='asdasd', published=False, author=author)
        view = LibraryBookAdd.as_view()
        request = RequestFactory().get('/library/add-book/2')
        response = view(request, book_id=book.id)
        self.assertTrue(response)
        self.assertContains(response, 'value="Save"')

    def test_post(self):
        author = Author.objects.create(name='author1')
        book = Book.objects.create(title='asdasd', published=False, author=author)
        library = Library.objects.create(name='lib1', city_name='city1')
        response = self.client.post(
            '/library/add-book/{}'.format(book.id),
            data={'quantity': 3, 'library': library.id})
        self.assertEquals(302, response.status_code, response)
        self.assertEqual(3, library.book_count)
