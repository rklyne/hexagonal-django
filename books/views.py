# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import messages
from django.shortcuts import render_to_response
from django.views.generic.base import TemplateView

from .app import app
from .entities.author import Author
from .entities.book import Book
from .forms import BookSearchForm


def create_dummy_data():
    repo = app._books
    book = Book("asd", Author("asdf"))
    book2 = Book("asd2", Author("asdf"))
    author2_book = Book("asdf", Author("asdf2"))
    repo.add_book(book)
    repo.add_book(book2)
    repo.add_book(author2_book)


class Index(TemplateView):

    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super(Index, self).get_context_data(**kwargs)

        context['book_count'] = app.book_search.get_count()
        context['search_form'] = BookSearchForm()
        context['titles'] = [book.title for book in app.book_search.all()]
        return context

    def post(self, request):
        if 'populate' in request.POST:
            create_dummy_data()
            messages.info(request, "dummy books created")
            return self.get(request)
        form = BookSearchForm(request.POST)
        if not form.is_valid():
            return self.get(request)
        data = form.cleaned_data
        if data['title']:
            try:
                books = [app.book_search.get_by_title(data['title'])]
            except app.book_search.NoResults:
                messages.warning(request, "book not found")
                return self.get(request)
        elif 'all' in request.POST:
            books = app.book_search.all()
        else:
            books = app.book_search.list_by_author(Author(name=data['author']))
        return render_list_view(request, books)


def render_list_view(request, books):
    return render_to_response('list.html', {'books': list(books)})


class List(TemplateView):
    template_name = 'list.html'
