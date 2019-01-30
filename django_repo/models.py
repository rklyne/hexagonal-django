# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Author(models.Model):
    title = models.TextField()
    website = models.TextField(blank=True, null=True)


class Book(models.Model):
    title = models.TextField()
    author = models.ForeignKey(Author)
    isbn = models.TextField(blank=True, null=True)
    published = models.BooleanField()
