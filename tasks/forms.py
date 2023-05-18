from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import Categoria, Task, Solicitud, User, Subcategoria

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
    is_admin = forms.BooleanField(required=False)
    is_ejecutivo = forms.BooleanField(required=False)
    is_cliente = forms.BooleanField(required=False)

    class Meta:
        model = User
        fields =('email', 'password1', 'password2', 'first_name', 'last_name',
                     'mobile', 'adress', 'is_admin', 'is_ejecutivo', 'is_cliente')


class TaskForm(forms.ModelForm):
    categoria = forms.ModelChoiceField(queryset=Categoria.objects.all(), widget=forms.Select(attrs={'id': 'id_categoria', 'data-url': '/obtener_subcategorias/'}))

    class Meta:
        model = Task
        fields = ['nombre', 'categoria', 'subcategoria', 'complejidad']

class SolicitudForm(forms.ModelForm):

    class Meta:
        model = Solicitud
        fields = ['comentario','requerimiento']
