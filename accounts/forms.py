from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    nome = forms.CharField(max_length=30, required=True)
    sobrenome = forms.CharField(max_length=30, required=True)
    profissão = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(max_length=254)

    class Meta:
        model = User
        fields = ('username', 'nome', 'sobrenome', 'profissão', 'email', 'password1', 'password2',)

