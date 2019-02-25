# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import ListView, FormView

from books.models import Book
from .models import Library, LibraryOwnedBook
from .forms import LibraryCreateForm, LibraryBookAddForm


class LibraryList(ListView):
    model = Library


class LibraryCreate(FormView):
    form_class = LibraryCreateForm
    template_name = 'library/library_create.html'
    success_url = reverse_lazy('library-list')

    def form_valid(self, form):
        data = form.cleaned_data
        Library.objects.create(name=data['name'], city_name=data['city_name'])
        messages.info(self.request, "Library record created")
        return super(LibraryCreate, self).form_valid(data)


class LibraryBookAdd(FormView):
    form_class = LibraryBookAddForm
    template_name = 'library/library_book_add.html'
    success_url = reverse_lazy('library-list')

    def get_context_data(self, **kwargs):
        context = super(LibraryBookAdd, self).get_context_data(**kwargs)
        context['book'] = Book.objects.get(id=self.kwargs['book_id'])
        return context

    def form_valid(self, form):
        data = form.cleaned_data
        book_id = self.kwargs['book_id']
        book = Book.objects.get(id=book_id)
        library = data['library']
        for _ in range(data['quantity']):
            LibraryOwnedBook.objects.create(
                library=library, book=book)
        messages.info(self.request, "Library record created")
        return super(LibraryBookAdd, self).form_valid(data)
