from django import forms
from django.contrib.auth.models import User
from app_basica.models import InfoPerfilUsuario

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta():
        model = User
        fields = ('username','email','password')

class InfoPerfilUsuarioForm(forms.ModelForm):
    class Meta():
        model = InfoPerfilUsuario
        fields = ('portfolio_site','profile_pic')
