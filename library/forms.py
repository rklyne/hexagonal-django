from django import forms

from .models import Library


class LibraryCreateForm(forms.Form):
    name = forms.CharField(max_length=500)
    city_name = forms.CharField(max_length=500)


class LibraryBookAddForm(forms.Form):
    library = forms.ModelChoiceField(Library.objects.all())
    quantity = forms.IntegerField(min_value=1)
