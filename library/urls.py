from django.conf.urls import url

from .views import LibraryList, CreateLibrary


urlpatterns = [
    url(r'^new', CreateLibrary.as_view(), name='library-create'),
    url(r'^', LibraryList.as_view(), name='library-list'),
]
