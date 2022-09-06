from django.shortcuts import render
from .models import *
from django.http import HttpResponse
# Create your views here.
from .models import Usuario, Administradores, Certificados, Estado, Respuesta, Sondeos
def inicio (request):
    Son = Sondeos.objects.all()
    Res = Respuesta.objects.all()
    contexto = {'sondeos': Son, 'respuestas' : Res}
    return render(request, "index.html", contexto)

#renderizar login
def login (request):
    return render(request, "login.html")

#renderizar validar y redirigir usuario
def logear(request):

    try:
        usuar=request.POST['user']
        pasword=request.POST['pass']

        u=Usuario.objects.filter(usuario=usuar,contrasena=pasword)
        print (u)
        if u:
            return HttpResponse('esta logeado')
        else:
            return HttpResponse(' no esta logeado')
        

    except Exception as e:
        return HttpResponse(e)    
