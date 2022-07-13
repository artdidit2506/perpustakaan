from import_export import resources
from perpustakaan.models import Buku
from import_export.fields import Field

# untuk export-import file


class BukuResource(resources.ModelResource):
    kelompok_id__nama = Field(attribute='kelompok_id', column_name='kelompok')

    class Meta:
        model = Buku
        fields = ('judul', 'penulis', 'kelompok_id__nama', 'penerbit',
                  'jumlah', 'datetime')
        export_order = ('judul', 'penulis', 'penerbit',
                        'kelompok_id__nama', 'jumlah', 'datetime')
