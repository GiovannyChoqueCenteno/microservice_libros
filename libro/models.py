from django.db import models

# Create your models here.
def upload_to(instance, filename):
    return 'images/{filename}'.format(filename=filename)

class Categoria(models.Model):
    nombre = models.CharField(max_length=30)
class Libro(models.Model):
    titulo = models.CharField(max_length=30)
    autor = models.CharField(max_length=30)
    precio = models.FloatField()
    idioma = models.CharField(max_length=20)
    portada = models.ImageField(upload_to=upload_to,blank=True)
    file = models.ImageField()
    categoria_id = models.ForeignKey(Categoria , on_delete=models.CASCADE)

# class NotaPrestamo(models.Model):
#     user_id = models.PositiveBigIntegerField()
# class DetallePrestamo(models.Model):
#     preciototal = models.FloatField()
#     cantidad = models.PositiveIntegerField()
#     notaprestamo_id = models.ForeignKey(NotaPrestamo,on_delete=models.CASCADE)
