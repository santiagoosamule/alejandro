from django.db import models

# Create your models here.

class Post(models.Model):
    titulo = models.CharField(max_length=40)
    descripcion = models.TextField()
    imagen=models.ImageField(upload_to="photos",blank=True)
    precio=models.FloatField(default=True)
    author = models.ForeignKey("auth.User", 
        on_delete = models.CASCADE,blank=True),

    class Meta:
        verbose_name_plural = "Publicaciones"

    def __str__(self):
        return self.titulo


class Personas(models.Model):

    imagen=models.ImageField(upload_to="photos",blank= True)
    nombre=models.CharField(max_length=50)
    descripcion=models.CharField(max_length=200)

    class Meta:
        verbose_name_plural="personal"

    def __str__(self):
        return self.nombre