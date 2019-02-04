# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import messages
from django.views.generic.base import TemplateView

from .app import app
from .entities.author import Author
from .forms import BookSearchForm
from services.book_search import BookSearchService


class Index(TemplateView):

    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super(Index, self).get_context_data(**kwargs)

        context['book_count'] = app.book_search.get_count()
        context['search_form'] = BookSearchForm()
        context['titles'] = [book.title for book in app.book_search.all()]
        return context

    def post(self, request):
        form = BookSearchForm(request.POST)
        if not form.is_valid():
            return self.get(request)
        data = form.cleaned_data
        if 'title' in data:
            try:
                books = [app.book_search.get_by_title(data['title'])]
            except app.book_search.NoResults:
                messages.warning(request, "book not found")
                return self.get(request)
        else:
            books = app.book_search.list_by_author(Author(name=data['author']))
        return self.render_to_response('list.html', {'books': books})
