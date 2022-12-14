from rest_framework import viewsets, status
from rest_framework.response import Response

from libro.models import Categoria, Libro
from libro.serializers import CategoriaSerializer, LibroGetSerializer,LibroPostSerializer


class CategoriaViewSet(viewsets.ViewSet):
    def list(self,request):
        categorias = Categoria.objects.all()
        serializer = CategoriaSerializer(categorias,many=True)

        return Response(serializer.data)
    def create(self,request):
        serializer =CategoriaSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    def retrieve(self,request,pk=None):
        categoria = Categoria.objects.get(id=pk)
        serializer = CategoriaSerializer(categoria)
        return Response(serializer.data)
    def update(self,request , pk=None):
        categoria = Categoria.objects.get(id=pk)
        serializer = CategoriaSerializer(instance=categoria,data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
    def destroy(self,request,pk=None):
        categoria = Categoria.objects.get(id=pk)
        categoria.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
# Create your views here.

class LibroViewSet(viewsets.ViewSet):
    def list(self,request):
        libros = Libro.objects.all()
        search = self.request.query_params.get('search')
        categoria_id = self.request.query_params.get('categoria_id')
        if search is not None:
            libros = libros.filter(titulo__icontains=search)
        if categoria_id is not None:
            libros = libros.filter(categoria_id=categoria_id)
        serializer = LibroGetSerializer(libros,many=True)
        return Response(serializer.data)
    def create(self,request):
        serializer =LibroPostSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    def retrieve(self,request,pk=None):
        libro = Libro.objects.get(id=pk)
        serializer = LibroGetSerializer(libro)
        return Response(serializer.data)
    def update(self,request , pk=None):
        libro = Libro.objects.get(id=pk)
        serializer = LibroPostSerializer(instance=libro ,data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
    def destroy(self,request,pk=None):
        libro = Libro.objects.get(id=pk)
        libro.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

