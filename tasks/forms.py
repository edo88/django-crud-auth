from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import Task, Solicitud, User

class LoginForm(forms.Form):
    email = forms.CharField(
        widget= forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )

class SignUpForm(UserCreationForm):
    email = forms.CharField(
        widget= forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    mobile = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    adress = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    class Meta:
        model = User
        fields =('email', 'password1', 'password2', 'first_name', 'last_name',
                     'mobile', 'adress', 'is_admin', 'is_ejecutivo', 'is_cliente')

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['nombre', 'categoria', 'subcategoria', 'complejidad']

class SolicitudForm(forms.ModelForm):

    class Meta:
        model = Solicitud
        fields = ['comentario','requerimiento']
