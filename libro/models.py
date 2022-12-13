from django.db import models

# Create your models here.
def upload_to_images(instance, filename):
    return 'images/{filename}'.format(filename=filename)
def upload_to_pdfs(instance, filename):
    return 'pdf/{filename}'.format(filename=filename)

class Categoria(models.Model):
    nombre = models.CharField(max_length=30)
class Libro(models.Model):
    titulo = models.CharField(max_length=30)
    autor = models.CharField(max_length=30)
    idioma = models.CharField(max_length=20)
    portada = models.ImageField(upload_to=upload_to_images,blank=True)
    descripcion = models.TextField();
    indice = models.TextField();
    file = models.FileField(upload_to=upload_to_pdfs,blank=True)
    categoria_id = models.ForeignKey(Categoria , on_delete=models.CASCADE)

# class NotaPrestamo(models.Model):
#     user_id = models.PositiveBigIntegerField()
# class DetallePrestamo(models.Model):
#     preciototal = models.FloatField()
#     cantidad = models.PositiveIntegerField()
#     notaprestamo_id = models.ForeignKey(NotaPrestamo,on_delete=models.CASCADE)
