from django import forms
from datetime import date
from django.forms import ModelForm
from .models import Profile

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

class DashboardForm(forms.Form):
    age = forms.IntegerField()
    instagram_id = forms.CharField()
    bio = forms.CharField(widget=forms.Textarea())

class DashboardUpdateForm(forms.Form):
    username = forms.CharField()
    email = forms.EmailField()
    age = forms.IntegerField()
    bio = forms.CharField(widget=forms.Textarea())

class ProfileModelForm(ModelForm):
    class Meta:
        model = Profile
        fields = ["pfp","age","instagram_id","bio"]
        
