from django import forms
from datetime import date

class DiaryForm(forms.Form):
    date = forms.DateField(initial=date.today())
    content = forms.CharField(widget=forms.Textarea())