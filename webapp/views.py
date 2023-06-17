from django.shortcuts import render
from django.http import HttpResponse
from django import render

# Create your views here.
def bienvenido(request):
    return render(request,"bienvenido.html")

def despedida(request):
    return HttpResponse("<h1>Despedida desde Django</h1>")
"""
def contacto(request):
    numeroTelefonico = "Mi numero de contacto es: 809-210-5513 <br>"
    correo = "Email es: natanaelsosa@gmail.com"  
    return HttpResponse(numeroTelefonico+correo)
    
    """