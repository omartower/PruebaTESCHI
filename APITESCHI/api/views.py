from django.shortcuts import render
from rest_framework.views import APIView
# Create your views here.
import csv
from django.http import HttpResponse
from .models import Persona
from django import forms

def exportar_personas_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="personas.csv"'

    writer = csv.writer(response)
    writer.writerow(['Nombre', 'Edad', 'Correo'])

    personas = Persona.objects.all()
    for persona in personas:
        writer.writerow([persona.nombre, persona.edad, persona.correo])

    return response

def tabla_personas(request):
    personas = Persona.objects.all()
    
    return render(request, 'personas.html', {'personas': personas})

class PersonaForm(forms.ModelForm):
    class Meta:
        model = Persona
        fields = '__all__'
#AQUI_1

def tabla_personas(request):
    # Crear una lista de objetos Persona manualmente
    personas = [
        Persona(nombre='Nombre1', edad=25, correo='correo1@example.com'),
        Persona(nombre='Nombre2', edad=30, correo='correo2@example.com'),
        # Agregar más personas según sea necesario
    ]

    return render(request, 'personas.html', {'personas': personas})

#AQUI_2
from django.shortcuts import render, redirect

def agregar_persona(request):
    if request.method == 'POST':
        form = PersonaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tabla_personas')
    else:
        form = PersonaForm()

    return render(request, 'agregar_persona.html', {'form': form})


class personas(APIView):
    template_name="personas.html"
    def get(self,request):
        return render(request,self.template_name)


class Home(APIView):
    template_name="index.html"
    def get(self,request):
        return render(request,self.template_name)

class Login_p(APIView):
    template_name="Login_p.html"
    def get(self,request):
        return render(request,self.template_name)
class servicios(APIView):
    template_name="servicios.html"
    def get(self,request):
        return render(request,self.template_name)

class Acerca(APIView):
    template_name="Acerca.html"
    def get(self,request):
        return render(request,self.template_name)
    
#CONECCION DE LA API DJANGO: 

import requests
from django.shortcuts import render
from django.conf import settings

def search_books(request):
    api_key = settings.GOOGLE_BOOKS_API_KEY
    query = request.GET.get('query', '')  
    url = f'https://www.googleapis.com/books/v1/volumes?q={query}&key={api_key}'

    response = requests.get(url)
    data = response.json()

    items = data.get('items', [])

    context = {
        'items': items,
    }

    return render(request, 'search_books.html', context)

#Agregar libros

from django.shortcuts import render, redirect
from .models import Libro
from .forms import LibroForm

from django.shortcuts import render, redirect
from .forms import LibroForm

def agregar_libro(request):
    if request.method == 'POST':
        form = LibroForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = LibroForm()

    return render(request, 'agregar_libro.html', {'form': form})


#lista libros 

from django.shortcuts import render
from .models import Libro

def lista_libros(request):
    libros = Libro.objects.all()
    return render(request, 'lista_libros.html', {'libros': libros})

#editar y eliminar libros 

from django.shortcuts import render, get_object_or_404, redirect
from .models import Libro
from .forms import LibroForm

def lista_libros(request):
    libros = Libro.objects.all()
    return render(request, 'lista_libros.html', {'libros': libros})

def editar_libro(request, libro_id):
    libro = get_object_or_404(Libro, id=libro_id)

    if request.method == 'POST':
        form = LibroForm(request.POST, instance=libro)
        if form.is_valid():
            form.save()
            return redirect('lista_libros')
    else:
        form = LibroForm(instance=libro)

    return render(request, 'editar_libro.html', {'form': form, 'libro': libro})

def eliminar_libro(request, libro_id):
    libro = get_object_or_404(Libro, id=libro_id)

    if request.method == 'POST':
        libro.delete()
        return redirect('lista_libros')

    return render(request, 'eliminar_libro.html', {'libro': libro})

#LOGIN 

from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from .forms import RegistroForm, LoginForm

def registro_usuario(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')  
    else:
        form = RegistroForm()
    return render(request, 'registro.html', {'form': form})

def login_usuario(request):
    if request.method == 'POST':
        form = LoginForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')  
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

#Aqui termina login 

from django.shortcuts import render
from django.views import View
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from django.http import HttpResponseRedirect
from django.urls import reverse

class Login_p(View):
    template_name = 'login_p.html'

    def get(self, request):
        form = AuthenticationForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return HttpResponseRedirect(reverse('index'))  # Redirige a la página principal después del inicio de sesión
        return render(request, self.template_name, {'form': form})
#Autenticacion de Login 
from django.shortcuts import render, redirect
from django.views import View
from .forms import RegistroForm

class RegistroView(View):
    template_name = 'Login_p.html'

    def get(self, request, *args, **kwargs):
        form = RegistroForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()
            # Puedes redirigir a donde quieras después del registro.
            return redirect('index')
        return render(request, self.template_name, {'form': form})