from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import gettext_lazy as _


class LoginForm(AuthenticationForm):
    username = forms.CharField(label=False,
                           widget=forms.TextInput(attrs={'class':'form-control rounded-left','placeholder':"Username"}),
                           max_length=100,
                           required=True,
                           localize=True,
                           disabled=False,
                           help_text="")
    password = forms.CharField(label=False,
                           widget=forms.PasswordInput(attrs={'class':'form-control rounded-left','placeholder':"Password"}),
                           max_length=20,
                           required=True,
                           localize=True,
                           disabled=False,
                           help_text="")

