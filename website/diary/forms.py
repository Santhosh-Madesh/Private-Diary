from django import forms
from datetime import date

class DiaryForm(forms.Form):
    date = forms.DateField(initial=date.today())
    content = forms.CharField(widget=forms.Textarea())

class SignupForm(forms.Form):
    username = forms.CharField(max_length=150)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())

class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput())

class ChangePasswordForm(forms.Form):
    username = forms.CharField(max_length=150)
    current_password = forms.CharField(widget=forms.PasswordInput())
    new_password = forms.CharField(widget=forms.PasswordInput())
    confirm_new_password = forms.CharField(widget=forms.PasswordInput())
