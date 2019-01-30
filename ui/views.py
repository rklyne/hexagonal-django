# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views.generic.base import TemplateView

from django_books.app import app
from model.services.book_search import BookSearchService


class Index(TemplateView):

    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super(Index, self).get_context_data(**kwargs)

        context['titles'] = [book.title for book in app.book_search.all()]
        return context
