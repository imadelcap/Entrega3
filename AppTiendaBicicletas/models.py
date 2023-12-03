from django.db import models

# Modelos necesarios para el stock de la tienda de bicicletas

class Cliente(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    email = models.EmailField()
    edad = models.IntegerField()

    def __str__(self):
        return 'Cliente: ' + self.nombre + self.apellido + ' - ' + self.email + ' - edad =' + self.edad
    
class ModeloBicicleta(models.Model):
    marca = models.CharField(max_length=20)
    tipo = models.CharField(max_length=30)
    rodado = models.IntegerField()

    def __str__(self):
        return 'Bicicleta: ' + self.marca + ' - ' + self.tipo + ' - rodado ' + self.rodado

class Accesorio(models.Model):
    tipo = models.CharField(max_length=20) 
    marca = models.CharField(max_length=20)
    descripcion = models.TextField(max_length=100)
    
    def __str__(self):
        return 'Accesorio: ' + self.tipo + ' - ' + self.marca + ' - ' + self.descripcion

