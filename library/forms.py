from django import forms


class CreateLibraryForm(forms.Form):
    name = forms.CharField(max_length=500)
    city_name = forms.CharField(max_length=500)
