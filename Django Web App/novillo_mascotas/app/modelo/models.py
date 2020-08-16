from django.db import models

# Create your models here.
class Cliente (models.Model):
    cliente_id = models.AutoField(primary_key = True)
    cedula = models.CharField(max_length=10, null = False, unique = True)
    nombres = models.CharField(max_length=70, null = False)
    apellidos = models.CharField(max_length=70, null = False)
    celular = models.CharField(max_length=15, null = False)
    email = models.EmailField(max_length=100, null = False)

    def __str__(self):
        return self.cedula

class Mascota (models.Model):
    mascota_id = models.AutoField(primary_key = True)
    nombre = models.CharField(max_length=70, null = False)
    raza = models.CharField(max_length=70, null = False)
    altura = models.CharField(max_length=70, null = False)
    tipo = models.CharField(max_length=70, null = False)
    cliente = models.ForeignKey(Cliente, on_delete = models.CASCADE)

    def __str__(self):
        cadena =str(self.nombre) + ";" + str(self.tipo) + ";"+ str(self.raza)+ ";" + str(self.mascota_id)
        return cadena

class Turno (models.Model):
    turno_id = models.AutoField(primary_key = True)
    descripcion = models.TextField(default='descripción del turno')
    responsable = models.CharField(max_length = 100, null = False)
    fecha = models.DateTimeField(auto_now_add = True, null = False)
    mascota = models.ForeignKey(Mascota, on_delete = models.CASCADE)

    def __str__(self):
        return self.turno_id
