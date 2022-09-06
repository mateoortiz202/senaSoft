from django.db import models

# Create your models here.
#creamos las clases que se utilizaran en nuestro projecto

class Usuario(models.Model):
    idUsuario = models.AutoField(primary_key=True)
    nombresCompletos = models.CharField(max_length=100)
    tD = (
        ('ti', 'Tarjeta de identidad'),
        ('cc', 'Cedula de Ciudadania'),
        ('ce', 'Cedula de Extranjeria'),
    )
    tipoDocumetno = models.CharField(max_length=2, choices=tD)
    numeroDocumento = models.CharField(max_length=100)
    sx = (
        ('M', 'Masculino'),
        ('F', 'Femenino'),
    )
    sexo = models.CharField(max_length=2, choices=sx)
    telefonoCelular = models.IntegerField()
    telefonoFijo = models.IntegerField()
    correo = models.CharField(max_length=100)
    municipio = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    barrio_vereda = models.CharField(max_length=100, default="Fatima")
    fechaNacimiento = models.DateField()
    
    et =(
        ("A","afro"),
        ("P","palenque"),
        ('ng','ninguno'),
    )
    etnia = models.CharField(max_length=2, choices=et)
    condicionDiscapacidad = models.CharField(max_length=100, default="ninguna")
    estractoRecidencial = models.IntegerField()
    nivelEducativo= models.CharField(max_length=100)
    #dp = dispositivo
    dp = (
        ('s', 'si'),
        ('n', 'no'),
    )
    dispositivo = models.CharField(max_length=2, choices=dp, default="si")
    #cdp = cual dispositivo
    cdp = (
        ('TM', 'T. movil'),
        ('c', 'Computador'),
        ('Tb','Tablet'),
        ('Ot','Otro')
    )
    tipoDispositivo = models.CharField(max_length=2, choices=cdp, default="TM")
    #conectividad
    cn = (
        ('s', 'si'),
        ('n', 'no'),
    )
    conectividad = models.CharField(max_length=2, choices=cn, default="s")
    #TA = tipo de afiliacion
    TA = (
        ('Sd', 'Subsidiado'),
        ('Ct', 'contributivo'),
    )
    tipoAfiliacion = models.CharField(max_length=2, choices=TA, default="Sd")
    usuario = models.CharField(max_length=100)
    contrasena = models.CharField(max_length=100)
    
    def __str__(self) -> str:
        return str(self.nombresCompletos)
    
class Estado(models.Model):

    #filtro
    fl=(
        ("A","afro"),
        ("P","palenque"),
        ("H","hombres"),
        ("M","Mujeres"),
        ("MY","Mayores"),
        ("T","todos"),
    )
    filtro = models.CharField(max_length=100,choices=fl,default='T')


    def __str__(self) -> str:
        return self.filtro
    
class Administradores(models.Model):

    idAdministrador = models.IntegerField(primary_key=True)
    nombreCompleto = models.CharField(max_length=100)
    usuario = models.CharField(max_length=100)
    contrasena = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.nombreCompleto

class Certificados(models.Model):
    fechaGeneracion = models.DateTimeField(auto_now_add=True)
    radicao = models.CharField(max_length=255, null=True)

    def __str__(self) -> str:
        return str(self.fechaGeneracion)

    
class Sondeos(models.Model):
    idSondeos = models.AutoField(primary_key=True)
    idAdmin = models.ForeignKey(Administradores, on_delete= models.CASCADE)
    asunto = models.CharField(max_length=100)
    descripcion = models.TextField()
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE)
    imagen = models.CharField(max_length=100)
    edadMinima = models.CharField(max_length=3)
    tematica = models.CharField(max_length=100)
    #publico = models., ----no tiene funcion
    fechaPublicacion = models.DateTimeField()
    fechaFinPublicacion = models.DateTimeField()
    fechaCreacion = models.DateTimeField(auto_now_add=True)
    #ob = obligatorio
    ob = (
        ('s', 'si'),
        ('n', 'no'),
    )
    obligatorio = models.CharField(max_length=2, choices=ob, default="n")
    
    def __str__(self) -> str:
        return str(self.idSondeos)
    
class Respuesta(models.Model):

    estado= models.BooleanField()
    fecha=models.DateTimeField(auto_now_add=True)
    idCertificados=models.ForeignKey(Certificados,on_delete=models.CASCADE)
    idSondeo=models.ForeignKey(Sondeos, on_delete=models.CASCADE)
    idUsuario=models.ForeignKey(Usuario, on_delete=models.CASCADE)
    respuesta = models.TextField()
    
    def __str__(self) -> str:
        return str(self.fecha)  
