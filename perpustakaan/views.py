from multiprocessing import context
from django.shortcuts import render
from perpustakaan.models import Buku

# Create your views here.
def buku(request):
    books = Buku.objects.all()
    
    context = {
        'books':books,
    }
    return render(request, 'perpustakaan/buku.html', context)
