from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    
    #The URL afterwards 'shorted/' is the URL that the user wants to shorts
    path('shorted/', views.shorted, name='shorted')
]
