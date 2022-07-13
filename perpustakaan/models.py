from datetime import date, datetime
from django.db import models

# Create your models here.


class Kelompok(models.Model):
    nama = models.CharField(max_length=19)
    keterangan = models.TextField()

    def __str__(self):
        return self.nama


class Buku(models.Model):
    judul = models.CharField(max_length=50)
    penulis = models.CharField(max_length=50)
    penerbit = models.CharField(max_length=50)
    jumlah = models.IntegerField(null=True)
    kelompok_id = models.ForeignKey(
        Kelompok, on_delete=models.CASCADE, null=True)
    cover = models.ImageField(upload_to='cover/', null=True)
    datetime = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.judul
