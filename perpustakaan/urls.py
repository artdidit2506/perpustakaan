from django.urls import path
from .import views

urlpatterns = [
    path('', views.buku, name='buku'),
    path('penerbit/', views.penerbit, name='penerbit'),
    path('tambah-buku/', views.tambah_buku, name='tambah-buku'),
    path('buku/ubah/<int:id_buku>', views.ubah_buku, name='ubah_buku'),
]
