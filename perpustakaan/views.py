from multiprocessing import context
from django.shortcuts import render
from perpustakaan.models import Buku
from perpustakaan.forms import FormBuku
# Create your views here.
def buku(request):
    books = Buku.objects.all()
    
    context = {
        'books':books,
    }
    return render(request, 'perpustakaan/buku.html', context)

def penerbit(request):
    return render(request, 'perpustakaan/penerbit.html')

def tambah_buku(request):
    form = FormBuku()
    
    context = {
        'form' : form,
    }
    return render(request, 'perpustakaan/tambah-buku.html', context)
