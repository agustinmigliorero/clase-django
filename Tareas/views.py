from django.shortcuts import render, HttpResponse
from django.template import loader

from .models import Proyecto, Item

# Create your views here.


def Tareas(request):
    proyectos = Proyecto.objects.order_by("id")
    plantilla = loader.get_template("index.html")
    context = {"proyectos": proyectos}
    return HttpResponse(plantilla.render(context, request))


def TareasDetalle(request, proyecto_id):
    proyecto = Proyecto.objects.get(id=proyecto_id)
    items = Item.objects.filter(proyecto=proyecto)
    plantilla = loader.get_template("proyecto.html")
    context = {"proyecto": proyecto, "items": items}
    return HttpResponse(plantilla.render(context, request))
