
from django.urls import path
from . import views
app_name = 'sondeo'

urlpatterns = [
    path('', views.inicio, name="inicio"),
    path('urlUsuario/', views.registrarUsuario, name="urlUsuario"),
    path('registrarUsuario/', views.registrarU, name="registrarUsuario"),
    path('login/', views.login, name="login"),
    path('logear=', views.logear, name="logear"),
    path('cerrarSesion/', views.cerrarSesion, name="cerrarSesion"),
    path('urlAdmin/', views.urlAdmin, name="urlAdmin"),
    path('logAdmin/', views.logAdmin, name="logAdmin"),
    path('urlSondeo/', views.urlSondeo, name="urlSondeo"),
    path('guardarSondeo/', views.guardarSondeo, name="guardarSondeo"),
    
    path('guardarRespuesta/', views.guardarRespuesta, name="guardarRespuesta"),
    path('mostrarRes/<int:pk>', views.traerRes, name="mostrarRes"),
    path('listarCerti/', views.listarCerti, name="listarCerti"),
        
    
]