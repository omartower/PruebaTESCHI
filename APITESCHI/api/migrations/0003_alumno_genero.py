# Generated by Django 3.2.4 on 2023-11-21 23:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_registro_usuario'),
    ]

    operations = [
        migrations.CreateModel(
            name='Genero',
            fields=[
                ('idGenero', models.AutoField(db_column='idGenero', primary_key=True, serialize=False)),
                ('tipoGenero', models.TextField(db_column='tipoGenero')),
            ],
            options={
                'db_table': 'Generos',
            },
        ),
        migrations.CreateModel(
            name='Alumno',
            fields=[
                ('idAlumno', models.IntegerField(db_column='idAlumno', primary_key=True, serialize=False)),
                ('nameAlumno', models.CharField(db_column='nameAlumno', max_length=100)),
                ('fk_genero', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.genero')),
            ],
            options={
                'db_table': 'Alumnos',
            },
        ),
    ]
