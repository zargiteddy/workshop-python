# 10. PENGENALAN SINGKAT PUSTAKA STANDAR
## 10.1. Interface Sistem Operasi
Module [os](https://docs.python.org/3/library/os.html#module-os) menyediakan beberapa fungsi yang berguna untuk berinteraksi dengan sistem operasi:

_**nama file: `10.1-1.py`**_
```python
>>> import os
>>> os.getcwd() 
>>> os.chdir('/server/accesslogs') # Mengganti current directory
>>> os.system('mkdir today') # Menjalankan perintah mkdir di dalam shell sistem
```
Pastikan bahwa kita menggunakan `import os`, bukan menggunakan `from os import *`. Hal tersebut akan mencegah `os.open()` membayang-bayangi fungsi `open()` built-in yang beroperasi dengan cara yang berbeda.

Fungsi built-in `dir()`(https://docs.python.org/3/library/functions.html#dir) dan `help()`[https://docs.python.org/3/library/functions.html#help] sangat membantu kita dalam bekerja dengan modul yang besar seperti [os](https://docs.python.org/3/library/os.html#module-os):

_**nama file: `10.1-2.py`**_
```python
>>> import os
>>> dir(os)
<returns a list of all module functions>
>>> help(os)
<returns an extensive manual page created from the module's docstrings>
```
Untuk manajemen file dan direktori, modul [shutil](https://docs.python.org/3/library/shutil.html#module-shutil)

_**nama file: `10.1-3.py`**_
```python
>>> import shutil
>>> shutil.copyfile('data.db', 'archive.db')
'archive.db'
>>> shutil.move('/build/executables', 'installdir')
'installdir'
```
- - - - - - -
## 10.2. Wildcard pada File
Modul [glob](https://docs.python.org/3/library/glob.html#module-glob) menyediakan fungsi yang berguna untuk membuat list file dari pencarian wildcard direktori:

_**nama file: `10.2.py`**_
```python
>>> import glob
>>> glob.glob('*.py')
['coba.py']
```
- - - - - - 
## 10.3. Argumen Baris Perintah
Utility script sering kali perlu memproses argumen baris perintah. Argumen-argumen tersebut disimpan dalam bentuk list di dalam atribut `argv` dalam modul `sys`. 

_**nama file: `10.3-1.py`**_
```python
>>> import sys
>>> print(sys.argv)
['demo.py', 'one', 'two', 'three']
```
Modul [argparse](https://docs.python.org/3/library/argparse.html#module-argparse) menyediakan mekanisme yang lebih canggih untuk memproses argumen baris perintah. Script dibawah meng-ekstrak satu atau lebih _filenames_ dan jumlah opsional baris yang nantinya akan langsung ditampilkan:

_**nama file: `10.3-2.py`**_
```python
import argparse

parser = argparse.ArgumentParser(
    prog='top',
    description='Show top lines from each file')
parser.add_argument('filenames', nargs='+')
parser.add_argument('-l', '--lines', type=int, default=10)
args = parser.parse_args()
print(args)
```
Ketika dijalankan pada baris perintah dengan `python top.py --lines=5 alpha.txt beta.txt`, script menetapkan `args.lines` ke `5` dan `args.filenames` ke `['alpha.txt', 'beta.txt']`.

- - - - - - -
## 10.4. Pengalihan Output Error dan Penghentian Program
Module [sys](https://docs.python.org/3/library/sys.html#module-sys) juga memiliki atribut untuk _stdin_, _stdout_, dan _stderr_. _stderr_ berguna untuk memunculkan _warning_ dan pesan error untuk membuatnya terlihat bahkan ketika _stdout_ sudah dialihkan:

_**nama file: `10.4.py`**_
```python
>>> sys.stderr.write('Warning, log file not found starting a new one\n')
Warning, log file not found starting a new one
```
Cara tercepat untuk menghentikan script adalah dengan menggunakan `sys.exit()`.
- - - - - - -
## 10.5. Pencocokan Pola String
Module [re](https://docs.python.org/3/library/re.html#module-re) menyediakan tool expresi reguler untuk pemrosesan string. Untuk _matching_ (pencocokan) dan manipulasi, expresi reguler menyediakan solusi optimal yaitu:

_**nama file: `10.5.py`**_
```python
>>> import re
>>> re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest')
['foot', 'fell', 'fastest']
>>> re.sub(r'(\b[a-z]+) \1', r'\1', 'cat in the the hat')
'cat in the hat'
```
Ketika kita hanya membutuhkan kapabilitas sederhana, kita bisa menggunakan method string karena lebih mudah untuk di _read_ dan _debug_:

```python
>>> 'tea for too'.replace('too', 'two')
'tea for two'
```
- - - - - - - 
## 10.6. Matematika
Modul [math](https://docs.python.org/3/library/math.html#module-math) memberikan akses ke fungsi pustaka C untuk folating point math:

_**nama file: `10.6-1.py`**_
```python
>>> import math
>>> math.cos(math.pi / 4)
0.70710678118654757
>>> math.log(1024, 2)
10.0
```
Modul [random](https://docs.python.org/3/library/random.html#module-random) menyediakan tool untuk membuat seleksi acak:

_**nama file: `10.6-2.py`**_
```python
>>> import random
>>> random.choice(['apple', 'pear', 'banana'])
'apple'
>>> random.sample(range(100), 10) # sampling tanpa replacement
[30, 83, 16, 4, 8, 81, 41, 50, 18, 33]
>>> random.random()    # float acak
0.17970987693706186
>>> random.randrange(6) # integer acak yang dipilih dari range(6)
4
```
Modul [statistics](https://docs.python.org/3/library/statistics.html#module-statistics) menghitung properti statistika dasar (mean, median, variance, dll) dari data numerik:

_**nama file: `10.6-3.py`**_
```python
>>> import statistics
>>> data = [2.75, 1.75, 1.25, 0.25, 0.5, 1.25, 3.5]
>>> statistics.mean(data)
1.6071428571428572
>>> statistics.median(data)
1.25
>>> statistics.variance(data)
1.3720238095238095
```
- - - - - - - -
## 10.7. Akses Internet
Ada banyak modul yang berguna untuk mengakses internet dan memproses protokol internet. Dua modul internet yang sederhana di antaranya adalah [urllib.request](https://docs.python.org/3/library/urllib.request.html#module-urllib.request) untuk mengambil data dari URL dan [smtplib](https://docs.python.org/3/library/smtplib.html#module-smtplib) untuk mengirim email:

_**nama file: `10.7.py`**_
```python
>>> from urllib.request import urlopen
>>> with urlopen('http://worldtimeapi.org/api/timezone/etc/UTC.txt') as response:
...     for line in response:
...         line = line.decode()             # Konversi bytes ke str
...         if line.startswith('datetime'):
...             print(line.rstrip())         # Hapus newline yang tertinggal
...
datetime: 2022-01-01T01:36:47.689215+00:00

>>> import smtplib
>>> server = smtplib.SMTP('localhost')
>>> server.sendmail('soothsayer@example.org', 'jcaesar@example.org',
... """To: jcaesar@example.org
... From: soothsayer@example.org
...
... Beware the Ides of March.
... """)
>>> server.quit()
```
- - - - - - -
## 10.8. Tanggal dan Waktu
Modul [datetime](https://docs.python.org/3/library/datetime.html#module-datetime) menyediakan kelas untuk memanipulasi tanggal dan waktu dengan cara yang sederhana maupun cara yang rumit. Perhitungan tanggal dan waktu memang telah didukung, tetapi fokus utama penerapan modul `datetime` terletak pada ekstraksi member yang lebih efisien yang digunakan untuk pemformatan dan manipulasi. Modul ini juga mendukung objek yang _aware_ terhadap zona waktu.

_**nama file: `10.8.py`**_
```python
>>> # dates dapat dibuat and diformat dengan mudah
>>> from datetime import date
>>> now = date.today()
>>> now
datetime.date(2003, 12, 2)
>>> now.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B.")
'12-02-03. 02 Dec 2003 is a Tuesday on the 02 day of December.'

>>> # dates mendukung perhitungan kalender
>>> birthday = date(1964, 7, 31)
>>> age = now - birthday
>>> age.days
14368
```
- - - - - - -
## 10.9. Kompresi Data
Format pengarsipan dan pemformatan data secara langsung didukung oleh modul seperti `zlib`, `gzip`, `bz2`, `lzma`, `zipfile` dan `tarfile`.

_**nama file: `10.9.py`**_
```python
>>> import zlib
>>> s = b'witch which has which witches wrist watch'
>>> len(s)
41
>>> t = zlib.compress(s)
>>> len(t)
37
>>> zlib.decompress(t)
b'witch which has which witches wrist watch'
>>> zlib.crc32(s)
226805979
```
- - - - - - - - -
## 10.10. Pengukuran Performa
Kita bisa memilih untuk menggunakan fitur tuple seperti _packing_ dan _unpacking_. Modul [timeit](https://docs.python.org/3/library/timeit.html#module-timeit) dengan cepat dapat mendemonstrasikan keunggulan performa:

_**nama file: `10.10.py`**_
```python
>>> from timeit import Timer
>>> Timer('t=a; a=b; b=t', 'a=1; b=2').timeit()
0.57535828626024577
>>> Timer('a,b = b,a', 'a=1; b=2').timeit()
0.54962537085770791
```
- - - - - - - -
## 10.11. Kontrol Kualitas
Modul [doctest](https://docs.python.org/3/library/doctest.html#module-doctest) menyediakan tool untuk meninjau modul dan memvalidasi test yang ada di dalam docstring suatu program. Konstruksi test memiliki proses yang sederhana yaitu _cutting_ dan _pasting_ panggilan beserta dengan hasilnya ke dalam docstring. Hal tersebut meningkatkan kualitas dokumentasi dengan menyediakan contoh kepada user dan hal tersebut juga memungkinkan modul doctest untuk memastikan jika kode tetap sesuai denagan apa yang ada di dalam dokumentasi:

_**nama file: `10.11-1.py`**_
```python
def average(values):
    """Computes the arithmetic mean of a list of numbers.

    >>> print(average([20, 30, 70]))
    40.0
    """
    return sum(values) / len(values)

import doctest
doctest.testmod()
```
Modul [unittest](https://docs.python.org/3/library/unittest.html#module-unittest) memungkinkan kita untuk me-maintain kumpulan test komprehensif pada file terpisah:

_**nama file: `10.11-2.py`**_
```python
import unittest

class TestStatisticalFunctions(unittest.TestCase):

    def test_average(self):
        self.assertEqual(average([20, 30, 70]), 40.0)
        self.assertEqual(round(average([1, 5, 7]), 1), 4.3)
        with self.assertRaises(ZeroDivisionError):
            average([])
        with self.assertRaises(TypeError):
            average(20, 30, 70)

unittest.main()
```
- - - - - - - -
## 10.12. Batteries Included
Python memiliki filosofi "batteries included". Filosofi tersebut bisa dilihat dari kapabilitas _package_, contohnya:
- [xmlrpc.client](https://docs.python.org/3/library/xmlrpc.client.html#module-xmlrpc.client) dan [xmlrpc.server](https://docs.python.org/3/library/xmlrpc.server.html#module-xmlrpc.server) membuat implementasi panggilan prosedur remote menjadi sebuah tugas yang mudah.
- Package [email](https://docs.python.org/3/library/email.html#module-email) adalah sebuah library untuk mengelola pesan email, termasuk MIME dan berbagai dokumen [RFC-2822](https://tools.ietf.org/html/rfc2822.html).
- Package [json](https://docs.python.org/3/library/json.html#module-json) menyediakan dukungan robust untuk parsing format _data interchange_.
- Modul [sqlite3](https://docs.python.org/3/library/sqlite3.html#module-sqlite3) adalah _wrapper_ untuk library database SQLite yang menyediakan database persistent yang bisa diupdate dan diakses dengan sintaks SQL yang nonstandard.
- Internasionalisasi didukung oleh berbagai modul seperti [gettext](https://docs.python.org/3/library/gettext.html#module-gettext), [locale](https://docs.python.org/3/library/locale.html#module-locale), dan package [codecs](https://docs.python.org/3/library/codecs.html#module-codecs).
<br>

# 11. PENGENALAN SINGKAT PUSTAKA STANDAR — BAGIAN II
Bagian kedua ini membahas tentang modul-modul yang lebih canggih yang mendukung kebutuhan pemrograman profesional. Modul-modul tersebut jarang muncul di script berukuran kecil.

## 11.1. Pemformatan Output
Modul [reprlib](https://docs.python.org/3/library/reprlib.html#module-reprlib) menyediakan versi [repr()](https://docs.python.org/3/library/functions.html#repr) yang dikustomisasi untuk penampilan singkat atau sederhana dari kontainer nested yang berukuran besar:

_**nama file: `11.1-1.py`**_
```python
>>> import reprlib
>>> reprlib.repr(set('supercalifragilisticexpialidocious'))
"{'a', 'c', 'd', 'e', 'f', 'g', ...}"
```
Modul [pprint](https://docs.python.org/3/library/pprint.html#module-pprint) menawarkan kontrol yang lebih canggih dalam mencetak objek built-in dan objek yang didefinisikan oleh user dengan cara yang bisa dibaca oleh interpreter. Jika hasil melebihi satu baris, "pretty printer" menambahkan _break_ pada baris dan indentasi untuk menampilkan strukur data secara lebih jelas:

_**nama file: `11.1-2.py`**_
```python
>>> import pprint
>>> t = [[[['black', 'cyan'], 'white', ['green', 'red']], [['magenta',
...     'yellow'], 'blue']]]
...
>>> pprint.pprint(t, width=30)
[[[['black', 'cyan'],
   'white',
   ['green', 'red']],
  [['magenta', 'yellow'],
   'blue']]]
```
Modul [textwrap](https://docs.python.org/3/library/textwrap.html#module-textwrap) memformat paragraf dari sebuah teks supaya ukurannya pas dengan lebar layar yang telah diatur:

_**nama file: `11.1-3.py`**_
```python
>>> import textwrap
>>> doc = """The wrap() method is just like fill() except that it returns
... a list of strings instead of one big string with newlines to separate
... the wrapped lines."""
...
>>> print(textwrap.fill(doc, width=40))
The wrap() method is just like fill()
except that it returns a list of strings
instead of one big string with newlines
to separate the wrapped lines.
```
Modul [locale](https://docs.python.org/3/library/locale.html#module-locale) mengakses sebuah database dengan gaya format data yang spesifik. Atribut pengelompokan dari fungsi format milik locale menyediakan sebuah cara untuk pemformatan angka dengan pemisah kelompok:

_**nama file: `11.1-4.py`**_
```python
>>> import locale
>>> locale.setlocale(locale.LC_ALL, 'English_United States.1252')
'English_United States.1252'
>>> conv = locale.localeconv() 
>>> x = 1234567.8
>>> locale.format("%d", x, grouping=True)
'1,234,567'
>>> locale.format_string("%s%.*f", (conv['currency_symbol'],
...                      conv['frac_digits'], x), grouping=True)
'$1,234,567.80'
```
- - - - - - - -
## 11.2. Templating
Modul `string` memiliki kelas [Template](https://docs.python.org/3/library/string.html#string.Template) dengan sintaks yang disederhanakan yang cocok untuk pengeditan oleh _end-users_. Hal tersebut memungkinkan pengguna untuk mengkustomisasi aplikasi mereka tanpa harus mempengaruhi aplikasi.

Format templating menggunakan nama _placeholder_ yang dibentuk dengan `$` dengan identifier Python yang valid. Mengelilingi placeholder dengan brace dapat membuat placeholder bisa diikuti dengan lebih banyak huruf alfanumerik tanpa spasi yang gangguan spasi. Menulis `$$` akan membuat _single escaped_ `$`:

_**nama file: `11.2-1.py`**_
```python
>>> from string import Template
>>> t = Template('${village}folk send $$10 to $cause.')
>>> t.substitute(village='Nottingham', cause='the ditch fund')
'Nottinghamfolk send $10 to the ditch fund.'
```
Method [substitute()](https://docs.python.org/3/library/string.html#string.Template.substitute) memunculkan `KeyError` ketika placeholder tidak disediakan di dalam dictionary atau argumen keyword. Untuk aplikasi bergaya _mail-merge_, data yang disediakan user bisa saja tidak lengkap, sehingga user perlu menggunakan method[safe_substitute()](https://docs.python.org/3/library/string.html#string.Template.safe_substitute) — hal ini membuat placeholder tidak berubah jika ada data yang hilang:

_**nama file: `11.2-2.py`**_
```python
>>> t = Template('Return the $item to $owner.')
>>> d = dict(item='unladen swallow')
>>> t.substitute(d)
Traceback (most recent call last):
  ...
KeyError: 'owner'
>>> t.safe_substitute(d)
'Return the unladen swallow to $owner.'
```
Subclass template bisa menentukan pembatas kustom. Contohnya, utilitas penggantian nama batch untuk sebuah browser foto bisa memilih untuk menggunakan tanda persen untuk placeholder seperti tanggal saat ini, nomor urut gambar, atau format file:

_**nama file: `11.2-3.py`**_
```python
>>> import time, os.path
>>> photofiles = ['img_1074.jpg', 'img_1076.jpg', 'img_1077.jpg']
>>> class BatchRename(Template):
...     delimiter = '%'
>>> fmt = input('Enter rename style (%d-date %n-seqnum %f-format):  ')
Enter rename style (%d-date %n-seqnum %f-format):  Ashley_%n%f

>>> t = BatchRename(fmt)
>>> date = time.strftime('%d%b%y')
>>> for i, filename in enumerate(photofiles):
...     base, ext = os.path.splitext(filename)
...     newname = t.substitute(d=date, n=i, f=ext)
...     print('{0} --> {1}'.format(filename, newname))

img_1074.jpg --> Ashley_0.jpg
img_1076.jpg --> Ashley_1.jpg
img_1077.jpg --> Ashley_2.jpg
```
Aplikasi lain untuk templating memisahkan logika program dari detail berbagai format output. Hal ini memungkinkan kita untuk men-substitusi template kustom untuk file XML, laporan plain text, dan laporan web HTML.
- - - - - - - -
## 11.3. Bekerja dengan Layout Record Data Biner
Modul [struct](https://docs.python.org/3/library/struct.html#module-struct) menyediakan fungsi `pack()` dan `unpack()` untuk bekerja dengan format record biner. Contoh di bawah menunjukkan cara untuk melakukan loop pada informasi header di dalam file ZIP tanpa menggunakan modul [zipfile](https://docs.python.org/3/library/zipfile.html#module-zipfile). Kode pack `"H"` dan `"I"` merepresentasikan dua dan empat byte angka yang tidak _unsigned_. `"<"` mengindikasikan bahwa kode tersebut adalah ukuran standar dan ada di dalam urutan byte little-endian:

_**nama file: `11.3.py`**_
```python
import struct

with open('myfile.zip', 'rb') as f:
    data = f.read()

start = 0
for i in range(3):  # menunjukkan 3 header pertama
    start += 14
    fields = struct.unpack('<IIIHH', data[start:start+16])
    crc32, comp_size, uncomp_size, filenamesize, extra_size = fields

    start += 16
    filename = data[start:start+filenamesize]
    start += filenamesize
    extra = data[start:start+extra_size]
    print(filename, hex(crc32), comp_size, uncomp_size)

    start += extra_size + comp_size # lewati ke header selanjutnya
```
- - - - - - -
## 11.4. Multi-threading
_Threading_ adalah teknik untuk memisahkan pekerjaan yang tidak dependen secara sekuensial. Thread bisa digunakan untuk meng-improve ke-responsif-an aplikasi yang menerima input user ketika pekerjaan lain berjalan di background. 

Kode di bawah menunjukkan bagaimana modul [threading](https://docs.python.org/3/library/threading.html#module-threading) high level bisa menjalankan task di background ketika program utama sedang berjalan:

_**nama file: `11.4.py`**_
```python
import threading, zipfile

class AsyncZip(threading.Thread):
    def __init__(self, infile, outfile):
        threading.Thread.__init__(self)
        self.infile = infile
        self.outfile = outfile

    def run(self):
        f = zipfile.ZipFile(self.outfile, 'w', zipfile.ZIP_DEFLATED)
        f.write(self.infile)
        f.close()
        print('Finished background zip of:', self.infile)

background = AsyncZip('mydata.txt', 'myarchive.zip')
background.start()
print('The main program continues to run in foreground.')

background.join()  # menunggu background task selesai
print('Main program waited until background was done.')
```
Pendekatan yang umum digunakan untuk koordinasi task adalah untuk mengonsentrasikan semua akses ke resource di dalam thread tunggal dan kemudian menggunakan modul [queue](https://docs.python.org/3/library/queue.html#module-queue) untuk mengirimi thread tersebut dengan request dari thread lain. Aplikasi yang menggunakan objek `Queue` untuk komunikasi dan koordinasi inter-thread lebih mudah didesain, lebih mudah dibaca, dan lebih bisa diandalkan.
- - - - - - -
## 11.5. Logging
Modul [logging](https://docs.python.org/3/library/logging.html#module-logging) menawarkan sistem logging yang fleksibel dan memiliki fitur yang lengkap. Pada kasus yang paling sederhana, pesan log dikirim ke dalam file atau ke `sys.stderr`:

_**nama file: `11.5.py`**_
```python
import logging
logging.debug('Debugging information')
logging.info('Informational message')
logging.warning('Warning:config file %s not found', 'server.conf')
logging.error('Error occurred')
logging.critical('Critical error -- shutting down')
```
Hal tersebut menghasilkan output:

```python
WARNING:root:Warning:config file server.conf not found
ERROR:root:Error occurred
CRITICAL:root:Critical error -- shutting down
```
Sistem logging bisa dikonfigurasi langsung dari Python atau bisa dimuat dari konfigurasi user untuk logging yang dikustomisasi tanpa memengaruhi aplikasi.
- - - - - - - 
## 11.6. Referensi Weak
Python melakukan manajemen memori otomatis. Memori ini langsung dilepas setelah referensi terakhir pada memori tersebut sudah dieliminasi.

Modul [weakref](https://docs.python.org/3/library/weakref.html#module-weakref) menyediakan tool untuk melacak objek tanpa membuat referensi. Ketika objek tidak lagi dibutuhkan, objek tersebut secara otomatis dihapus dari tabel weakref dan _callback_ langsung dimunculkan untuk objek weakref. Aplikasi sejenis termasuk pemrosesan caching objek yang "mahal" untuk dibuat:

_**nama file: `11.6.py`**_
```python
>>> import weakref, gc
>>> class A:
...     def __init__(self, value):
...         self.value = value
...     def __repr__(self):
...         return str(self.value)
...
>>> a = A(10) # membuat reference
>>> d = weakref.WeakValueDictionary()
>>> d['primary'] = a  # tidak membuat referensi
>>> d['primary']  # ambil objek jika masih aktif
10
>>> del a # hapus satu referensi tersebut
>>> gc.collect() # jalankan garbage collection
0
>>> d['primary'] # entry dihapus secara otomatis
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    d['primary'] # entry dihapus secara otomatis
  File "C:/python310/lib/weakref.py", line 46, in __getitem__
    o = self.data[key]()
KeyError: 'primary'
```
- - - - - - - -
## 11.7. Tool untuk Bekerja dengan List
Banyak kebutuhan struktur data yang bisa dipertemukan dengan jenis list built-in. Modul [array](https://docs.python.org/3/library/array.html#module-array) menyediakan objek [array()](https://docs.python.org/3/library/array.html#array.array) yang berbentuk seperti list yang menyimpan hanya data homogen yang disimpan secara compact. Contoh di bawah menunjukkan array angka yang disimpan dalam bentuk angka biner unsigned dua byte (typecode `"H"`):

_**nama file: `11.7-1.py`**_
```python
>>> from array import array
>>> a = array('H', [4000, 10, 700, 22222])
>>> sum(a)
26932
>>> a[1:3]
array('H', [10, 700])
```
Modul [collections](https://docs.python.org/3/library/collections.html#module-collections) menyediakan objek [deque()](https://docs.python.org/3/library/collections.html#collections.deque) yang berbentuk seperti list tetapi dengan append yang lebih cepat dan pop dari sisi kiri tetapi lookup di tengah yang lebih lambat. Objek-objek ini cocok untuk mengimplementasikan queue:

_**nama file: `11.7-2.py`**_
```python
>>> from collections import deque
>>> d = deque(["task1", "task2", "task3"])
>>> d.append("task4")
>>> print("Handling", d.popleft())
Handling task1
```
```python
unsearched = deque([starting_node])
def breadth_first_search(unsearched):
    node = unsearched.popleft()
    for m in gen_moves(node):
        if is_goal(m):
            return m
        unsearched.append(m)
```
Pustaka juga menawarkan tool lain seperti modul [bisect](https://docs.python.org/3/library/bisect.html#module-bisect) dengan fungsi untuk memanipulasi list urut:

_**nama file: `11.7-3.py`**_
```python
>>> import bisect
>>> scores = [(100, 'perl'), (200, 'tcl'), (400, 'lua'), (500, 'python')]
>>> bisect.insort(scores, (300, 'ruby'))
>>> scores
[(100, 'perl'), (200, 'tcl'), (300, 'ruby'), (400, 'lua'), (500, 'python')]
```
Modul [heapq](https://docs.python.org/3/library/heapq.html#module-heapq) menyediakan fungsi untuk mengimplementasikan heap berdasarkan list reguler. Nilai paling rendah yang bisa dimasukkan adalah nol. `heapq` berguna untuk aplikasi yang secara berulang kali mengakses elemen paling kecil tetapi tidak ingin menjalankan pengurutan list full:

_**nama file: `11.7-4.py`**_
```python
>>> from heapq import heapify, heappop, heappush
>>> data = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
>>> heapify(data) # mengatur ulang list ke dalam heap urutan
>>> heappush(data, -5) # masukkan entry baru
>>> [heappop(data) for i in range(3)]  # ambil tiga entry terkecil
[-5, 0, 1]
```
- - - - - - - - -
## 11.8. Aritmetika Floating Point Desimal
Modul [decimal](https://docs.python.org/3/library/decimal.html#module-decimal) menawarkan sebuah tipe data [Decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal) untuk aritmetika floating point desimal. Dibandingkan dengan implementasi `float` built-in dari floating point biner, kelas tersebut sangat membantu untuk:
- aplikasi finansial.
- kontrol pada presisi.
- kontrol atas pembulatan untuk memenuhi kebutuhan legal atau regulasi.
- pelacakan letak desimal yang signifikan.
- aplikasi dimana user mengharapkan hasil yang sesuai dengan perhitungan yang dilakukan secara manual.

Misalnya, perhitungan pajak 5% pada tagihan telepon sebesar 70 cent akan memebrikan hasil yang berbeda pada floating point desimal dan floating point biner. Perbedaan menjadi signifikan jika hasilnya dibulatkan ke cent terdekat:

_**nama file: `11.8.py`**_
```python
>>> from decimal import *
>>> round(Decimal('0.70') * Decimal('1.05'), 2)
Decimal('0.74')
>>> round(.70 * 1.05, 2)
0.73
```
Kita juga bisa menggunakan kelas `Decimal` untuk mengimplementasikan perhitungan modulo dan pengujian persamaan yang tidak cocok untuk floating point biner:

```python
>>> Decimal('1.00') % Decimal('.10')
Decimal('0.00')
>>> 1.00 % 0.10
0.09999999999999995

>>> sum([Decimal('0.1')]*10) == Decimal('1.0')
True
>>> sum([0.1]*10) == 1.0
False
```
Modul [decimal](https://docs.python.org/3/library/decimal.html#module-decimal) menyediakan aritmetika dengan presisi sesuai yang dibutuhkan:

```python
>>> getcontext().prec = 36
>>> Decimal(1) / Decimal(7)
Decimal('0.142857142857142857142857142857142857')
```
- - - - -
### Bab 10 dan 11 sudah selesai! Molte grazie! :nerd_face: