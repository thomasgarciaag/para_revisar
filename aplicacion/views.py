from django.shortcuts import render
from django.http import HttpResponse
from aplicacion.models import bd_familiares
from django.template import Template, Context
from django.template import loader

# Create your views here.

def listado_familiares(request):
    familiares = bd_familiares.objects.all()

    datos = {"listado_familiares" : familiares}

    plantilla = loader.get_template("plantilla_primer_url.html")

    documento = plantilla.render(datos)
    
    return HttpResponse(documento) 