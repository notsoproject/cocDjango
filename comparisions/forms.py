# forms.py

from django import forms

class ComparisonForm(forms.Form):
    id1 = forms.CharField(label='ID 1', max_length=100)
    id2 = forms.CharField(label='ID 2', max_length=100)
