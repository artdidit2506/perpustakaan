from django.urls import path
from . import views
from perpustakaan.views import *
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', views.buku, name='buku'),
    path('penerbit/', views.penerbit, name='penerbit'),
    path('tambah-buku/', views.tambah_buku, name='tambah-buku'),
    path('buku/ubah/<int:id_buku>', views.ubah_buku, name='ubah_buku'),
    path('buku/hapus/<int:id_buku>', views.hapus_buku, name='hapus_buku'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
