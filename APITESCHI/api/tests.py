from django.test import TestCase

#from .models import Genero, Alumno

# Create your tests here.
import unittest
from .models import Persona


class PersonaTestCase(TestCase):

    def setUp(self):
        # Configurar datos de prueba
        Persona.objects.create(nombre="Ruben", edad=25, correo="Ruben@example.com")
        Persona.objects.create(nombre="Ricardo", edad=30, correo="Ricardo@example.com")

    def test_persona_nombre(self):
        # Obtener instancias de personas
        persona1 = Persona.objects.get(nombre="Ruben")
        persona2 = Persona.objects.get(nombre="Ricardo")

        # Verificar si los nombres son correctos
        self.assertEqual(persona1.nombre, "Ruben")
        self.assertEqual(persona2.nombre, "Ricardo")

    def test_persona_edad(self):
        # Obtener instancias de personas
        persona1 = Persona.objects.get(nombre="Ruben")
        persona2 = Persona.objects.get(nombre="Ricardo")

        # Verificar si las edades son correctas
        self.assertEqual(persona1.edad, 25)
        self.assertEqual(persona2.edad, 30)

    def test_persona_correo(self):
        # Obtener instancias de personas
        persona1 = Persona.objects.get(nombre="Ruben")
        persona2 = Persona.objects.get(nombre="Ricardo")

        # Verificar si los correos son correctos
        self.assertEqual(persona1.correo, "Ruben@example.com")
        self.assertEqual(persona2.correo, "Ricardo@example.com")