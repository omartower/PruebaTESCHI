from django import forms
from .models import Libro

class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = ['Nombre_Libro', 'Autor', 'Edicion', 'Editorial', 'Imagen']