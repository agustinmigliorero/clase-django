from django.urls import path
from . import views

urlpatterns = [
    path("", views.Proyectos),
    path("<int:proyecto_id>", views.ProyectoDetalle),
    path("crear-proyecto/", views.CrearProyecto),
    path("borrar-proyecto/<int:proyecto_id>", views.BorrarProyecto),
    path("crear-item/<int:proyecto_id>", views.CrearItem),
]
