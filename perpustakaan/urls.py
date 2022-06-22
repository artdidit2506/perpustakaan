from django.urls import path
from .import views

urlpatterns = [
    path('', views.buku, name='buku'),
    path('penerbit/', views.penerbit, name='penerbit'),
    path('tambah-buku/', views.tambah_buku, name='tambah-buku')
]