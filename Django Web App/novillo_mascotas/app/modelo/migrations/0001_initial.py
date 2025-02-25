# Generated by Django 3.0.7 on 2020-08-15 16:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('cliente_id', models.AutoField(primary_key=True, serialize=False)),
                ('cedula', models.CharField(max_length=10, unique=True)),
                ('nombres', models.CharField(max_length=70)),
                ('apellidos', models.CharField(max_length=70)),
                ('celular', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Mascota',
            fields=[
                ('mascota_id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=70)),
                ('raza', models.CharField(max_length=70)),
                ('altura', models.CharField(max_length=70)),
                ('tipo', models.CharField(max_length=70)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='modelo.Cliente')),
            ],
        ),
        migrations.CreateModel(
            name='Turno',
            fields=[
                ('turno_id', models.AutoField(primary_key=True, serialize=False)),
                ('descripcion', models.TextField(default='descripción del turno')),
                ('responsable', models.CharField(max_length=100)),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('mascota', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='modelo.Mascota')),
            ],
        ),
    ]
