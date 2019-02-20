# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views.generic import ListView

from library.models import Library


class LibraryList(ListView):
    model = Library
