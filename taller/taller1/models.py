from django.db import models

class Genero(models.Model):
    id_genero = models.AutoField(db_column='idGenero', primary_key=True)
    genero = models.CharField(max_length=20, blank=False, null=False)
    
    def __str__(self):
        return self.genero

class Usuario(models.Model):
    rut = models.CharField(primary_key=True, max_length=10)
    nombre = models.CharField(max_length=20)
    apellido_paterno = models.CharField(max_length=20)
    apellido_materno = models.CharField(max_length=20)
    fecha_nacimiento = models.DateField(blank=False, null=False)
    id_genero = models.ForeignKey(Genero, on_delete=models.CASCADE, db_column='idGenero')
    telefono = models.CharField(max_length=45)
    email = models.EmailField(unique=True, max_length=100, blank=True, null=True)

    def __str__(self):
        return self.rut
    
class Servicio(models.Model):
    id_servicio =  models.CharField(primary_key=True, max_length=10)
    nombre_serv =  models.CharField(max_length=20)
    precio = models.CharField(max_length=11)
    plazo_entrega = models.CharField(max_length=20)
    descripcion_servicio = models.CharField(max_length=500)

    def __str__(self):
        return self.id_servicio

    


   