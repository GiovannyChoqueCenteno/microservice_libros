from rest_framework import serializers
from .models import Categoria, Libro, NotaPrestamo, DetallePrestamo


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'

class LibroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Libro
        fields = '__all__'
class NotaPrestamoSerializer(serializers.ModelSerializer):
    class Meta:
        model = NotaPrestamo
        fields = '__all__'
class DetallePrestamoSerializer(serializers.ModelSerializer):
    class Meta :
        model = DetallePrestamo
        fields = '__all__'