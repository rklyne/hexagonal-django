# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import ListView, FormView

from .models import Library
from .forms import CreateLibraryForm


class LibraryList(ListView):
    model = Library


class CreateLibrary(FormView):
    form_class = CreateLibraryForm
    template_name = 'library/library_create.html'
    success_url = reverse_lazy('library-list')

    def form_valid(self, form):
        data = form.cleaned_data
        Library.objects.create(name=data['name'], city_name=data['city_name'])
        messages.info(self.request, "Library record created")
        return super(CreateLibrary, self).form_valid(data)
