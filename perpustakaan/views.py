from email import message
from multiprocessing import context
from django.shortcuts import render, redirect
from perpustakaan.models import Buku
from perpustakaan.forms import FormBuku
from django.contrib import messages

# Create your views here.



def hapus_buku(request, id_buku):
    buku = Buku.objects.filter(id=id_buku)
    buku.delete()
    messages.success(request, 'Data berhasil dihapus')
    return redirect('buku')


def ubah_buku(request, id_buku):
    buku = Buku.objects.get(id=id_buku)
    if request.POST:
        form = FormBuku(request.POST, instance=buku)
        if form.is_valid():
            form.save()
            messages.success(request, 'Data berhasil diperbarui')
            return redirect('ubah_buku', id_buku=id_buku)

    else:
        form = FormBuku(instance=buku)
        context = {
            'form': form,
            'buku': buku,
        }

    return render(request, 'perpustakaan/ubah-buku.html', context)


def buku(request):
    books = Buku.objects.all()

    context = {
        'books': books,
    }
    return render(request, 'perpustakaan/buku.html', context)


def penerbit(request):
    return render(request, 'perpustakaan/penerbit.html')


def tambah_buku(request):
    if request.POST:
        form = FormBuku(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Data berhasil ditambahkan')

            return redirect('buku')
            form = FormBuku()

            context = {
                'form': form,
            }
            return render(request, 'perpustakaan/tambah-buku.html', context)

    else:
        form = FormBuku()
        context = {
            'form': form,
        }

    return render(request, 'perpustakaan/tambah-buku.html', context)
