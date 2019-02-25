from django.conf.urls import url

from .views import LibraryList, LibraryCreate, LibraryBookAdd


urlpatterns = [
    url(r'^new', LibraryCreate.as_view(), name='library-create'),
    url(r'^add-book/(?P<book_id>.+)', LibraryBookAdd.as_view(), name='library-book-add'),
    url(r'^', LibraryList.as_view(), name='library-list'),
]
