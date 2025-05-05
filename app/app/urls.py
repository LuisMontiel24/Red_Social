from django.urls import path
from . import views

urlpatterns = [
    path('loginC/', views.loginC, name='loginC'),
    path('inicio-sesion/', views.inicio_sesion, name='inicio_sesion'),
    path('logout/', views.logout, name='logout'),
]