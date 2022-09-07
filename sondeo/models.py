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
    tipoDocumento = models.CharField(max_length=2, choices=tD)
    numeroDocumento = models.CharField(max_length=100)
    sx = (
        ('M', 'Masculino'),
        ('F', 'Femenino'),
        ('I', 'Intersexual'),
        ('IN', 'Indefinido'),
        ('P', 'Prefieren no decir'),
    )   
    sexo = models.CharField(max_length=2, choices=sx)
    telefonoCelular = models.IntegerField()
    telefonoFijo = models.IntegerField()
    correo = models.CharField(max_length=100)
    municipio = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    barrio_vereda = models.CharField(max_length=100, default="Fatima")
    fechaNacimiento = models.DateField()
    
   
    etnia = models.CharField(max_length=100, default="ninguno")
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
    tipoDispositivo = models.CharField(max_length=100, choices=cdp, default="TM")
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
    # hb=habilitado o no
    hb = (
        ('s', 'si'),
        ('n', 'no'),        
    )
    habilitado = models.CharField(max_length=2, choices=hb, default="n")
    grupoPoblacional = models.CharField(max_length=100)
    comuna = models.CharField(max_length=100)
    barrio = models.CharField(max_length=100)
    imagen = models.CharField(max_length=100)
    edadMinima = models.IntegerField(default=0)
    edadMaxima = models.IntegerField(default=0)
    tematica = models.CharField(max_length=100)
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
