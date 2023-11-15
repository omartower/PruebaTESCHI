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
    query = request.GET.get('query', 'Django')  # Puedes cambiar 'Django' por cualquier consulta que desees
    url = f'https://www.googleapis.com/books/v1/volumes?q={query}&key={api_key}'

    response = requests.get(url)
    data = response.json()

    items = data.get('items', [])

    context = {
        'items': items,
    }

    return render(request, 'books/search_books.html', context)