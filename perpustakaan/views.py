from email import message
from multiprocessing import context
from urllib import response
from django.shortcuts import render, redirect, HttpResponse
from perpustakaan.models import Buku
from perpustakaan.forms import FormBuku
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.contrib.auth.forms import UserCreationForm
from perpustakaan.resource import BukuResource
# Create your views here.


def export_xls(request):

    # Create an instance of the resource class
    buku = BukuResource()
    dataset = buku.export()
    response = HttpResponse(
        dataset.xls, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="Laporan Buku.xls"'
    return response


@login_required(login_url=settings.LOGIN_URL)
def register(request):
    if request.POST:
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Selamat, Anda telah terdaftar!')
            return redirect('register')
        else:
            messages.error(request, 'Mohon maaf, Anda gagal terdaftar!')
            return redirect('register')
    else:
        form = UserCreationForm()
        context = {
            'form': form,
        }
        return render(request, 'registration/register.html', context)


@login_required(login_url=settings.LOGIN_URL)
def hapus_buku(request, id_buku):
    buku = Buku.objects.filter(id=id_buku)
    buku.delete()
    messages.success(request, 'Data berhasil dihapus')
    return redirect('buku')


@login_required(login_url=settings.LOGIN_URL)
def ubah_buku(request, id_buku):
    buku = Buku.objects.get(id=id_buku)
    if request.POST:
        form = FormBuku(request.POST, instance=buku, files=request.FILES)
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


@login_required(login_url=settings.LOGIN_URL)
def buku(request):
    books = Buku.objects.all()

    context = {
        'books': books,
    }
    return render(request, 'perpustakaan/buku.html', context)


@login_required(login_url=settings.LOGIN_URL)
def penerbit(request):
    return render(request, 'perpustakaan/penerbit.html')


@login_required(login_url=settings.LOGIN_URL)
def tambah_buku(request):
    if request.POST:
        form = FormBuku(request.POST, request.FILES)
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
