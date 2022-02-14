# 1. PENDAHULUAN
-----------------------------
PERHATIAN!
 untuk mengakses source code, bisa masuk ke folder src dan cari nama file py sesuai yang sudah saya tuliskan setiap sebelum saya menulis code di file README ini. Contoh:

 _**nama file: `2.1.2.py`**_
```python
>>> the_world_is_flat = True
>>> if the_world_is_flat:
...     print("Be careful not to fall off!")
...     
Be careful not to fall off!
```
--------------------
Selamat datang di pertemuan pertama workshop Python :snake:! _First of all_, di sini saya akan membahas beberapa hal tentang bahasa pemrograman Python. Tulisan ini adalah sebuah proses _"Whetting your appetite"_ yang bisa diartikan sebagai "menggugah selera kita untuk memulai belajar menggunakan bahasa pemrograman Python".

Python adalah bahasa pemrograman yang sangat mudah digunakan serta menawarkan struktur dan _support_ untuk program berukuran besar. Python juga bisa melakukan proses _error checking_ yang lebih baik daripada C dan memiliki _arrays_ dan _dictionaries_ yang fleksibel.

Python dapat membagi-bagi program menjadi module yang dapat digunakan di program Python yang lain. Python memiliki koleksi _standard modules_ yang sangat banyak yang bisa kita gunakan sebagai basis pada program Python yang kita miliki. Python adalah _interpreted language_, yang artinya kita dapat menghemat waktu saat pengembangan program karena tidak ada proses _compilation_ dan _linking_.

Python membuat penulisan program menjadi padat (_compact_) dan mudah dibaca. Program yang ditulis di Python pada dasarnya memerlukan kode yang lebih sedikit daripada program yang ditulis dengan bahasa C, C++, atau Java karena:
 - Tipe data _high-level_ yang dapat melakukan operasi kompleks dalam satu _statement_.
 - Pengelompokan _statement_ dilakukan dengan _indentation_ (tulisan sedikit menjorok ke kanan), bukan dengan _brackets_.
 - Tidak memerlukan deklarasi variabel atau argumen.

<br/>

# 2. MENGGUNAKAN PYTHON INTERPRETER

## 2.1. Memunculkan Interpreter
Biasanya, Python interpreter ter-install pada direktori `/usr/local/bin/python3.10`. Untuk masuk ke direktori tersebut, pada terminal atau shell kita ketik `/usr/local/bin` lalu kita aktifkan interpreter dengan mengetik _command_: `python3.10`. Selain pada direktori tersebut, interpreter juga bisa disimpan di dalam direktori alternatif seperti `/usr/local/python`.

Untuk keluar dari interpreter, kita bisa mengetik `control - D` (pada unix) atau `Control - Z` (pada windows) di _primary prompt_. Jika tidak bisa, kita bisa keluar dari interpreter dengan menggunakan _command_ `quit()`.

Fitur _line-editing_ pada interpreter terdiri dari _interactive editing_, _history subtitution_, dan _code completion_ pada sistem yang mendukung pustaka (_library_) [GNU Readline](https://tiswww.case.edu/php/chet/readline/rltop.html). Untuk memerika apakah _command line editing_ di-_support_ pada interpreter, kita bisa mengetik `Control - P` pada _Python prompt_. Jika berbunyi (_beep_), berarti kita memiliki _command-line editing_. Jika tidak ada apapun yang muncul atau terjadi, berarti _command-line editing_ tidak _available_ dan kita hanya dapat menggunakan _backspace_ untuk menghapus karakter pada suatu baris.

Python interpreter bekerja sama seperti shell Unix. Maksudnya adalah, contoh; ketika dipanggil menggunakan sebuah input standar yang dikoneksikan ke sebuah perangkat tty (_teletypewriter_), interpreter mengeksekusi _command_ secara interaktif. Contoh lain adalah, ketika interpreter dipanggil dengan file sebagai input standar, maka interpreter membaca dan mengeksekusi script dari file tersebut.

Selain menggunakan command `python3.10`, kita juga bisa mengaktifkan interpreter dengan menuliskan `python -c command [arg] ...`, yang langsung mengeksekusi _statement(s)_ yang dituliskan pada _command_. Beberapa _module_ Python berfungsi sebagai _script_. _modules_ tersebut dapat dipanggil dengan perintah `python -m module [arg] ...`,  yang mengeksekusi _source file_ untuk _module_.

Jika ingin lebih tahu banyak tentang berbagai opsi _command line_, kita bisa lihat di [Command line and environment](https://docs.python.org/3/using/cmdline.html#using-on-general).

### 2.1.1. Argument Passing
Nama script dan argumen-argumen tambahan selanjutnya akan dibubah menjadi sebuah list string dan dialokasikan ke variabel `argv` di dalam module `sys`. Kita bisa mengakses list ini dengan mengeksekusi `import sys`. Beberapa poin tentang argument passing:

 - Panjang sebuah list setidaknya adalah satu.
 - Jika tidak ada script dan argumen, maka `sys.argv[0]` dianggap sebagai _empty string_.
 - Jika nama script diberikan sebagai `'-'`(_standard input_), `sys.argv[0]` diset sebagai `'-'`.
 - Jika -c _command_  digunakan, `sys.argv[0]` diset sebagai `'-c'`
 - Jika -m _module_ digunakan, `sys.argv[0]` akan diset menjadi nama lengkap dari lokasi module tersebut.
 - Opsi yang terletak setelah -c _command_ atau -m _module_ tidak akan diproses oleh Python interpreter, tetapi diletakkan di `sys.argv`.

### 2.1.2. Interactive Mode
Di dalam mode ini, interpreter akan _prompt_ untuk _command_ selanjutnya dengan _primary prompt_ dengan tanda `(>>>)`; dan untuk baris-baris selanjutnya interpreter _prompt_ dengan _secondary prompt_ dengan tanda `(`...`)`. Berikut tampilan ketika interpreter menampilkan sebuah _welcome message_ sebelum prompt pertama:

    $ python3.10
    Python 3.10.2 (main, Feb  5 2022, 12:29:58) [GCC 9.3.0] on linux
    Type "help", "copyright", "credits" or "license" for more information.
    >>>

_continuation lines_ berfungsi ketika statement telah memasuki sebuah _multi-line_. Contoh:

 _**nama file: `2.1.2.py`**_
```python
>>> the_world_is_flat = True
>>> if the_world_is_flat:
...     print("Be careful not to fall off!")
...     
Be careful not to fall off!
```
## 2.2. Interpreter dan Environment-nya.
### 2.2.1. Source Code Encoding
Secara default, _encoding_ untuk _source code_ Python adalah UTF-8. Untuk menampilkan semua karakter di _encoding_ itu, editor yang kita gunakan harus tahu bahwa file tersebut adalah UTF-8 dan editor juga harus menggunakan font yang _support_ semua karakter di file tersebut.

untuk mendeklarasikan encoding (selain encoding default UTF-8), kita harus menuliskan baris untuk _"special comment"_ pada baris pertama sebuah file. Berikut syntax-nya:

 _**nama file: `2.2.1.py`**_
```python
# -*- coding: encoding -*-
```

Contoh; untuk mendeklarasikan Windows-1252 encoding sebagai encoding yang akan digunakan, kita harus menuliskan berikut di baris pertama file:

```python
# -*- coding: cp1252 -*-
```

Ada satu pengecualian terhadap aturan deklarasi encoding _first line_ yaitu ketika code dimulai dengan [UNIX "shebang" line](https://docs.python.org/3/tutorial/appendix.html#tut-scripts). Pada kasus ini, deklarasi encoding harus dituliskan di baris kedua file, contoh:

```python
#!/usr/bin/env python3
# -*- coding: cp1252 -*-
```
<br/>

# 3. PENGANTAR INFORMAL TERHADAP BAHASA PEMROGRAMAN PYTHON
Input dan output pada bagian ini dibedakan dengan hadir atau tidaknya _prompts_ (`>>>` dan `...`). Input adalah segala baris yang kita tulis setelah prompt, sementara output adalah baris yang kemunculannya tidak dimulai dengan prompt.

Pertama-tama, kita bahas tentang _comments_. _Comments_ di Python dimuali dengan karakter _hash_ (#) dan akan berakhir di akhir baris yang diberi tanda _hash_ tersebut. Berikut contohnya:

_**nama file: `3.py`**_
```python
# ini adalah comment pertama
spam = 1 # ini adalah comment kedua
         # comment ketiga!
text = "# ini bukan komen karena berada di dalam quotes (tanda petik)"
```
## 3.1. Menggunakan Python Sebagai Kalkulator
### 3.1.1. Numbers
Interpreter berfungsi sebagai kalkulator sederhana. Operator seperti +, -, * dan / berfungsi sama seperti di bahasa pemrograman lain. Parentheses (()) dapat digunakan untuk _grouping_. Contoh:

_**nama file: `3.1.1-1.py`**_
```python
>>> 2 + 2
4
>>> 50 - 5*6
20
>>> (50 - 5*6) / 4
5.0
>>> 8 / 5  # pembagian selalu me-return angka float
1.6
```
---------------------
Division (/) selalu me-return float. Untuk melakukan [floor division](https://docs.python.org/3/glossary.html#term-floor-division) dan mendapatkan hasil integer, kita bisa menggunakan operator //. Untuk menghitung sisa pembagian bisa kita gunakan %.

_**nama file: `3.1.1-2.py`**_
```python
>>> 17 / 3 # pembagian biasa me-return float
5.666666666666667
>>> 17 // 3 # floor division menghilangkan bagian pecahan
5
>>> 17 % 3 # operator % me-return sisa pembagian
2
>>> 5 * 3 + 2 # hasil bagi floor division * pembagi + sisa pembagian
17
```
---------------------
Dengan Python, kita bisa menggunakan ** untuk menghitung hasil perpangkatan:

_**nama file: `3.1.1-3.py`**_
```python
>>> 5 ** 2 # 5 kuadrat
25
>>> 2 ** 7 # 2 pangkat 7
128
```
---------------------
Tanda sama dengan (=) digunakan untuk menetapkan value ke dalam variabel:

_**nama file: `3.1.1-4.py`**_
```python
>>> width = 20
>>> height = 5 * 9
>>> width * height
900
```
---------------------
Jika variabel tidak didefinisikan (not defined), maka akan menampilkan hasil error:

_**nama file: `3.1.1-5.py`**_
```python
>>> n  # mencoba mengakses variabel yang tidak didefinisikan
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'n' is not defined
```
---------------------
Operator dengan operand bertipe campuran meng-convert operand integer menjadi floating point:

_**nama file: `3.1.1-6.py`**_
```python
>>> 4 * 3.75 - 1
14.0
```
---------------------
Di mode interaktif, hasil perhitungan terakhir ditetapkan ke dalam variabel `_`. Contoh:

_**nama file: `3.1.1-7.py`**_
```python
>>> tax = 12.5 / 100
>>> price = 100.50
>>> price * tax
12.5625
>>> price + _
113.0625
>>> round(_, 2)
113.06
```
---------------------
### 3.1.2. Strings
Python bisa memanipulasi string yang dapat dituliskan dengan beberapa cara seperti dengan _single quote_ ('...') atau _double quote_ ("..."):

_**nama file: `3.1.2-1.py`**_
```python
>>> 'spam eggs'  # single quotes
'spam eggs'
>>> 'doesn\'t'  # menggunakan \' untuk escape single quote...
"doesn't"
>>> "doesn't"  # ...atau bisa juga dengan double quote
"doesn't"
>>> '"Yes," they said.'
'"Yes," they said.'
>>> "\"Yes,\" they said."
'"Yes," they said.'
>>> '"Isn\'t," they said.'
'"Isn\'t," they said.'
```
---------------------
Fungsi print() menghasilkan output yang lebih mudah dibaca, yaitu dengan menghilangkan tanda kutip dan melakukan _print_ untuk memunculkan _special characters_:

_**nama file: `3.1.2-2.py`**_
```python
>>> '"Isn\'t," they said.'
'"Isn\'t," they said.'
>>> s = 'First line.\nSecond line.'  # \n berarti baris baru
>>> s  # tanpa print(), \n akan masuk ke dalam output dan tidak bekerja secara semestinya
'First line.\nSecond line.'
>>> print(s)  # dengan print(), \n menambahkan baris baru
First line.
Second line.
```
--------------
Jika kita tidak ingin karakter dipengaruhi oleh \ untuk dianggap sebagai _special characters_, kita bisa menggunakan _raw strings_ dengan menambahkan huruf `r` sebelum tanda petik pertama:

_**nama file: `3.1.2-3.py`**_
```python
>>> print('C:\some\name')  # \n berarti baris baru!
C:\some
ame
>>> print(r'C:\some\name')  # letakkan r sebelum tanda petik
C:\some\name
```
---------------------
Kita bisa menyebarkan String ke beberapa baris 
yaitu dengan _triple-quote_ : `"""..."""` atau`'''...'''`. Contoh:

_**nama file: `3.1.2-4.py`**_
```python
print("""\
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
""")
```
kode di atas menghasilkan output seperti ini:
```python
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
```
---------------------
Strings dapat digabungkan dengan operator +, dan diulangi dengan *:

_**nama file: `3.1.2-5.py`**_
```python
>>> # 'un' 3 kali, dilanjutkan dengan 'ium'
>>> 3 * 'un' + 'ium'
'unununium'
```
---------------------
Dua atau lebih _string literals_ yang bersebelahan akan secara otomatis digabungkan:

_**nama file: `3.1.2-6.py`**_
```python
>>> 'Py' 'thon'
'Python'
```
---------------------
Fitur di atas sangat berfungsi ketika kita mau memisahkan string yang terlalu panjang menjadi beberapa baris:

_**nama file: `3.1.2-7.py`**_
```python
>>> text = ('Put several strings within parentheses '
...         'to have them joined together.')
>>> text
'Put several strings within parentheses to have them joined together.'
```
---------------------
Fitur tersebut hanya berfungsi terhadap dua _literals_. Fitur tersebut tidak berfungsi terhadap variabel atau expression:

_**nama file: `3.1.2-8.py`**_
```python
>>> prefix = 'Py'
>>> prefix 'thon'  # can't concatenate a variable and a string literal
  File "<stdin>", line 1
    prefix 'thon'
                ^
SyntaxError: invalid syntax
>>> ('un' * 3) 'ium'
  File "<stdin>", line 1
    ('un' * 3) 'ium'
                   ^
SyntaxError: invalid syntax
```
Jika ingin menggabungkan variabel dan literal, gunakan + seperti contoh dibawah ini:
```python
>>> prefix + 'thon'
'Python'
```
---------------------
Kita bisa memberikan index ke Strings, dengan karakter pertama memiliki index 0:

_**nama file: `3.1.2-9.py`**_
```python
>>> word = 'Python'
>>> word[0]  # karakter di posisi 0
'P'
>>> word[5]  # karakter di posisi 5
'n'
```
Index juga bisa berupa bilangan negatif, yang dihitung dari kanan:
```python
>>> word[-1]  # karakter terakhir
'n'
>>> word[-2]  # karakter kedua dari terakhir
'o'
>>> word[-6]
'P'
```
Selain _indexing_, ada juga yang namanya _slicing_. _Indexing_ berfungsi untuk mengambil satu karakter saja, sedangkan _slicing_ bisa mengambil _substring_ (beberapa karakter tertentu dari string):
```python
>>> word[0:2]  # karakter dari posisi 0 (included) sampai 2 (excluded)
'Py'
>>> word[2:5]  # karakter dari posisi 2 (included) sampai 5 (excluded)
'tho'
```
Index _slice_ memiliki suatu ketentuan; index pertama yang dihilangkan dianggap 0, sedangkan index kedua yang dihilangkan dianggap sebagai size string yang di-_slice_.
```python
>>> word[:2]   # karakter dari awal sampai posisi 2 (excluded)
'Py'
>>> word[4:]   # karakter dari posisi 4 (included) sampai akhir
'on'
>>> word[-2:]  # karakter kedua dari akhir (included) sampai akhir karakter
'on'
```
Perhatikan bahwa index awal selalu _included_ (termasuk yang diindex/slice), sedangkan index akhir selalu _excluded_ (tidak termasuk yang diindex/slice). Hal ini berguna untuk memastikan jika rumus `s[:i] + s[i:]` selalu sama dengan `s`:
```python
>>> word[:2] + word[2:]
'Python'
>>> word[:4] + word[4:]
'Python'
```
Memasukkan index yang terlalu besar akan menghasilkan output error:
```python
>>> word[42]  # string hanya memiliki 6 karakter
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: string index out of range
```
Walau begitu, slice yang melebihi index tetap akan diproses dengan lancar tanpa error:
```python
>>> word[4:42]
'on'
>>> word[42:]
''
```
Python strings tidak dapat diganti (_immutable_). Maka dari itu, memasukkan value ke dalam posisi index akan memunculkan error:
```python
>>> word[0] = 'J'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object does not support item assignment
>>> word[2:] = 'py'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object does not support item assignment
```
Jika kita membutuhkan string yang berbeda, kita harus membuat string baru:
```python
>>> 'J' + word[1:]
'Jython'
>>> word[:2] + 'py'
'Pypy'
```
Fungsi _built-in_ `len()` me-return panjang dari string:
```python
>>> s = 'supercalifragilisticexpialidocious'
>>> len(s)
```
---------------------
### 3.1.3. Lists
_Compound data types_ di Python yang paling _versatile_(serbaguna) adalah list, yang bisa ditulis di dalam sebuah _bracket_ dan setiap value di dalamnya dipisahkan dengan tanda koma.

_**nama file: `3.1.3-1.py`**_
```python
>>> squares = [1, 4, 9, 16, 25]
>>> squares
[1, 4, 9, 16, 25]
```
Seperti string, list juga bisa diindex dan dislice:
```python
>>> squares[0]  # indexing me-return item
1
>>> squares[-1]
25
>>> squares[-3:]  # slicing me-return list baru
[9, 16, 25]
```
Seluruh operasi slice me-return list baru berisi element yang di-request. Artinya, slice dibawah akan me-return [shallow copy](https://docs.python.org/3/library/copy.html#shallow-vs-deep-copy) dari list target:
```python
>>> squares[:]
[1, 4, 9, 16, 25]
```
List juga men-support operasi _concatenation_ (penggabungan):
```python
>>> squares + [36, 49, 64, 81, 100]
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
```
---------------------
List bersifat [mutable](https://docs.python.org/3/glossary.html#term-mutable). Kita bisa mengganti konten di dalam suatu list:

_**nama file: `3.1.3-2.py`**_
```python
>>> cubes = [1, 8, 27, 65, 125]  # ada sesuatu yang salah di sini
>>> 4 ** 3  # kubik 4 adalah 64, bukan 65!
64
>>> cubes[3] = 64  # ganti value yang salah dengan 64
>>> cubes
[1, 8, 27, 64, 125]
```
Kita juga bisa menambahkan item baru di akhir list dengan menggunakan _method_ `append()`:
```python
>>> cubes.append(216)  # menambahkan kubik 6
>>> cubes.append(7 ** 3)  # menambahkan kubik 7
>>> cubes
[1, 8, 27, 64, 125, 216, 343]
```
---------------------
Penambahan nilai ke dalam slice juga bisa dilakukan, dan hal ini bisa mengubah ukuran dari list atau juga bisa menghilangkan seluruh nilai di dalam list:

_**nama file: `3.1.3-3.py`**_
```python
>>> letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
>>> letters
['a', 'b', 'c', 'd', 'e', 'f', 'g']
>>> # mengganti beberapa nilai
>>> letters[2:5] = ['C', 'D', 'E']
>>> letters
['a', 'b', 'C', 'D', 'E', 'f', 'g']
>>> # menghilangkan nilai
>>> letters[2:5] = []
>>> letters
['a', 'b', 'f', 'g']
>>> # hapus list dengan mengganti semua elemen dengan empty list
>>> letters[:] = []
>>> letters
[]
```
Method built-in `len()` juga bisa diterapkan di list:
```python
>>> letters = ['a', 'b', 'c', 'd']
>>> len(letters)
4
```
---------------------
Kita juga bisa melakukan nest pada list (list yang didalamnya ada list):

_**nama file: `3.1.3-4.py`**_
```python
>>> a = ['a', 'b', 'c']
>>> n = [1, 2, 3]
>>> x = [a, n]
>>> x
[['a', 'b', 'c'], [1, 2, 3]]
>>> x[0]
['a', 'b', 'c']
>>> x[0][1]
'b'
```
## 3.2. Langkah Pertama Menuju Pemrograman
Dengan Python, kita bisa membuat _sub-sequence_ deret Fibonacci:

_**nama file: `3.2-1.py`**_
```python
>>> # deret Fibonacci:
... # penjumlahan dua elemen mendefinisikan elemen selanjutnya
... a, b = 0, 1
>>> while a < 10:
...     print(a)
...     a, b = b, a+b
...
```
Contoh di atas memperkenalkan beberapa fitur baru:
- Baris pertama terdiri dari _multiple assignment_: variabel a dan variabel b secara bersamaan mendapatkan _value_ 0 dan 1.
- while loop berjalan selama kondisi `a < 10` bernilai True. Di Python, semua nilai integer yang bukan nol bernilai True, dan nol selalu bernilai False.
- _body_ dari loop while tersebut ter-_indent_. _indentation_ adalah cara Python untuk mengelompokkan beberapa statemen.
- fungsi `print()` menulis nilai dari argumen yang diberikan.
_**nama file: `3.2-2.py`**_
```python
   >>> i = 256*256
   >>> print('The value of i is', i)
   The value of i is 65536
```
- keyword `end` bisa digunakan untuk menghindari baris baru setelah output, atau mengakhiri output dengan string lain:
_**nama file: `3.2-3.py`**_
```python
>>> a, b = 0, 1
>>> while a < 1000:
...     print(a, end=',')
...     a, b = b, a+b
...
0,1,1,2,3,5,8,13,21,34,55,89,144,233,377,610,987,
```
-----------------

### Bab 1-3 selesai! Thank you! :smile:












