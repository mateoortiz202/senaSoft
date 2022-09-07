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
    return render(request, "index/index.html", contexto)

#renderizar login
def login (request):
    return render(request, "login/login.html")

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

def registrarUsuario (request):

    usuarios=Usuario.objects.all()
    

    return render(request,'login/registrar.html',{'context': usuarios})  


def registrarU(request):

    if request.method == 'POST':

        try:
            
            nomComple=request.POST['nombres_completos']
            tDocumento=request.POST['tipo_documento']
            nDocumento=request.POST['numero_documento']
            sex=request.POST['sexo_']
            telCel=request.POST['telefono_celular']
            telFijo=request.POST['telefono_fijo']
            email=request.POST['correo']
            municip=request.POST['municipio_']
            dir=request.POST['direccion_']
            dirVB=request.POST['barrio_vereda']
            fechaN=request.POST['fecha_nacimiento']
            eTnia=request.POST['etnia']
            discapacidad=request.POST['condicion_discapacidad']
            estracto=request.POST['estracto_residencial']
            nEducativo=request.POST['nivel_educativo']
            Pispositivo=request.POST['dispositivo_pregunta']
            tDispositvo=request.POST['dispositivo_']
            conecti=request.POST['conectividad_']
            tAfiliacion=request.POST['tipo_afiliacion']
            user=request.POST['usu']
            passw=request.POST['pass']

            u=Usuario.objects.create(nombresCompletos=nomComple,tipoDocumetno=tDocumento,numeroDocumento=nDocumento,sexo=sex,telefonoCelular=telCel,telefonoFijo=telFijo,correo=email,municipio=municip,direccion=dir,barrio_vereda=dirVB,fechaNacimiento=fechaN,etnia=eTnia,condicionDiscapacidad=discapacidad,estractoRecidencial=estracto,nivelEducativo=nEducativo,dispositivo=Pispositivo,tipoDispositivo=tDispositvo,conectividad=conecti,tipoAfiliacion=tAfiliacion,usuario=user,contrasena=passw)

            u.save()

            return HttpResponse("se agrego")

        except Exception as e:

            return HttpResponse(e)    
