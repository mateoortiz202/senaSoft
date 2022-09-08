# Generated by Django 4.0.6 on 2022-09-08 16:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Administradores',
            fields=[
                ('idAdministrador', models.IntegerField(primary_key=True, serialize=False)),
                ('nombreCompleto', models.CharField(max_length=100)),
                ('usuario', models.CharField(max_length=100)),
                ('contrasena', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Certificados',
            fields=[
                ('idCertificado', models.AutoField(primary_key=True, serialize=False)),
                ('fechaGeneracion', models.DateTimeField(auto_now_add=True)),
                ('radicado', models.CharField(max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('idUsuario', models.AutoField(primary_key=True, serialize=False)),
                ('nombresCompletos', models.CharField(max_length=100)),
                ('tipoDocumento', models.CharField(choices=[('ti', 'Tarjeta de identidad'), ('cc', 'Cedula de Ciudadania'), ('ce', 'Cedula de Extranjeria')], max_length=2)),
                ('numeroDocumento', models.CharField(max_length=100)),
                ('sexo', models.CharField(choices=[('M', 'Masculino'), ('F', 'Femenino'), ('I', 'Intersexual'), ('IN', 'Indefinido'), ('P', 'Prefieren no decir')], max_length=2)),
                ('telefonoCelular', models.IntegerField()),
                ('telefonoFijo', models.IntegerField()),
                ('correo', models.CharField(max_length=100)),
                ('municipio', models.CharField(max_length=100)),
                ('direccion', models.CharField(max_length=100)),
                ('barrio_vereda', models.CharField(default='Fatima', max_length=100)),
                ('fechaNacimiento', models.DateField()),
                ('etnia', models.CharField(default='ninguno', max_length=100)),
                ('condicionDiscapacidad', models.CharField(default='ninguna', max_length=100)),
                ('estractoRecidencial', models.IntegerField()),
                ('nivelEducativo', models.CharField(max_length=100)),
                ('dispositivo', models.CharField(choices=[('s', 'si'), ('n', 'no')], default='si', max_length=2)),
                ('tipoDispositivo', models.CharField(choices=[('TM', 'T. movil'), ('c', 'Computador'), ('Tb', 'Tablet'), ('Ot', 'Otro')], default='TM', max_length=100)),
                ('conectividad', models.CharField(choices=[('s', 'si'), ('n', 'no')], default='s', max_length=2)),
                ('tipoAfiliacion', models.CharField(choices=[('Sd', 'Subsidiado'), ('Ct', 'contributivo')], default='Sd', max_length=2)),
                ('usuario', models.CharField(max_length=100)),
                ('contrasena', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Sondeos',
            fields=[
                ('idSondeos', models.AutoField(primary_key=True, serialize=False)),
                ('asunto', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
                ('habilitado', models.CharField(choices=[('s', 'si'), ('n', 'no')], default='n', max_length=2)),
                ('grupoPoblacional', models.CharField(max_length=100)),
                ('comuna', models.CharField(max_length=100)),
                ('barrio', models.CharField(max_length=100)),
                ('imagen', models.CharField(max_length=100)),
                ('edadMinima', models.IntegerField(default=0)),
                ('edadMaxima', models.IntegerField(default=0)),
                ('tematica', models.CharField(max_length=100)),
                ('fechaPublicacion', models.DateField()),
                ('fechaFinPublicacion', models.DateField()),
                ('fechaCreacion', models.DateTimeField(auto_now_add=True)),
                ('obligatorio', models.CharField(choices=[('s', 'si'), ('n', 'no')], default='n', max_length=2)),
                ('idAdmin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sondeo.administradores')),
            ],
        ),
        migrations.CreateModel(
            name='Respuesta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('respuesta', models.TextField()),
                ('idCertificados', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sondeo.certificados')),
                ('idSondeo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sondeo.sondeos')),
                ('idUsuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sondeo.usuario')),
            ],
        ),
    ]