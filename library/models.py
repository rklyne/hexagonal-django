# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Library(models.Model):
    name = models.CharField(max_length=500)
    public = models.BooleanField(default=False)
    city_name = models.CharField(max_length=500)
    reference_library = models.BooleanField(default=False)

    @property
    def book_count(self):
        return self.inventory.count()

    @property
    def loaned_book_count(self):
        return self.inventory.filter(on_loan=True).count()


class LibraryOwnedBook(models.Model):
    library = models.ForeignKey(Library, related_name='inventory')
    book = models.ForeignKey('books.Book')
    on_loan = models.BooleanField(default=False)
