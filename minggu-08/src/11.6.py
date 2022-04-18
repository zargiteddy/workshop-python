import weakref, gc
class A:
    def __init__(self, value):
        self.value = value
    def __repr__(self):
        return str(self.value)

a = A(10) # membuat reference
d = weakref.WeakValueDictionary()
d['primary'] = a  # tidak membuat referensi
print(d['primary']) # ambil objek jika masih aktif
del a # hapus satu referensi tersebut
print(gc.collect()) # jalankan garbage collection

d['primary'] # entry dihapus secara otomatis