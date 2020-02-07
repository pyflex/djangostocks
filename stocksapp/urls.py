from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('add_stock', views.add_stock, name='add_stock'),
    path('delete/<stock_id>', views.delete, name='delete'),
    path('delete_stock', views.delete_stock, name="delete_stock"),
]
