from django.forms import forms, fields


class BookSearchForm(forms.Form):
    title = fields.CharField(
        max_length=50, required=False, help_text='Exact title match')
    author = fields.CharField(
        max_length=50, required=False, help_text='Exact author match')
