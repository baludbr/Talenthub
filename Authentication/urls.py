from django.urls import path,include
from .views import *
urlpatterns = [
    path("",dashboard),
    path('register/',register,name='register'),
     path('login/',login,name='login'),
     path('otp/',verification,name='otp'),
     path('nav/',navbar,name='nav'),
     path('profile/',profile,name='profile'),
     path('logout/',logout,name='logout')
]