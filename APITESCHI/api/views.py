from django.shortcuts import render
from rest_framework.views import APIView
# Create your views here.
import csv
from django.http import HttpResponse
from .models import Persona
from django import forms

#prueba
from django.shortcuts import render, redirect
from rest_framework.views import APIView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
import secrets
import string 
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.http import HttpResponse
from django.shortcuts import render
from django.conf import settings
#aqui termina 

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

#INICIO DE SESION:

from django.shortcuts import render
from django.http import HttpResponse

def upload_file(request):
    # Tu implementación de la función
    return HttpResponse("Upload File View")


def signup(request):
    if request.method =='GET':
        return render(request, 'signup.html',{
            'form' : UserCreationForm
        })
    else:
            try:
                user = User.objects.create_user(first_name=request.POST['first_name'], email=request.POST['email'], last_name=request.POST['last_name'], username=request.POST['username'], password=request.POST['password'])
                user.save()
                nombre = request.POST['first_name']
                correo = request.POST['email']
                apellido = request.POST['last_name']
                usuario = request.POST['username']
                contra = request.POST['password']
                return redirect('enviar_correo', nombre=nombre, correo=correo, apellido=apellido, usuario=usuario, contra=contra)
                                
            except IntegrityError:
                return render(request, 'signup.html',{
                    'form' : UserCreationForm,
                    "mensaje" : 'Username already exist'
                })
                #return HttpResponse('Username already exist')
        #return HttpResponse('Password do not match')
        
def signout(request):
    logout(request)
    return redirect('signin')


def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html', {
            'form': AuthenticationForm
        })
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'signin.html', {
                'form': AuthenticationForm,
                'error': 'Usuario o contraseña incorrecta'
            })
        else:
            login(request, user)
            return render(request, 'index.html')

def enviar_correo(request, nombre, correo, apellido, usuario, contra):
    subject = 'Bienvenido'
    from_email = 'omarcitob13b13@gmail.com'
    recipient_list = [correo]

    # Renderiza la plantilla HTML con el contexto
    contexto = {'nombre': nombre,
                'correo': correo,
                'apellido': apellido,
                'usuario': usuario,
                "contra": contra}
    contenido_correo = render_to_string('enviar_correo.html', contexto)

    # Envía el correo
    send_mail(subject, '', from_email, recipient_list, html_message=contenido_correo)
    #ventana reseteo de contraseña
    return redirect('signin')

class forgotpas(APIView):
    def get(self,request):
        return
    
def rest(request):
    return render(request, 'rest.html')


#codigo reseteo contraseña
def generar_contrasena_temporal(length=10):
    caracteres=string.ascii_letters + string.digits
    contraseña_temporal=''.join(secrets.choice(caracteres)for i in range(length))
    return contraseña_temporal

# Método que manda web
def web():
    print("Bienvenidos")

#envio de correos
def enviar_contrasena_temporal(request, username):
    usuario = usuario.objects.get(username=username)  # Recupera el usuario por su nombre de usuario

    # Genera una contraseña temporal
    contrasena_temporal = generar_contrasena_temporal()

    # Asigna la contraseña temporal al usuario
    usuario.set_password(contrasena_temporal)
    usuario.save()

    # Envía un correo electrónico con la contraseña temporal
    subject = 'Contraseña temporal'
    message = f'Tu contraseña temporal es: {contrasena_temporal}'
    from_email = 'omarcitob13b13@gmail.com'
    recipient_list = [usuario.email]

    send_mail(subject, message, from_email, recipient_list)

    return render(request,'enviar_correo.html')


    
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