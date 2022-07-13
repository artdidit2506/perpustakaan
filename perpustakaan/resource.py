from import_export import resources
from perpustakaan.models import Buku


class BukuResource(resources.ModelResource):
    class Meta:
        model = Buku
        fields = ('cover', 'judul', 'penulis', 'penerbit',
                  'jumlah', 'datetime', 'kelompok_id')
