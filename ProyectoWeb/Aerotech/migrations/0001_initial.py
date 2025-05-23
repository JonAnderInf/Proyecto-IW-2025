# Generated by Django 5.2 on 2025-04-26 11:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dni', models.CharField(max_length=9, unique=True)),
                ('nombre', models.CharField(max_length=100)),
                ('apellidos', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=254)),
                ('telefono', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Equipo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_serie', models.CharField(max_length=100, unique=True)),
                ('modelo', models.CharField(max_length=100)),
                ('marca', models.CharField(max_length=100)),
                ('tipo', models.CharField(max_length=100)),
                ('fecha_adquisicion', models.DateField()),
                ('fecha_puesta_marcha', models.DateField()),
                ('proveedor_nombre', models.CharField(max_length=100)),
                ('proveedor_telefono', models.CharField(max_length=15)),
                ('planta', models.CharField(max_length=100)),
                ('empleados', models.ManyToManyField(related_name='equipos_asignados', to='Aerotech.empleado')),
            ],
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('referencia', models.CharField(max_length=100, unique=True)),
                ('titulo', models.CharField(max_length=200)),
                ('descripcion', models.TextField()),
                ('fecha_apertura', models.DateField(auto_now_add=True)),
                ('fecha_resolucion', models.DateField(blank=True, null=True)),
                ('urgencia', models.CharField(choices=[('alta', 'Alta'), ('media', 'Media'), ('baja', 'Baja')], max_length=10)),
                ('tipo', models.CharField(choices=[('averia', 'Avería'), ('mejora', 'Mejora'), ('mantenimiento', 'Mantenimiento')], max_length=15)),
                ('estado', models.CharField(choices=[('abierto', 'Abierto'), ('cerrado', 'Cerrado')], max_length=10)),
                ('empleado_asignado', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Aerotech.empleado')),
                ('equipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Aerotech.equipo')),
            ],
        ),
    ]
