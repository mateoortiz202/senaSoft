from django.shortcuts import render
from .models import *
from django.http import HttpResponse
# Create your views here.
from .models import Usuario, Administradores, Certificados, Estado, Respuesta, Sondeos
def inicio (request):
    Son = Sondeos.objects.all()
    Res = Respuesta.objects.all()
    #del request.session['autenticado']
    sess = request.session.get('autenticado', False)
    contexto = {'sondeos': Son, 'respuestas' : Res, 'autenticacion': sess}
    return render(request, "index.html", contexto)

#renderizar login
def login (request):
    return render(request, "login.html")

#renderizar validar y redirigir usuario
def logear(request):

    try:
        usuar=request.POST['user']  
        pasword=request.POST['pass']

        u=Usuario.objects.get(usuario=usuar)
        if u:
            if u.contrasena == pasword:
                #creamos la variable de sesion
                request.session['autenticado'] = [u.idUsuario, u.contrasena, u.sexo, u.etnia, u.municipio, u.nombresCompletos]
                return HttpResponse('esta logeado')
            else:
                return HttpResponse('contraseña incorrecta')
        print (u)
    except Usuario.DoesNotExist:
        return HttpResponse('Usuario no registrado')
    except Exception as e:
        return HttpResponse(e)    
