from dataclasses import field, fields
from pyexpat import model
from tkinter import Widget
from tkinter.tix import Form
from django import forms
from django.forms import ModelForm
from perpustakaan.models import Buku


class FormBuku(ModelForm):
    class Meta:
        model = Buku
        fields = '__all__'


widget = {
    'judul': forms.TextInput(attrs={
        'class': 'form-control',
        'id': 'Judul Buku',
        'placeholder': 'Judul Buku',
    }),

    'penulis': forms.TextInput({'class': 'form-control', 'id': 'Penulis'}),
    'penerbit': forms.TextInput({'class': 'form-control', 'id': 'Penerbit'}),
    'jumlah': forms.NumberInput({'class': 'form-control', 'id': 'Jumlah'}),
    'kolompok_id': forms.Select({'class': 'form-control', 'id': 'Kolompok'}),
}
