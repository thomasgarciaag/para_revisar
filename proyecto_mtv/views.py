from django.http import HttpResponse
from django.template import Template, Context




def vista_primer_url(request):

    archivo = open(r"D:\Escritorio\python\mtv2\proyecto_mtv\proyecto_mtv\templates\plantilla_primer_url.html") 

    #Creamos el objeto plantilla
    plantilla=Template(archivo.read())  

    archivo.close()

   # listado_alumnos = ["Thomas Garcia", "Leonel Gareis"]

   # datos = {"tecnologia": "python", "listado_alumnos": listado_alumnos}

   # contexto = Context(datos)
    contexto = Context()

    documento = plantilla.render(contexto)

    return HttpResponse(documento)    


