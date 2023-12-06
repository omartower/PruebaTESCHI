from django.db import models


# Create your models here.

class Genero(models.Model):
    idGenero = models.AutoField(primary_key=True, db_column='idGenero')
    tipoGenero = models.TextField(db_column='tipoGenero')
    
    class Meta:
        db_table = 'Generos'

class Alumno(models.Model):
    idAlumno = models.IntegerField(primary_key=True, db_column='idAlumno')
    nameAlumno = models.CharField(max_length=100, db_column='nameAlumno')
    fk_genero = models.ForeignKey(Genero, on_delete=models.CASCADE)  # Agrega on_delete aquí
        
    class Meta:
        db_table = 'Alumnos'

#Base de personas

class Persona(models.Model):
   nombre = models.CharField(max_length=100)
   edad = models.PositiveIntegerField()
   correo = models.EmailField()

   def __str__(self):
    return self.nombre
    
#Base de datos Login

class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    contraseña = models.CharField(max_length=100)

class Registro(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    fecha_registro = models.DateTimeField(auto_now_add=True)

#Base para agregar libros 
from django.db import models

class Libro(models.Model):
    Nombre_Libro = models.CharField(max_length=255)
    Autor = models.CharField(max_length=255)
    Edicion = models.CharField(max_length=50)
    Editorial = models.CharField(max_length=100)
    Imagen = models.ImageField(upload_to='libros_imagenes/', null=True, blank=True)

    def __str__(self):
        return self.Nombre_Libro


            
