# conta/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
#from django.contrib.auth.models import User
from acesso.models import Usuario

class CadastroUsuarioForm(UserCreationForm):
    email = forms.EmailField(required=True, label='Email Institucional')
    nickname = forms.CharField(required=True, label='Apelido')

    class Meta:
        model = Usuario
        fields = ('nickname', 'email', 'password1', 'password2')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email.endswith('@uemg.br'):
            raise forms.ValidationError("Por favor, utilize um email institucional da UEMG.")
        return email

    def save(self, commit=True):
        user = super().save(commit=False)
        user.username = self.cleaned_data['email']
        user.first_name = self.cleaned_data['nickname']
        if commit:
            user.save()
        return user
