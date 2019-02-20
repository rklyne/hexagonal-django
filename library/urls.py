from django.conf.urls import url

from .views import LibraryList


urlpatterns = [
    url(r'^', LibraryList.as_view()),
]
