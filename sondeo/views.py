from typing import ParamSpecArgs
from django.shortcuts import render, redirect
from .models import *
from django.http import HttpResponse
# Create your views here.
from .models import Usuario, Administradores, Certificados, Estado, Respuesta, Sondeos
def inicio (request):
    Son = Sondeos.objects.all()
    Res = Respuesta.objects.all()
    sess = request.session.get('autenticado', False)        
    contexto = {'sondeos': Son, 'respuestas' : Res, 'autenticacion': sess}
    return render(request, "index/sondeos.html", contexto)
#renderizar login
def login (request):
    return render(request, "login/login.html")

#renderizar validar y redirigir usuario
def logear(request):

    try:
        usuar=request.POST['user']  
        pasword=request.POST['pass']
  
        u=Usuario.objects.get(usuario=usuar) 
        if u.contrasena == pasword:
            #creamos la variable de sesion
            request.session['autenticado'] = ["U", u.nombresCompletos, u.idUsuario, u.contrasena, u.sexo, u.etnia, u.municipio]
            return HttpResponse('esta logeado')
        else:
            return HttpResponse('contraseña incorrecta')   
        
    except Usuario.DoesNotExist:
        return HttpResponse('Usuario no registrado')
    except Exception as e:
        return HttpResponse(e)    

def urlAdmin(request):
    return render(request, "login/loginAdmin.html")


def logAdmin(request):

    try:
        usuar=request.POST['user']  
        pasword=request.POST['pass']

        A = Administradores.objects.get(usuario=usuar)
        if A.contrasena == pasword:
            #creamos la variable de sesion
            request.session['autenticado'] = ["A", A.nombreCompleto, A.idAdministrador, A.usuario]
            return redirect('/sondeo')
        else:
            return HttpResponse('contraseña incorrecta')    
    except Administradores.DoesNotExist:
        return HttpResponse('Administrador no existente')
    except Exception as e:
        return HttpResponse(e) 
    
def cerrarSesion(request):
    if request.session['autenticado']:
        del request.session['autenticado']
        request.session.modified = True
    return redirect("../")

def formSondeo(request):
    sess = request.session.get('autenticado', False)
    if request.session.get['autenticado']:
        Son = Sondeos.objects.all()
        Res = Respuesta.objects.all()
        Usu = Usuario.objects.all()        
        contexto = {'sondeos': Son, 'respuestas' : Res, 'usuarios': Usu, 'autenticacion': sess}
        return render(request, "index/sondeos.html", contexto)
    else:
        #un mensaje con la biblioteca de messages
        return HttpResponse(request, "Usted no es administrador")