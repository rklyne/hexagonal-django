# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic.base import TemplateView

from django_repo.adapter import BookRepo

from model.services.book_search import BookSearchService

# Create your views here.

def get_repo():
    return BookRepo()


class Index(TemplateView):

    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super(Index, self).get_context_data(**kwargs)

        repo = get_repo()
        service = BookSearchService(repo)
        context['titles'] = [book.title for book in service.all()]
        return context
