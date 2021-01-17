from django import forms
from django.utils.translation import gettext_lazy as _

class CityForm(forms.Form):
    city = forms.CharField(label=_('Enter a city'), max_length=200)
