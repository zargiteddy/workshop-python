# 7. INPUT DAN OUTPUT
Ada beberapa cara untuk menampilkan output sebuah program; data bisa di-_print_ dengan bentuk _human-readable_ (dapat dengan mudah dibaca dan dimengerti oleh manusia), atau data bisa juga ditulis untuk penggunaan di masa mendatang.

## 7.1. Pemformatan Output yang Lebih Bagus
Sejauh ini kita telah mempelajari dua cara untuk menulis _values_: _expression statement_ dan fungsi [print](https://docs.python.org/3/library/functions.html#print). (Cara lainnya adalah dengan menggunakan method `write()` dari objek file; output file standar dapat direferensikan sebagai `sys.stdout`.)

Seringkali kita ingin memiliki kendali yang lebih atas pemformatan output, dan bukan hanya _print_ value yang _space-separated_ (dipisah dengan spasi). Ada beberapa cara untuk memformat output:

- Untuk menggunakan [formatted string literals](https://docs.python.org/3/tutorial/inputoutput.html#tut-f-strings), awali string dengan `f` atau `F` sebelum tanda petik. Di dalam string ini, kita bisa menulis ekspresi Python diantara karakter `{` dan `}` yang bisa me-refer ke variabel atau nilai literal.

    _**nama file: `7.1-1.py`**_
    ```python
    >>> year = 2016
    >>> event = 'Referendum'
    >>> f'Results of the {year} {event}'
    'Results of the 2016 Referendum'
    ```

- Method [str.format](https://docs.python.org/3/library/stdtypes.html#str.format), yang penulisannya membutuhkan sedikit lebih banyak _effort_. Kita tetap akan menggunakan `{` dan `}` untuk menandakan dimana variabel akan disubtitusi, tetapi kita juga harus menyediakan informasi yang akan diformat.

    _**nama file: `7.1-2.py`**_
    ```python
    >>> yes_votes = 42_572_654
    >>> no_votes = 43_132_495
    >>> percentage = yes_votes / (yes_votes + no_votes)
    >>> '{:-9} YES votes  {:2.2%}'.format(yes_votes, percentage)
    ' 42572654 YES votes  49.67%'
    ```

- Kita bisa meng-handle string dengan teknik _slicing_ dan _concatenation_ (rangkaian) untuk membuat _layout_.

Jika kita tidak membutuhkan output yang terlihat bagus/cantik, tetapi hanya ingin menampilkan beberapa variabel untuk debugging, kita bisa meng-convert value ke dalam string dengan fungsi [repr()](https://docs.python.org/3/library/functions.html#repr) atau [str()](https://docs.python.org/3/library/stdtypes.html#str).

Fungsi `str()` digunakan untuk me-return representasi value yang mudah dibaca, sementara `repr()` digunakan untuk men-generate representasi yang bisa dibaca oleh interpreter. Untuk objek yang tidak memiliki representasi tertentu untuk _human consumption_, `str()` akan me-return value yang sama dengan `repr()`. Kebanyakan value seperti angka atau struktur seperti list dan dictionary memiliki representasi yang sama saat menggunanakan fungsi `str()` maupun `repr()`. String memiliki dua representasi yang berbeda. Contoh:

_**nama file: `7.1-3.py`**_
```python
>>> s = 'Hello, world.'
>>> str(s)
'Hello, world.'
>>> repr(s)
"'Hello, world.'"
>>> str(1/7)
'0.14285714285714285'
>>> x = 10 * 3.25
>>> y = 200 * 200
>>> s = 'The value of x is ' + repr(x) + ', and y is ' + repr(y) + '...'
>>> print(s)
The value of x is 32.5, and y is 40000...
>>> # The repr() of a string adds string quotes and backslashes:
... hello = 'hello, world\n'
>>> hellos = repr(hello)
>>> print(hellos)
'hello, world\n'
>>> # The argument to repr() may be any Python object:
... repr((x, y, ('spam', 'eggs')))
"(32.5, 40000, ('spam', 'eggs'))"
```
Modul `string` memiliki class [Template](https://docs.python.org/3/library/string.html#string.Template) yang menyediakan cara lain untuk mensubtitusi value ke dalam bentuk string, menggunakan placeholder seperti `$x` dan menggantinya dengan value dari dictionary. Walau begitu, `Template` menyediakan kontrol yang sedikit terhadap proses pemformatan.
- - - - 
### 7.1.1. String Literal yang Diformat
String literal yang diformat (_f-strings_) memungkinkan kita untuk menyertakan value ekspresi Python di dalam string dengan mengawali string dengan `f` atau `F` dan menulis ekspresi sebagai `{expression}`.

Kode di bawah adalah contoh pembulatan pi ke 3 langkah setelah desimal:

_**nama file: `7.1.1-1.py`**_
```python
>>> import math
>>> print(f'The value of pi is approximately {math.pi:.3f}.')
The value of pi is approximately 3.142.
```
- - - -
Meletakkan bilangan bulat setelah '`:`' akan menyebabkan field tersebut memiliki lebar karakter yang paling minimum. Hal ini berfungsi untuk membuat kolom tersusun berbaris.

_**nama file: `7.1.1-2.py`**_
```python
>>> table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
>>> for name, phone in table.items():
...     print(f'{name:10} ==> {phone:10d}')
...
Sjoerd     ==>       4127
Jack       ==>       4098
Dcab       ==>       7678
```
- - - - -
Modifier lain bisa digunakan untuk mengonversi value sebelum diformat.

_**nama file: `7.1.1-3.py`**_
```python
>>> animals = 'eels'
>>> print(f'My hovercraft is full of {animals}.')
My hovercraft is full of eels.
>>> print(f'My hovercraft is full of {animals!r}.')
My hovercraft is full of 'eels'.
```
- - - - - -
### 7.1.2. Method String `format()`
Penggunaan dari [str.format()](https://docs.python.org/3/library/stdtypes.html#str.format) dapat dilihat di bawah ini:

_**nama file: `7.1.2-1.py`**_
```python
>>> print('We are the {} who say "{}!"'.format('knights', 'Ni'))
We are the knights who say "Ni!"
```
- - - - - - 
Bracket dan karakter di dalamnya digantikan dengan objek yang diletakkan ke dalam method `str.format()`. Angka di dalam bracket bisa digunakan untuk _refer_ ke posisi objek yang diletakkan ke dalam method `str.format()`.

_**nama file: `7.1.2-2.py`**_
```python
>>> print('{0} and {1}'.format('spam', 'eggs'))
spam and eggs
>>> print('{1} and {0}'.format('spam', 'eggs'))
eggs and spam
```
- - - - - -
Jika keyword argumen digunakan di dalam method `str.format()`, valuenya akan di-refer dengan menggunakan nama argumen.

_**nama file: `7.1.2-3.py`**_
```python
>>> print('This {food} is {adjective}.'.format(
...       food='spam', adjective='absolutely horrible'))
This spam is absolutely horrible.
```
- - - - -
Argumen posisional dan keyword bisa dikombinasikan:

_**nama file: `7.1.2-4.py`**_
```python
>>> print('The story of {0}, {1}, and {other}.'.format('Bill', 'Manfred',
                                                       other='Georg'))
The story of Bill, Manfred, and Georg.
```
- - - - - -
Jika kita memiliki format string yang sangat panjang yang tidak ingin kita pisah, kita bisa me-refer variabel supaya diformat berdasarkan nama dan bukan dengan posisi. Hal ini bisa dilakukan dengan memasukkan dictionary lalu menggunakan `[]` untuk mengakses _keys_.

_**nama file: `7.1.2-5.py`**_
```python
>>> table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
>>> print('Jack: {0[Jack]:d}; Sjoerd: {0[Sjoerd]:d}; '
...       'Dcab: {0[Dcab]:d}'.format(table))
Jack: 4098; Sjoerd: 4127; Dcab: 8637678
```
Bisa juga dilakukan dengan meletakkan tabel sebagai argumen keyword dengan notasi '**'.
- - - -
Hal ini berguna dalam kombinasi dengan fungsi built-in [vars()](https://docs.python.org/3/library/functions.html#vars) yang me-return sebuah dictionary yang didalamnya ada variabel lokal.

Sebagai contoh, kode dibawah menghasilkan kumpulan kolom yang tersusun rapi yang menampilkan bilangan bulat dan kuadrat serta kubik:

_**nama file: `7.1.2-6.py`**_
```python
>>> for x in range(1, 11):
...     print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))
...
 1   1    1
 2   4    8
 3   9   27
 4  16   64
 5  25  125
 6  36  216
 7  49  343
 8  64  512
 9  81  729
10 100 1000
```
- - - - 
### 7.1.3. Pemformatan String Secara Manual
Berikut tabel kuadrat dan kubik yang diformat secara menual:

_**nama file: `7.1.3-1.py`**_
```python
>>> for x in range(1, 11):
...     print(repr(x).rjust(2), repr(x*x).rjust(3), end=' ')
...     # Note use of 'end' on previous line
...     print(repr(x*x*x).rjust(4))
...
 1   1    1
 2   4    8
 3   9   27
 4  16   64
 5  25  125
 6  36  216
 7  49  343
 8  64  512
 9  81  729
10 100 1000
```
- - - - 
[str.rjust()](https://docs.python.org/3/library/stdtypes.html#str.rjust) meletakkan string di sebelah kanan dengan lebar tertentu dengan memberi spasi di sebelah kiri. Method lain yang similiar dengan `str.rjust()` adalah `str.ljust()` dan `str.center()`. Method-method tersebut tidak menuliskan apapun dan hanya me-return string baru.

Ada method lain bernama [str.zfill()](https://docs.python.org/3/library/stdtypes.html#str.zfill) yang meletakkan string numerik di sebelah kiri dengan angka nol. Method tersebut mengenali tanda plus dan minus.

_**nama file: `7.1.3-2.py`**_
```python
>>> '12'.zfill(5)
'00012'
>>> '-3.14'.zfill(7)
'-003.14'
>>> '3.14159265359'.zfill(5)
'3.14159265359'
```
- - - - - -
### 7.1.4. Pemformatan String Lama
Operator `%` (modulo) juga bisa digunakan untuk pemformatan string. Pada `'string' % values`, instance dari `%` di dalam `%` string digantikan dengan nol atau elemen dari `values`. Operasi ini dikenal dengan interpolasi string. Contoh:

_**nama file: `7.1.4.py`**_
```python
>>> import math
>>> print('The value of pi is approximately %5.3f.' % math.pi)
The value of pi is approximately 3.142.
```
- - - - - - 
## 7.2. Membaca dan Menulis File
[open](https://docs.python.org/3/library/functions.html#open) me-return objek file, dan biasanya digunakan dengan dua argumen: `open(filename, mode)`.

_**nama file: `7.2.py`**_
```python
>>> f = open('workfile', 'w')
```
Argumen pertama adalah string yang mengandung _filename_. Argumen kedua adalah string lain yang mengandung beberapa karakter yang mendeskripsikan bagaimana file akan digunakan. `mode` bisa dengan `'r'` jika file hanya akan dibaca, `'w'` jika hanya untuk ditulis, dan `'a'` membuka file untuk _appending_ (menambahkan). `'r+'` membuka file untuk dibaca dan ditulis.

Biasanya, file dibuka dengan _text mode_, yang berarti kita membaca dan menulis string di file yang diencode dengan encoding yang spesifik. Jika encoding tidak ditentukan, maka defaultnya akan mengikuti platform.

Kita bisa berlatih menggunakan keyword [with](https://docs.python.org/3/reference/compound_stmts.html#with) saat bekerja dengan objek file. Keuntungan menggunakan `with` adalah file akan ditutup dengan benar setelah selesai digunakan. Menggunakan `with` juga lebih ringkas dibanding menulis blok [try-finally](https://docs.python.org/3/reference/compound_stmts.html#finally):

```python
>>> with open('workfile') as f:
...     read_data = f.read()

>>> # We can check that the file has been automatically closed.
>>> f.closed
True
```

Jika kita tidak menggunakan keyword `with`, maka kita harus memanggil `f.close()` untuk menutup file dan mengosongkan seluruh resource sistem yang digunakan.

Setelah objek file ditutup dengan menggunakan statemen `with` atau dengan memanggil `f.close()`, percobaan untuk menggunakan objek file akan gagal.

```python
>>> f.close()
>>> f.read()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: I/O operation on closed file.
```
- - - - - -
### 7.2.1. Method Objek File
Pada contoh di bagian ini, kita asumsikan objek file bernama `f` sudah dibuat.

Untuk membaca seluruh konten file, panggil `f.read(size)` yang membaca beberapa kuantitas data dan me-return kuantitas tersebut dalam bentuk string (dalam _text mode_) atau objek byte (dalam mode binary). _size_ adalah argumen numerik opsional. Jika _size_ dihilangkan atau negatif, seluruh konten file akan dibaca dan di-return. Jika akhir file sudah dicapai, `f.read()` akan me-return empty string('').

_**nama file: `7.2.1-1.py`**_
```python
>>> f.read()
'This is the entire file.\n'
>>> f.read()
''
```
`f.readline()` membaca _single line_ dari file; karakter _newline_ (\n) ditinggalkan pada akhir string, dan hanya dihilangkan pada baris akhir file jika file tidak diakhiri dengan _newline_. Hal ini menyebabkan return value menjadi jelas (tidak ambigu).

```python
>>> f.readline()
'This is the first line of the file.\n'
>>> f.readline()
'Second line of the file\n'
>>> f.readline()
''
```
- - - - - -
Untuk membaca sebuah baris dari file, kita bisa melakukan loop pada objek file. Hal ini dianggap lebih efisien, cepat, dan ringkas.

_**nama file: `7.2.1-2.py`**_
```python
>>> for line in f:
...     print(line, end='')
...
This is the first line of the file.
Second line of the file
```
- - - - -
Jika ingin membaca semua baris dalam list kita juga bisa menggunakan `list(f)` atau `f.readlines()`.

`f.write(string)` menulis konten string ke dalam file, lalu me-return jumlah karakter yang tertulis.

_**nama file: `7.2.1-3.py`**_
```python
>>> f.write('This is a test\n')
15
```
- - - - - -
Tipe objek lain harus dikonversi. Bisa dikonversi ke string atau ke objek byte.

_**nama file: `7.2.1-4.py`**_
```python
>>> value = ('the answer', 42)
>>> s = str(value)  # convert the tuple to string
>>> f.write(s)
18
```
`f.tell()` me-return integer yang memberikan posisi objek file yang direpresentasikan sebagai angka byte ketika dalam mode binary dan sebagai angka _opaque_ ketika dalam mode teks.

Untuk mengganti posisi objek file, gunakan `f.seek(offset, whence)`.

_**nama file: `7.2.1-5.py`**_
```python
>>> f = open('workfile', 'rb+')
>>> f.write(b'0123456789abcdef')
16
>>> f.seek(5) # Go to the 6th byte in the file
5
>>> f.read(1)
b'5'
>>> f.seek(-3, 2) # Go to the 3rd byte before the end
13
>>> f.read(1)
b'd'
```
- - - - - -
### 7.2.2. Menyimpan Data Terstruktur dengan `json`
Python memungkinkan kita untuk menggunakan format data interchange bernama [JSON (JavaScript Object Notation)](https://www.json.org/json-en.html). Modul standar bernama json dapat mengambil hirearki data Python, lalu mengonversinya ke bentuk representasi string; proses ini dinamakan _serializing_. Merekonstruksi data dari representasi string dinamakan _deserializing_. Di antara _serializing_ dan _deserializing_, string yang merepresentasikan objek bisa disimpan di dalam file atau data.

Jika kita memiliki objek x, kita bisa melihat representasi string JSON-nya dengan kode berikut:

_**nama file: `7.2.2.py`**_
```python
>>> import json
>>> x = [1, 'simple', 'list']
>>> json.dumps(x)
'[1, "simple", "list"]'
```
Variasi lain dari fungsi [dumps()](https://docs.python.org/3/library/json.html#json.dumps), bernama [dump()](https://docs.python.org/3/library/json.html#json.dump), melakukan _serializing_ pada objek untuk menjadikannya file teks. Jadi jika f adalah objek file teks untuk ditulis, kita bisa gunakan ini:

```python
json.dump(x, f)
```
Untuk _decode_ objek lagi, jika f adalah objek file teks yang sudah dibuka untuk dibaca, lakukan:

```python
x = json.load(f)
```
- - - - -

### Bab 7 sudah selesai! ¡muchas gracias! :cowboy_hat_face:
