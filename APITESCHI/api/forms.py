from django import forms
from .models import Libro

class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = ['Nombre_Libro', 'Autor', 'Edicion', 'Editorial', 'Imagen']

#Login 

from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Usuario

class RegistroForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ['nombre', 'email', 'telefono', 'username', 'password1', 'password2']

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import Usuario

class LoginForm(AuthenticationForm):
    class Meta:
        model = Usuario
        fields = ['username', 'password']