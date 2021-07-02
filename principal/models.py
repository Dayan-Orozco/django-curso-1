from django.db import models

class Persona(models.Model):
    id_persona = models.AutoField(primary_key=True) #django añade la llave primaria (no es necesario añadirlo)
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=120)
    correo = models.EmailField(max_length=200, unique=True) #unique es para validar que ese correo no puede estar repetido en la base de datos

    def __str__(self):
        return self.nombre +" "+ self.apellidos
