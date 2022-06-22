from dataclasses import field, fields
from pyexpat import model
from tkinter.tix import Form
from django.forms import ModelForm
from perpustakaan.models import Buku

class FormBuku(ModelForm):
    class Meta:
        model = Buku
        fields = '__all__'