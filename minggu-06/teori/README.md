# 8. Error dan Exception
di Python, ada dua jenis error yaitu _syntax error_ dan _exceptions_.

## 8.1. Syntax Error (Kesalahan pada Syntax)
_Syntax error_ yang bisa disebut juga dengan _parsing error_ adalah kesalahan yang biasanya muncul saat kita belajar Python:

_**nama file: `8.1.py`**_
```python
>>> while True print('Hello world')
  File "<stdin>", line 1
    while True print('Hello world')
                   ^
SyntaxError: invalid syntax
```
_Parser_ mengulangi baris penyinggung dan menampilkan 'tanda panah' kecil yang menunjuk pada titik paling awal saat _error_ terdeteksi. _Error_ tersebut disebabkan oleh token sebelum tanda panah: pada contoh, _error_ terdeteksi pada fungsi [print()](https://docs.python.org/3/library/functions.html#print) yang disebabkan oleh hilangnya titik dua ('`:`') sebelum fungsi tersebut.

## 8.2. Exception
Error yang terdeteksi saat eksekusi berlangsung disebut dengan _exceptions_. Error tersebut bukan error yang fatal. Kebanyakan _exceptions_ tidak diatasi oleh program dan menampilkan _error_ seperti berikut:

_**nama file: `8.2.py`**_
```python
>>> 10 * (1/0)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ZeroDivisionError: division by zero
>>> 4 + spam*3
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'spam' is not defined
>>> '2' + 2
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can only concatenate str (not "int") to str
```
Baris terakhir pesan _error_ menunjukkan apa yang terjadi. _Exceptions_ memiliki beberapa jenis, dan jenis _exceptions_ ditampilkan bersama sebuah pesan: tipe pada contoh di atas adalah [ZeroDivisionError](https://docs.python.org/3/library/exceptions.html#ZeroDivisionError), [NameError](https://docs.python.org/3/library/exceptions.html#NameError), dan [TypeError](https://docs.python.org/3/library/exceptions.html#TypeError). String yang di-print sebagai jenis _exception_ juga adalah nama dari _built-in exception_ yang muncul. Hal ini berlaku pada _built-in exception_, tetapi tidak harus berlaku pada _user-defined exception_.

Baris yang lain menampilkan detail berdasar jenis _exception_ dan penyebabnya.

Bagian sebelumnya dari pesan _error_ menunjukkan konteks dimana _exception_ terjadi, dalam bentuk _stack trackback_.

## 8.3. Penanganan Exception
Kita bisa membuat program yang digunakan untuk menangani _exception_. Pada contoh di bawah, program meminta _user_ untuk memasukkan integer, tetapi juga membolehkan _user_ untuk menginterupsi program.

_**nama file: `8.3-1.py`**_
```python
>>> while True:
...     try:
...         x = int(input("Please enter a number: "))
...         break
...     except ValueError:
...         print("Oops!  That was no valid number.  Try again...")
...
```
Berikut cara statement [try](https://docs.python.org/3/reference/compound_stmts.html#try) bekerja:
- Pertama, klausa `try` dieksekusi
- Jika tidak ada _exception_ muncul, klausa `except` dilewati dan eksekusi statement `try` berakhir.
- Jika _exception_ muncul pada proses eksekusi klausa `try`, sisa klausa akan dilewati.
- Jika _exception_ tidak cocok dengan _exception_ yang disebutkan di dalam klausa `except`, _exception_ tersebut diteruskan ke statement `try` luar.
- - - - - - - - -
Statement `try` bisa memiliki lebih dari satu klausa `except` untuk menentukan _handler_ untuk _exception_ yang berbeda. _Handler_ hanya akan menangani _exception_ yang muncul di dalam klausa `try`. Klausa `except` bisa memiliki beberapa _exceptions_ sebagai tuple, contoh:

_**nama file: `8.3-2.py`**_
```python
... except (RuntimeError, TypeError, NameError):
...     pass
```
- - - - - - - - - -
Kelas di klausa [except](https://docs.python.org/3/reference/compound_stmts.html#except) cocok dengan _exception_ jika kelas atau kelas base nya sama. Contohnya, kode di bawah akan menampilkan B, C, D secara urut:

_**nama file: `8.3-3.py`**_
```python
class B(Exception):
    pass

class C(B):
    pass

class D(C):
    pass

for cls in [B, C, D]:
    try:
        raise cls()
    except D:
        print("D")
    except C:
        print("C")
    except B:
        print("B")
```
Perhatikan bahwa jika klausa `except` dibalik, maka kode akan mencetak B, B, B.
- - - - - - - 
Semua _exceptions_ diwariskan dari [BaseException](https://docs.python.org/3/library/exceptions.html#BaseException) sehingga bisa digunakan sebagai _wildcard_ (karakter pengganti). Hal tersebut juga bisa digunakan untuk mencetak pesan _error_ dan memunculkan kembali _exception_:

_**nama file: `8.3-4.py`**_
```python
import sys

try:
    f = open('myfile.txt')
    s = f.readline()
    i = int(s.strip())
except OSError as err:
    print("OS error: {0}".format(err))
except ValueError:
    print("Could not convert data to an integer.")
except BaseException as err:
    print(f"Unexpected {err=}, {type(err)=}")
    raise
```
Selain itu, klausa `except` bisa menghilangkan nama _exception_. Nilai dari _exception_ harus diambil dari `sys.exc_info()[1]`.
- - - - - - - 
Statement `try ... except` memiliki klausa `else` opsional yang jika muncul maka harus mengikuti semua klausa `except`. Hal tersebut berguna untuk kode yang harus dieksekusi jika klausa `try` tidak memunculkan _exception_. Contoh:

_**nama file: `8.3-5.py`**_
```python
for arg in sys.argv[1:]:
    try:
        f = open(arg, 'r')
    except OSError:
        print('cannot open', arg)
    else:
        print(arg, 'has', len(f.readlines()), 'lines')
        f.close()
```
Penggunaan klausa `else` lebih baik daripada menambahkan kode pada klausa `try` karena hal tersebut mencegah program menangkap _exception_ yang tidak dimunculkan oleh kode yang dilindungi oleh statement `try ... except`.
- - - - - - -
Klausa `except` bisa menentukan variabel setelah nama _exception_. Variabel tersebut terikat dengan instance sebuah _exception_ dengan argumen yang disimpan di dalam `instance.args`. Instance tersebut mendefinisikan `__str__()` sehingga argumen dapat dicetak tanpa harus mereferensikan `.args`. Kita juga dapat meng-_instantiate_ sebuah _exception_ terlebih dahulu sebelum memunculkannya dan menambahkan atribut apapun ke dalamnya.

_**nama file: `8.3-6.py`**_
```python
>>> try:
...     raise Exception('spam', 'eggs')
... except Exception as inst:
...     print(type(inst))    # the exception instance
...     print(inst.args)     # arguments stored in .args
...     print(inst)          # __str__ allows args to be printed directly,
...                          # but may be overridden in exception subclasses
...     x, y = inst.args     # unpack args
...     print('x =', x)
...     print('y =', y)
...
<class 'Exception'>
('spam', 'eggs')
('spam', 'eggs')
x = spam
y = eggs
```
Jika _exception_ memiliki argumen, maka argumen-argumen tersebut akan dicetak sebagai bagian terakhir ('detail') dari sebuah pesan untuk _exception_ yang belum ditangani.
- - - - - - - 
Handler _exception_ tidak hanya menangani _exception_ jika _exception_ muncul secara langsung di dalam klausa `try`, tapi juga jika _exception_ muncul di dalam fungsi yang dipanggil di dalam klausa `try`. Contoh:

_**nama file: `8.3-7.py`**_
```python
>>> def this_fails():
...     x = 1/0
...
>>> try:
...     this_fails()
... except ZeroDivisionError as err:
...     print('Handling run-time error:', err)
...
Handling run-time error: division by zero
```

## 8.4. Memunculkan Exception
Statement [raise](https://docs.python.org/3/reference/simple_stmts.html#raise) memungkinkan programmer untuk memaksa _exception_ untuk muncul. Contoh:

_**nama file: `8.4-1.py`**_
```python
>>> raise NameError('HiThere')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: HiThere
```
- - - - - -
Jika kelas _exception_ diteruskan, maka kelas tersebut akan secara implisit diinstansiasi dengan memanggil konstruktor tanpa argumen:

_**nama file: `8.4-2.py`**_
```python
raise ValueError  # shorthand for 'raise ValueError()'
```
- - - - - -
Jika kita ingin menentukan apakah _exception_ harus dimunculkan tetapi kita juga tidak ingin menanganinya, maka kita bisa menggunakan bentuk sederhana dari statement _raise_ untuk memunculkan ulang sebuah _exception_:

_**nama file: `8.4-3.py`**_
```python
try:
...     raise NameError('HiThere')
... except NameError:
...     print('An exception flew by!')
...     raise
```

## 8.5. Exception Chaining (Pengikatan Exception)
Statement [raise](https://docs.python.org/3/reference/simple_stmts.html#raise)  membolehkan pendeklarasian [from](https://docs.python.org/3/reference/simple_stmts.html#raise) yang memungkinkan _exception_ berantai. Contoh:

_**nama file: `8.5-1.py`**_
```python
# exc must be exception instance or None.
raise RuntimeError from exc
```
Hal tersebut bisa berguna ketika kita men-transformasi _exceptions_. Contoh:

_**nama file: `8.5-2.py`**_
```python
>>> def func():
...     raise ConnectionError
...
>>> try:
...     func()
... except ConnectionError as exc:
...     raise RuntimeError('Failed to open database') from exc
...
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
  File "<stdin>", line 2, in func
ConnectionError

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "<stdin>", line 4, in <module>
RuntimeError: Failed to open database
```
- - - - - -
Pengikatan _exception_ terjadi secara otomatis ketika _exception_ dimunculkan di dalam sebuah [except](https://docs.python.org/3/reference/compound_stmts.html#except) atau [finally](https://docs.python.org/3/reference/compound_stmts.html#finally). Hal ini dapat dinonaktifkan dengan menggunakan idiom `None`:

_**nama file: `8.5-3.py`**_
```python
>>> try:
...     open('database.sqlite')
... except OSError:
...     raise RuntimeError from None
...
Traceback (most recent call last):
  File "<stdin>", line 4, in <module>
RuntimeError
```
## 8.6. Exception yang Didefinisikan oleh Pengguna
Program bisa memberi nama _exception_ dengan membuat kelas _exception_ baru. _Exception_ harus diambil dari kelas _exception_, bisa secara langsung maupun tidak langsung.

Kelas _exception_ bisa didefinisikan dan bisa melakukan apapun yang kelas lain bisa lakukan, tetapi biasanya lebih sederhana. Biasanya kelas _exception_ hanya menyediakan kumpulan atribut yang memungkinkan informasi _error_ diekstrak oleh handler untuk _exception_.

Kebanyakan _exception_ didefinisikan dengan nama yang diakhiri dengan "Error", mirip dengan penamaan _exception_ standar.

Banyak modul standar bisa mendefinisikan _exception_ untuk melaporkan error yang muncul di dalam fungsi yang telah didefinisikan.

## 8.7. Mendefinisikan Aksi Pembersihan
Statement `try` memiliki klausa opsional lain yang digunakan untuk mendefinisikan tindakan pembersihan yang harus dieksekusi di dalam segala situasi dan kondisi. Contoh:

_**nama file: `8.7-1.py`**_
```python
>>> try:
...     raise KeyboardInterrupt
... finally:
...     print('Goodbye, world!')
...
Goodbye, world!
KeyboardInterrupt
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
```
Klausa `finally` akan dieksekusi sebagai perintah terakhir sebelum statemen `try` selesai dieksekusi. Klausa `finally` berjalan saat statement `try` memproduksi ataupun juga saat tidak memproduksi sebuah _exception_. Berikut beberapa poin tentang apa saja yang terjadi saat _exception_ muncul:
- Jika _exception_ muncul saat eksekusi klausa `try`, _exception_ bisa ditangani oleh sebuah klausa `except`.
- Sebuah _exception_ dapat muncul saat proses eksekusi klausa `except` atau `else`.
- Jika klausa `finally` mengeksekusi statement [break](https://docs.python.org/3/reference/simple_stmts.html#break), [continue](https://docs.python.org/3/reference/simple_stmts.html#continue), atau [return](https://docs.python.org/3/reference/simple_stmts.html#return), maka _exception_ tidak dimunculkan kembali.
- Jika statement `try` sampai pada [break](https://docs.python.org/3/reference/simple_stmts.html#break), [continue](https://docs.python.org/3/reference/simple_stmts.html#continue), atau [return](https://docs.python.org/3/reference/simple_stmts.html#return), maka klausa `finally` akan dieksekusi sebelum eksekusi statement `break`, `continue`, atau `return`. 
- Jika klausa `finally` mengandung statement `return`, maka nilai yang di-return adalah nilai dari statement `return` milik `finally`, bukan nilai dari statemen `return` milik `try`.

Contoh:
_**nama file: `8.7-2.py`**_
```python
>>> def bool_return():
...     try:
...         return True
...     finally:
...         return False
...
>>> bool_return()
False
```
Contoh yang lebih rumit:
_**nama file: `8.7-3.py`**_
```python
>>> def divide(x, y):
...     try:
...         result = x / y
...     except ZeroDivisionError:
...         print("division by zero!")
...     else:
...         print("result is", result)
...     finally:
...         print("executing finally clause")
...
>>> divide(2, 1)
result is 2.0
executing finally clause
>>> divide(2, 0)
division by zero!
executing finally clause
>>> divide("2", "1")
executing finally clause
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 3, in divide
TypeError: unsupported operand type(s) for /: 'str' and 'str'
```
Seperti yang dapat kiya lihat, klausa `finally` dieksekusi pada seluruh event/kejadian. [TypeError](https://docs.python.org/3/library/exceptions.html#TypeError) muncul karena ada operasi pembagian dua string yang tidak ditangani oleh klausa `except` sehingga `TypeError` dimunculkan ulang setelah klausa `finally` selesai dieksekusi.

## 8.8. Aksi Pembersihan yang Sudah Didefinisikan
Beberapa objek mendefinisikan tindakan pembersihan standar untuk dilakukan ketika objek tidak lagi dibutuhkan, tanpa memedulikan apakah operasi yang menggunakan objek tersebut berhasil atau gagal. Lihatlah contoh berikut, yang mencoba untuk membuka file dan mencetak kontennya ke layar.

_**nama file: `8.8-1.py`**_
```python
for line in open("myfile.txt"):
    print(line, end="")
```
Masalah pada kode ini adalah kode ini membiarkan file terbuka selama beberapa waktu setelah bagian kode di atas selesai dieksekusi. Hal ini bukanlah masalah pada sebuah script sederhana, tetapi bisa menjadi masalah pada aplikasi yang berukuran besar. Statement [with](https://docs.python.org/3/reference/compound_stmts.html#with) memungkinkan objek seperti file bisa digunakan sekaligus memastikan objek tersebut selalu "bersih".

_**nama file: `8.8-2.py`**_
```python
with open("myfile.txt") as f:
    for line in f:
        print(line, end="")
```
Setelah statement dieksekusi, file _f_ selalu ditutup, bahkan ketika masalah ditemukan ketika proses menjalankan kode.
- - - - -
### Yess bab 8 sudah selesai! Merci beaucoup! :nerd_face: