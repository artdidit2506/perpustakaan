from django.urls import path
from . import views
from perpustakaan.views import *
from django.contrib.auth.views import LoginView, LogoutView
from django.conf.urls.static import static

urlpatterns = [
    path('', views.buku, name='buku'),
    path('penerbit/', views.penerbit, name='penerbit'),
    path('tambah-buku/', views.tambah_buku, name='tambah-buku'),
    path('buku/ubah/<int:id_buku>', views.ubah_buku, name='ubah_buku'),
    path('buku/hapus/<int:id_buku>', views.hapus_buku, name='hapus_buku'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),
    path('export/xls/', views.export_xls, name='export_xls'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
