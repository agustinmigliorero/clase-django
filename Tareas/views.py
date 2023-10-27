from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.http import JsonResponse
from django.template import loader

from .models import Proyecto, Item

# Create your views here.


def Proyectos(request):
    proyectos = Proyecto.objects.order_by("id")
    plantilla = loader.get_template("index.html")
    context = {"proyectos": proyectos}
    return HttpResponse(plantilla.render(context, request))


def ProyectoDetalle(request, proyecto_id):
    proyecto = Proyecto.objects.get(id=proyecto_id)
    items = Item.objects.filter(proyecto=proyecto)
    plantilla = loader.get_template("proyecto.html")
    context = {"proyecto": proyecto, "items": items}
    return HttpResponse(plantilla.render(context, request))


def CrearProyecto(request):
    if request.method == "POST":
        nombre = request.POST.get("nombre")
        Proyecto.objects.create(nombre=nombre)
        return HttpResponseRedirect("/proyectos")
    context = {"safe": True}
    return render(request, "crear-proyecto.html", context)


def BorrarProyecto(request, proyecto_id):
    if request.method == "DELETE":
        proyecto = Proyecto.objects.get(id=proyecto_id)
        proyecto.delete()
        return JsonResponse({"success": True})
    return HttpResponse("ERROR, ESTO SOLO ACEPTA METODOS DELETE")


def CrearItem(request, proyecto_id):
    if request.method == "POST":
        nombre = request.POST.get("nombre")
        descripcion = request.POST.get("descripcion")
        proyecto = Proyecto.objects.get(id=proyecto_id)
        Item.objects.create(proyecto=proyecto, nombre=nombre, descripcion=descripcion)
        return HttpResponseRedirect(f"/proyectos/{proyecto_id}")
    return HttpResponse("ERROR, ESTO SOLO ACEPTA METODOS POST")
