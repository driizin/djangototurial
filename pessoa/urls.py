from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index-pessoa'),
    path('<int:id_pessoa>/', views.detalha, name='detalhe-pessoa'),
    path('add/', views.create, name='add-pessoa'),
    path('edit/<int:id_pessoa>/', views.update, name='edit-pessoa'),
    path('delete/<int:id_pessoa>/', views.delete, name='delete-pessoa'),
    path('read/', views.read, name='read-pessoa'),
]
