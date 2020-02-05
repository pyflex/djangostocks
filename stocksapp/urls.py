from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'), 
]
