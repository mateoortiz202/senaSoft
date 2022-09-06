#urls del projecto
from django.urls import path
from . import views
app_name = 'sondeo'

urlpatterns = [
    path('', views.inicio, name="inicio"),




    path('login/', views.login, name="login"),
    path('logear=', views.logear, name="logear"),
]