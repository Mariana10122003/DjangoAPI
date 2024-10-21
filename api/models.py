from django.db import models

# Create your models here.
class Generos(models.Model):
    genero_id = models.AutoField(primary_key=True)
    tipo_genero = models.CharField(max_length=255)
    
    class Meta:
        db_table = "generos"
        
        
class Usuarios(models.Model):
    Usuarios_id = models.AutoField(primary_key=True)
    nombre_completo = models.CharField(max_length=255)
    
    class Meta:
        db_table = "usuarios"
        