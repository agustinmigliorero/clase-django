from django.urls import path
from . import views

urlpatterns = [
    path("", views.Tareas),
    path("<int:proyecto_id>", views.TareasDetalle),
]
