from django.db import models

# Create your models here.
class Buku(models.Model):
    judul = models.CharField(max_length=50)
    penulis = models.CharField(max_length=50)
    penerbit = models.CharField(max_length=50)
    jumlah = models.IntegerField(null=True)
    
    def __str__(self):
        return self.judul