from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from persona.models import Persona

def bienvenido(request):
    no_personas = Persona.objects.count()
    return render(request,"bienvenido.html",{'no_personas':no_personas})

    
