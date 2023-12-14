"""APITESCHI URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from api import views
from django.contrib import admin
from django.urls import path,include
from api.views import Home,Login_p,servicios,Acerca,search_books,personas,tabla_personas,exportar_personas_csv,agregar_libro,lista_libros
from api.views import editar_libro,eliminar_libro,RegistroView,upload_file




urlpatterns = [
    #path('admin/', admin.site.urls),
    path('',Home.as_view(),name='index'),
    path('login_p/', Login_p.as_view(), name='Login_p'),
    path('servicios/',servicios.as_view(),name='servicios'),
    path('Acerca/',Acerca.as_view(),name='Acerca'),
    path('personas/',personas.as_view(),name='personas'),
    path('tabla-personas/', tabla_personas, name='tabla_personas'),
    path('exportar-csv/', exportar_personas_csv, name='exportar_personas_csv'),
    path('search/', search_books, name='search_books'),
    path('admin/', admin.site.urls),
    path('agregar_libro/', agregar_libro, name='agregar_libro'),
    path('lista_libros/', lista_libros, name='lista_libros'),
    path('editar_libro/<int:libro_id>/', editar_libro, name='editar_libro'),
    path('eliminar_libro/<int:libro_id>/', eliminar_libro, name='eliminar_libro'),
    path('registro/', RegistroView.as_view(), name='registro'),  # Cambia RegistroView por la vista real que maneja el registro.
    path('signin/', views.signin,name='signin'),
    path('signup/', views.signup,name='signup'),
    path('logout/',views.signout, name='logout'),
    path('rest/',views.rest, name='rest'),
    path('upload/', upload_file, name='upload_file'),
    path('enviar-contrasena-temporal/<str:correo>/',views.enviar_contrasena_temporal, name='enviar-cotrasena-temporal'),
    path('enviar_correo/<str:nombre>/<str:correo>/<str:apellido>/<str:usuario>/<str:contra>/', views.enviar_correo, name='enviar_correo'),
     
       
    #path('books/', include('APIDJANGOTOWER.urls')),  
         
]

from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)