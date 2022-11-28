from rest_framework import viewsets, status
from rest_framework.response import Response

from libro.models import Categoria, Libro, NotaPrestamo, DetallePrestamo
from libro.serializers import CategoriaSerializer, LibroSerializer, NotaPrestamoSerializer, DetallePrestamoSerializer


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
        serializer = LibroSerializer(libros,many=True)
        return Response(serializer.data)
    def create(self,request):
        serializer =LibroSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    def retrieve(self,request,pk=None):
        libro = Libro.objects.get(id=pk)
        serializer = LibroSerializer(libro)
        return Response(serializer.data)
    def update(self,request , pk=None):
        libro = Libro.objects.get(id=pk)
        serializer = LibroSerializer(instance=libro ,data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
    def destroy(self,request,pk=None):
        libro = Libro.objects.get(id=pk)
        libro.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class NotaPrestamoViewSet(viewsets.ViewSet):
    def list(self,request):
        notaprestamos = NotaPrestamo.objects.all()
        serializer = NotaPrestamoSerializer(notaprestamos,many=True)
        return Response(serializer.data)
    def create(self,request):
        serializer =NotaPrestamoSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    def retrieve(self,request,pk=None):
        notaprestamo = NotaPrestamo.objects.get(id=pk)
        serializer = NotaPrestamoSerializer(notaprestamo)
        return Response(serializer.data)
    def update(self,request , pk=None):
        notaprestamo = NotaPrestamo.objects.get(id=pk)
        serializer = NotaPrestamoSerializer(instance=notaprestamo ,data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
    def destroy(self,request,pk=None):
        notaprestamo = NotaPrestamo.objects.get(id=pk)
        notaprestamo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class DetallePrestamoViewSet(viewsets.ViewSet):
    def list(self,request):
        detalleprestamos = DetallePrestamo.objects.all()
        serializer = DetallePrestamoSerializer(detalleprestamos,many=True)
        return Response(serializer.data)
    def create(self,request):
        serializer =DetallePrestamoSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    def retrieve(self,request,pk=None):
        detalleprestamo = DetallePrestamo.objects.get(id=pk)
        serializer = DetallePrestamoSerializer(detalleprestamo)
        return Response(serializer.data)
    def update(self,request , pk=None):
        detalleprestamo = DetallePrestamo.objects.get(id=pk)
        serializer = DetallePrestamoSerializer(instance=detalleprestamo ,data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
    def destroy(self,request,pk=None):
        detalleprestamo = DetallePrestamo.objects.get(id=pk)
        detalleprestamo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)