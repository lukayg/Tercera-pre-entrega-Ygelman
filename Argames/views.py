from django.template import Template, Context, loader
from  django.http import HttpResponse
import random

from aplicacion.models import *

def saludar(request):
    return HttpResponse("Bienvenido a Argames, su tienda de videjouegos favorita.")

def propuesta(request, nombre, apellido):
    respuesta = f"Ey {apellido} {nombre}, aqui podras encontrar desde los juegos mas viejos hasta los mas recientes!"
    return HttpResponse(respuesta)

def bienvenido_html(request, nombre, apellido):
    respuesta = f""" 
    <html>
    <h1>Bienvenido a Argames, su tienda de videjouegos favorita.
    <h2>Ey {apellido} {nombre}, aqui podras encontrar desde los juegos mas viejos hasta los mas recientes!
    </html>
    """
    return HttpResponse(respuesta)

def bienvenido_template(request):
    miHtml = open("C:/Users/silvi/OneDrive/Escritorio/Tercera Pre-entrega Ygelman/Argames/plantillas/bienvenido.html")
    plantilla = Template(miHtml.read())
    miHtml.close()
    contexto = Context()
    respuesta = plantilla.render(contexto)
    return HttpResponse(respuesta)

def bienvenido_template1(request):
    nombre = "Amadeus"
    apellido = "Mozart"
    juegos = ["Ben 10", "God of War", "Minecraft PS3"]
    contexto = {"nombre": nombre, "apellido": apellido, "juegos": juegos}
    plantilla = loader.get_template("bienvenido1.html")
    respuesta = plantilla.render(contexto)
    return HttpResponse(respuesta) 

def juego_nuevo(request):
    iCantidad = random.randint(20000, 30000)
    sNombre = "Ben 10 " + str(iCantidad)
    juego = Juego(nombre=sNombre, cantidad=iCantidad)
    juego.save()
    respuesta=f"<html><h1>Se guardo {sNombre} con {iCantidad} de copias en el inventario."
    return HttpResponse(respuesta)
