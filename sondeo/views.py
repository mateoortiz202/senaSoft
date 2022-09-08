import random
from django.shortcuts import render, redirect
from .models import *
from django.http import HttpResponse
import datetime

# Create your views here.
from .models import Usuario, Administradores, Certificados, Respuesta, Sondeos
def convertirFechas(fecha):
    año = (((int(fecha[0])*1000)+(int(fecha[1])*100)+(int(fecha[2])*10) + (int(fecha[3]))))
    mes= (((int(fecha[5]*10)) +(int(fecha[6]))))
    dia = (((int(fecha[8])*10) + (int(fecha[9]))))
    
    
        
        
        
    return True





def inicio (request):
    h=datetime.datetime.now()
    Son = Sondeos.objects.all()
    Res = Respuesta.objects.all()
    sess = request.session.get('autenticado', False)        
    contexto = {'sondeos': Son, 'respuestas' : Res, 'autenticacion': sess, 'fechaToday': h}
    return render(request, "index/sondeos.html", contexto)
#renderizar login

def listarCerti(request):
    usuario = request.session.get('autenticado', False)
    respuestas = Respuesta.objects.filter(idUsuario=usuario[2])
    certificados = []
    for i in respuestas:
        certificados.append(i.idCertificados)
    #for i in certificados:
    #    print(type(i))
    
    contexto = {'respuestas': respuestas, 'certificados' : certificados}
    return render(request, "index/listarCertificados.html", contexto)
    

def traerRes(request, pk):
    
    son = Sondeos.objects.get(idSondeos=pk)
    Res = Respuesta.objects.filter(idSondeo=pk)
    if request.session.get('autenticado'):
        usuario = request.session.get('autenticado')
        contestar = True
        for i in Res:
            print(usuario[2])
            #confilcto con la id de administradores y usuarios
            if i.idUsuario.idUsuario == usuario[2]:
                contestar = False
                contexto = {'respuestas' : Res, 'sondeos':son, 'contestar':contestar}
                print(contestar)
                return render(request, "index/respuestas.html", contexto)
            
        if contestar == True:
            if usuario[0] == "A":
                contestar = False
                contexto = {'respuestas' : Res, 'sondeos':son, 'contestar':contestar}
                return render(request, "index/respuestas.html", contexto)
            else:
                contexto = {'respuestas' : Res, 'sondeos':son, 'contestar':contestar}
                print (contestar)
                return render(request, "index/respuestas.html", contexto)
    else:
        contexto = {'respuestas' : Res, 'sondeos':son}
        return render(request, "index/respuestas.html", contexto) 
     
    
    
        
    

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
            return redirect('/sondeo')
        else:
            return HttpResponse('contraseña incorrecta')   
        
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

            u=Usuario.objects.create(nombresCompletos=nomComple,tipoDocumento=tDocumento,numeroDocumento=nDocumento,sexo=sex,telefonoCelular=telCel,telefonoFijo=telFijo,correo=email,municipio=municip,direccion=dir,barrio_vereda=dirVB,fechaNacimiento=fechaN,etnia=eTnia,condicionDiscapacidad=discapacidad,estractoRecidencial=estracto,nivelEducativo=nEducativo,dispositivo=Pispositivo,tipoDispositivo=tDispositvo,conectividad=conecti,tipoAfiliacion=tAfiliacion,usuario=user,contrasena=passw)

            u.save()

            return redirect('/sondeo/login')

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


def urlSondeo(request):
    return render(request, "formularios/formSondeos.html")
    

def guardarSondeo(request):
    if request.method == 'POST':
        try:
            admin = request.POST['administrador']
            asunto = request.POST['asunto']
            descripcion = request.POST['descripcion']
            habilitado = request.POST['habilitado']
            grupoPoblacional = request.POST['gp']
            comuna = request.POST['comuna']
            barrio = request.POST['barrio']
            imagen = request.POST['imagen']
            edadMinima = request.POST['edadMinima']
            edadMaxima = request.POST['edadMaxima']
            tematica = request.POST['tematica']
            fechaPublicacion = request.POST['fechaPublicacion']
            fechaFinPublicacion = request.POST['fechaFinPublicacion']
            obligatorio = request.POST['obligatorio']
            
            u = Sondeos.objects.create(
                idAdmin = Administradores.objects.get(pk=admin),
                asunto = asunto,
                descripcion = descripcion,
                habilitado = habilitado,
                grupoPoblacional = grupoPoblacional,
                comuna = comuna,
                barrio = barrio,
                imagen = imagen, 
                edadMinima = edadMinima,
                edadMaxima = edadMaxima,
                tematica = tematica,
                fechaPublicacion = fechaPublicacion,
                fechaFinPublicacion = fechaFinPublicacion,
                obligatorio = obligatorio
            )
            u.save()     
            
            return redirect("../")
            #un mensaje con la biblioteca de messages   
            
        except Exception as e:
                return HttpResponse(f'error: {e}')
            
            
def guardarRespuesta(request):
    #generera pdf 
    
    
    if request.method == 'POST':
        try:
            
            
            
            idUsuario = request.POST['usuario']
            respuesta = request.POST['respuesta']
            idSondeo = request.POST['idSondeo']
            us=Usuario.objects.get(idUsuario=idUsuario)

            #controlar caso
            radicado2 = str(random.randint(100000,999999))
                           
            certi = Certificados.objects.create(
                radicado = radicado2 
            )
            certi.save()    
            var = Certificados.objects.filter(radicado = radicado2)
            print(var[0].idCertificado)
            
            u = Respuesta.objects.create(
                
                idCertificados = Certificados.objects.get(pk=var[0].idCertificado),
                idSondeo = Sondeos.objects.get(pk=idSondeo),
                idUsuario = Usuario.objects.get(pk=idUsuario),
                respuesta = respuesta   
            )
            u.save()
            return render(request, 'formularios/certificado.html',{'user':us ,'radicado':radicado2})
        except Exception as e:
            return HttpResponse(f'error: {e}')
        return redirect('../')
    else:
        return HttpResponse("No hay datos, no entraste por donde debias")