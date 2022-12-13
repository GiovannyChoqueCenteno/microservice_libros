from rest_framework import serializers
from .models import Categoria, Libro


class CategoriaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Categoria
        fields = '__all__'

class LibroGetSerializer(serializers.ModelSerializer):

    class Meta:
        model = Libro
        fields = '__all__'
        depth=1


class LibroPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Libro
        fields = '__all__'
