from django.urls import path

from  .views import  CategoriaViewSet,LibroViewSet

urlpatterns = [
    path('categoria',CategoriaViewSet.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path('categoria/<str:pk>', CategoriaViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'
    })),
    path('libro', LibroViewSet.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path('libro/<str:pk>', LibroViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'
    })),

]