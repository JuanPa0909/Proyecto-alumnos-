from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_alumnos, name='listar_alumnos'),
    path('agregar/', views.agregar_alumno, name='agregar_alumno'),
    path('editar/<int:id>/', views.editar_alumno, name='editar_alumno'),
    path('eliminar/<int:id>/', views.eliminar_alumno, name='eliminar_alumno'),
     path('estadisticas/', views.estadisticas_alumnos, name='estadisticas_alumnos'),
]
