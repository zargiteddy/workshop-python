# 6. MODUL
Jika kita keluar dari Python interpreter lalu masuk ke interpreter lagi, maka semua definisi (fungsi dan variabel) yang sudah kita buat akan hilang. Maka dari itu, jika kita ingin membuat program yang panjang, lebih baik kita menggunakan text editor untuk menyiapkan input untuk interpreter dan menjalankannya dengan file tersebut sebagai input (hal ini juga biasa disebut dengan pembuatan _script_). Seiring penulisan program yang semakin panjang, kita bisa memisahnya menjadi beberapa file supaya _maintenance_ nya lebih mudah. Kita mungkin juga ingin menggunakan fungsi yang telah kita tulis di beberapa program tanpa menyalin definisinya ke dalam setiap program.

Untuk mendukung fitur ini, Python memiliki cara untuk meletakkan definisi di dalam sebuah file dan menggunakannya di dalam script atau _instance_ interaktif milik interpreter. File tersebut bisa kita sebut dengan _module_ (modul). Definisi dari modul dapat kita import ke dalam modul lain atau ke dalam _main module_.

Modul adalah sebuah file yang berisi definisi dan statement Python. Nama file adalah nama modul dengan penambahan suffix `.py`. Di dalam sebuah modul, nama modul (string) tersedia sebagai value dari variabel global `__name__`. Sebagai contoh, gunakan text editor untuk membuat file bernama `fibo.py` di sebuah direktori:

_**nama file: `fibo.py`**_
```python
# Fibonacci numbers module

def fib(n): # tulis deret Fibonacci sampai nilai ke-n
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

def fib2(n): # return deret Fibonacci sampai nilai ke-n
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result
```
- - - - - - -
Lalu masuk ke Python interpreter dan import modul fibo:

_**nama file: `6.py`**_
```python
>>> import fibo
```
Hal di atas tidak memasukkan nama fungsi yang didefinisikan di `fibo` ke dalam [symbol table](https://docs.python.org/3/library/symtable.html). Hal tersebut hanya memasukkan nama modul `fibo`. Dengan nama modul tersebut, kita bisa mengakses fungsi:
```python
>>> fibo.fib(1000)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987
>>> fibo.fib2(100)
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
>>> fibo.__name__
'fibo'
```
Jika kita ingin sering menggunakan fungsi, kita bisa menamainya dengan nama lokal:
```python
>>> fib = fibo.fib
>>> fib(500)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377
```
- - - - - - - - - -
## 6.1. Modul: Lanjutan
Sebuah modul dapat berisi statement _executable_ dan definisi fungsi. Statement tersebut dimaksudkan untuk menginisialisasi modul. Statement tersebut hanya dieksekusi pada saat pertama kali nama modil ditemukan di dalam sebuah statement import.

Setiap modul memiliki [symbol table](https://docs.python.org/3/library/symtable.html) privat yang digunakan sebagai _symbol table_ oleh seluruh fungsi yang telah didefinisikan di dalam modul. Lalu, _author_ dari modul tersebut bisa menggunakan variabel global di dalam modul tanpa harus khawatir kalau bentrok dengan variabel global milik user. Di sisi lain, kita juga bisa menyentuh variabel global modul dengan notasi yang sama dengan notasi yang digunakan untuk me-refer ke fungsinya, `modname.itemname`.

Modul juga bisa meng-import modul lain. Kita tidak perlu menempatkan statement [import](https://docs.python.org/3/reference/simple_stmts.html#import) di awal sebuah modul atau script. Nama modul yang telah diimpor akan ditempatkan di dalam _symbol table_ modul global.

Ada sebuah varian statement import yang meng-import nama dari modul langsung ke dalam _symbol table_ modul. Contoh:

_**nama file: `6.1-1.py`**_
```python
>>> from fibo import fib, fib2
>>> fib(500)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377
```
Hal tersebut tidak menampilkan nama modul dari tempat import di _symbol table_ lokal.
- - - - - - - - -
Ada juga varian untuk import semua nama yang didefinisikan oleh modul:

_**nama file: `6.1-2.py`**_
```python
>>> from fibo import *
>>> fib(500)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377
```
Hal tersebut mengimpor semua nama kecuali nama yang diawali dengan _underscore_ (_). Pada kebanyakan kasus, programmer Python tidak menggunakan fasilitas ini karena varian import ini memperkenalkan sebuah set nama yang tidak dikenali ke interpreter, dan bisa memnyembunyikan beberapa hal yang sudah kita definisikan.
- - - - - - 
Jika nama modul diawali dengan `as`, maka nama yang ditulis setelah `as` tersebut menjadi terikat ke modul yang diimpor.

_**nama file: `6.1-3.py`**_
```python
>>> import fibo as fib
>>> fib.fib(500)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377
```
Hal tersebut secara efektif mengimpor modul sama seperti `import fibo`, tetapi dengan satu perbedaan yaitu dengan nama `fib`.
- - - - - -
Penggunaan varian import tersebut juga bisa digunakan dengan memanfaatkan [from](https://docs.python.org/3/reference/simple_stmts.html#from):

_**nama file: `6.1-4.py`**_
```python
>>> from fibo import fib as fibonacci
>>> fibonacci(500)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377
```
- - - - - - -
### 6.1.1. Mengeksekusi Modul sebagai Script
Jika kita menjalankan modul Python menggunakan 
```
python fibo.py <arguments>
```
kode di dalam modul akan dieksekusi sebagaimana kita meng-import modul, tetapi dengan `__name__` diset ke `__main__`. Itu artinya menambahkan kode berikut ke bagian akhir modul:

_**nama file: `6.1.1.py`**_
```python
if __name__ == "__main__":
    import sys
    fib(int(sys.argv[1]))
```
Kita dapat membuat file tersebut bisa digunakan sebagai script dan juga bisa digunakan sebagai modul yang _importable_ (bisa diimport), karena kode yang melakukan _parse_ pada _command line_ hanya berjalan jika modul dieksekusi sebagai file "main":
```python
$ python fibo.py 50
0 1 1 2 3 5 8 13 21 34
```
Jika modul diimport, kode tidak berjalan:
```python
>>> import fibo
>>>
```
- - - - - - -
### 6.1.2. Path Pencarian Modul
Ketika sebuah modul bernama `spam` diimport, maka interpreter akan mencari modul built-in dengan nama `spam`. Jika tidak ditemukan, interpreter akan mencari file bernama `spam.py` di list direktori yang diberikan oleh variabel `sys.path`. [sys.path](https://docs.python.org/3/library/sys.html#sys.path) diinisialisasi dari lokasi berikut:
 - direktori berisi input script
 - [PYTHONPATH](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONPATH)
 - installation-dependent default
 
 Setelah inisialisasi, program Python bisa melakukan modifikasi pada `sys.path`. Direktori yang berisi script yang dijalankan ditempatkan di awal path pencarian, di posisi di depan path library standar. Ini berarti script di direktori tersebut akan di-load di direktori library. 
- - - - - - -
### 6.1.3. File Python yang Dikompilasi
Untuk mempercepat proses loading modul, Python menyimpan (cache) versi _compiled_ setiap modul di dalam direktori `__pycache__` dengan nama `module.version.pyc`, dimana versi ini meng-encode format file _compiled_; pada umumnya berisi nomor versi Python. Contohnya, di CPython release 3.3 versi _compiled_ `spam.py` akan di-cache sebagai `__pycache__/spam.cpython-33.pyc`. Penamaan ini memungkinkan modul _compiled_ dari release berbeda dan versi Python berbeda dapat berdampingan.

Python memeriksa tanggal modifikasi source terhadap versi compiled untuk menentukan apakah source tersebut kadaluarsa dan harus dikompilasi ulang. Modul _compiled_ bersifat _platform-independent_, jadi library yang bersifat sama bisa di-share antar sistem yang memiliki arsitektur yang berbeda.

Beberapa tips untuk expert:
- Kita bisa menggunakan switch [-0](https://docs.python.org/3/using/cmdline.html#cmdoption-O) dan [-00](https://docs.python.org/3/using/cmdline.html#cmdoption-OO) pada Python command untuk mengurangi ukuran modul yang dikompilasi.
- Program tidak berjalan dengan lebih cepat saat di-read dari file `.pyc` daripada saat di-read dari file `.py`.
- Modul [compileall](https://docs.python.org/3/library/compileall.html#module-compileall) bisa menciptakan file `.pyc` untuk seluruh modul di dalam direktori.
- Ada lebih banyak detail di proses ini, termasuk _decision flowchart_ di [PEP 3147](https://www.python.org/dev/peps/pep-3147/).
- - - - - - -
## 6.2. Modul Standar
Python memiliki library modul standar yang dideskripsikan di dokumen terpisah yaitu Python Library Reference. Beberapa modul sudah dibuat di dalam interpreter; hal ini menyediakan akses ke operasi yang bukan merupakan bagian dari inti _language_ yang bertujuan untuk efisiensi atau untuk menyediakan akses ke _primitives_ sistem operasi. Contohnya, modul [winreg](https://docs.python.org/3/library/winreg.html#module-winreg) hanya disediakan di sistem Windows. Ada juga modul yang sudah dibuat di setiap Python interpreter yaitu [sys](https://docs.python.org/3/library/sys.html#module-sys). Variabel `sys.ps1` dan `sys.ps2` mendefinisikan string yang digunakan sebagai prompt primary dan secondary.

_**nama file: `6.2-1.py`**_
```python
>>> import sys
>>> sys.ps1
'>>> '
>>> sys.ps2
'... '
>>> sys.ps1 = 'C> '
C> print('Yuck!')
Yuck!
C>
```
Kedua variabel tersebut terdefinisikan hanya jika interpreter aktif dalam mode interaktif.

Variabel `sys.path` adalah sebuah list string yang menentukan path pencarian milik interpreter. `sys.path` diinisialisasikan ke path default yang diambil dari environment variable [PYTHONPATH](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONPATH), atau dari default built-in jika PYTHONPATH belum diset. Kita bisa memodifikasinya menggunakan operasi _standard list_:

_**nama file: `6.2-2.py`**_
```python
>>> import sys
>>> sys.path.append('/ufs/guido/lib/python')
```
- - - - - - - -
## 6.3. Fungsi `dir()`
fungsi built-in `dir()` digunakan untuk mencari nama mana yang didefinisikan oleh sebuah modul. fungsi tersebut me-return _sorted list_ bertipe string:

_**nama file: `6.3-1.py`**_
```python
>>> import fibo, sys
>>> dir(fibo)
['__name__', 'fib', 'fib2']
>>> dir(sys)
['__breakpointhook__', '__displayhook__', '__doc__', '__excepthook__',
 '__interactivehook__', '__loader__', '__name__', '__package__', '__spec__',
 '__stderr__', '__stdin__', '__stdout__', '__unraisablehook__',
 '_clear_type_cache', '_current_frames', '_debugmallocstats', '_framework',
 '_getframe', '_git', '_home', '_xoptions', 'abiflags', 'addaudithook',
 'api_version', 'argv', 'audit', 'base_exec_prefix', 'base_prefix',
 'breakpointhook', 'builtin_module_names', 'byteorder', 'call_tracing',
 'callstats', 'copyright', 'displayhook', 'dont_write_bytecode', 'exc_info',
 'excepthook', 'exec_prefix', 'executable', 'exit', 'flags', 'float_info',
 'float_repr_style', 'get_asyncgen_hooks', 'get_coroutine_origin_tracking_depth',
 'getallocatedblocks', 'getdefaultencoding', 'getdlopenflags',
 'getfilesystemencodeerrors', 'getfilesystemencoding', 'getprofile',
 'getrecursionlimit', 'getrefcount', 'getsizeof', 'getswitchinterval',
 'gettrace', 'hash_info', 'hexversion', 'implementation', 'int_info',
 'intern', 'is_finalizing', 'last_traceback', 'last_type', 'last_value',
 'maxsize', 'maxunicode', 'meta_path', 'modules', 'path', 'path_hooks',
 'path_importer_cache', 'platform', 'prefix', 'ps1', 'ps2', 'pycache_prefix',
 'set_asyncgen_hooks', 'set_coroutine_origin_tracking_depth', 'setdlopenflags',
 'setprofile', 'setrecursionlimit', 'setswitchinterval', 'settrace', 'stderr',
 'stdin', 'stdout', 'thread_info', 'unraisablehook', 'version', 'version_info',
 'warnoptions']
```
- - - - - - -
Tanpa argumen, `dir()` membuat list berisi nama yang sudah kita definisikan:

_**nama file: `6.3-2.py`**_
```python
>>> a = [1, 2, 3, 4, 5]
>>> import fibo
>>> fib = fibo.fib
>>> dir()
['__builtins__', '__name__', 'a', 'fib', 'fibo', 'sys']
```
Bisa kita perhatikan jika fungsi `dir()` me-list semua tipe nama: variabel, modul, fungsi, dll.
- - - - - - -
`dir()` tidak me-list nama fungsi built-in dan variabel. Jika kita ingin membuat list fungsi built-in dan variabel, kita bisa menggunakan modul standar [builtins](https://docs.python.org/3/library/builtins.html#module-builtins)

_**nama file: `6.3-3.py`**_
```python
>>> import builtins
>>> dir(builtins)  
['ArithmeticError', 'AssertionError', 'AttributeError', 'BaseException',
 'BlockingIOError', 'BrokenPipeError', 'BufferError', 'BytesWarning',
 'ChildProcessError', 'ConnectionAbortedError', 'ConnectionError',
 'ConnectionRefusedError', 'ConnectionResetError', 'DeprecationWarning',
 'EOFError', 'Ellipsis', 'EnvironmentError', 'Exception', 'False',
 'FileExistsError', 'FileNotFoundError', 'FloatingPointError',
 'FutureWarning', 'GeneratorExit', 'IOError', 'ImportError',
 'ImportWarning', 'IndentationError', 'IndexError', 'InterruptedError',
 'IsADirectoryError', 'KeyError', 'KeyboardInterrupt', 'LookupError',
 'MemoryError', 'NameError', 'None', 'NotADirectoryError', 'NotImplemented',
 'NotImplementedError', 'OSError', 'OverflowError',
 'PendingDeprecationWarning', 'PermissionError', 'ProcessLookupError',
 'ReferenceError', 'ResourceWarning', 'RuntimeError', 'RuntimeWarning',
 'StopIteration', 'SyntaxError', 'SyntaxWarning', 'SystemError',
 'SystemExit', 'TabError', 'TimeoutError', 'True', 'TypeError',
 'UnboundLocalError', 'UnicodeDecodeError', 'UnicodeEncodeError',
 'UnicodeError', 'UnicodeTranslateError', 'UnicodeWarning', 'UserWarning',
 'ValueError', 'Warning', 'ZeroDivisionError', '_', '__build_class__',
 '__debug__', '__doc__', '__import__', '__name__', '__package__', 'abs',
 'all', 'any', 'ascii', 'bin', 'bool', 'bytearray', 'bytes', 'callable',
 'chr', 'classmethod', 'compile', 'complex', 'copyright', 'credits',
 'delattr', 'dict', 'dir', 'divmod', 'enumerate', 'eval', 'exec', 'exit',
 'filter', 'float', 'format', 'frozenset', 'getattr', 'globals', 'hasattr',
 'hash', 'help', 'hex', 'id', 'input', 'int', 'isinstance', 'issubclass',
 'iter', 'len', 'license', 'list', 'locals', 'map', 'max', 'memoryview',
 'min', 'next', 'object', 'oct', 'open', 'ord', 'pow', 'print', 'property',
 'quit', 'range', 'repr', 'reversed', 'round', 'set', 'setattr', 'slice',
 'sorted', 'staticmethod', 'str', 'sum', 'super', 'tuple', 'type', 'vars',
 'zip']
```
- - - - - - -
## 6.4. Packages
Package adalah sebuah penataan namespace modul Python dengan menggunakan "_dotted module names_" (nama modul yang diberi tanda titik). Contohnya, modul bernama `A.B` menandai sebuah submodule bernama `B` di dalam package bernama `A`.

Jika kita ingin mendesain sebuah koleksi modul (sebuah "package") untuk meng-handle file dan data sound, ada banyak format sound (biasanya dengan extension seperti `.wav`, `.aiff`, `.au`), jadi kita perlu membuat dan mempertahankan koleksi modul untuk konversi antara beberapa format file sound. Ada juga banyak operasi yang bisa kita gunakan pada data sound (mixing, menambah echo, mengaplikasikan fungsi equalizer, membuat efek stereo buatan). Berikut bentuk struktur package untuk sound:
```
sound/                          Top-level package
      __init__.py               Initialize the sound package
      formats/                  Subpackage for file format conversions
              __init__.py
              wavread.py
              wavwrite.py
              aiffread.py
              aiffwrite.py
              auread.py
              auwrite.py
              ...
      effects/                  Subpackage for sound effects
              __init__.py
              echo.py
              surround.py
              reverse.py
              ...
      filters/                  Subpackage for filters
              __init__.py
              equalizer.py
              vocoder.py
              karaoke.py
              ...
```
Ketika mengimport package, Python mencari subdirektori package lewat direktori pada `sys.path`.

File `__init__.py` dibutuhkan untuk membuat Python memperlakukan atau menganggap direkroti berisi file sebagai package. Pada beberapa kasus, `__init__.py` bisa hanya sekedar file kosong, tetapi juga bisa mengeksekusi insialisasi kode untuk package atau juga bisa men-set variabel `__all__`.

User package bisa mengimport modul individual dari package, contoh:

_**nama file: `6.4-1.py`**_
```python
import sound.effects.echo
```
import tersebut memuat submodule `sound.effects.echo` yang harus direferensikan dengan nama lengkap.
```python
sound.effects.echo.echofilter(input, output, delay=0.7, atten=4)
```
- - - - - - -
Cara alternatif untuk mengimport modul adalah dengan:

_**nama file: `6.4-2.py`**_
```python
from sound.effects import echo
```
Hal tersebut juga memuat echo submodule yang membuatnya _available_ tanpa prefix package:
```python
echo.echofilter(input, output, delay=0.7, atten=4)
```
- - - - - - -
Variasi lain untuk mengimpor fungsi yang diinginkan secara langsung:

_**nama file: `6.4-3.py`**_
```python
from sound.effects.echo import echofilter
```
Hal tersebut memuat submodule echo lagi, tetapi sekaligus membuat fungsi `echofilter()` langsung _available_ (tersedia):
```python
echofilter(input, output, delay=0.7, atten=4)
```
- - - - - - -
### 6.4.1. Mengimpor * dari Package
Apa yang terjadi jika user menulis `from sound.effects import *`? Yang terjadi adalah import tersebut mengecek ke filesystem, mencari submodule mana yang ada di dalam package, dan langsung impor seluruh submodule. Hal ini dapat memakan waktu yang cukup banyak dan juga dapat menyebabkan efek samping tertentu.

Satu-satunya solusi adalah author package harus menyediakan index eksplisit package. Jika `__init__.py` package mendefinisikan sebuah list bernama `__all__`, list tersebut akan dianggap sebagai list nama modul yang wajib diimpor ketika `from package import *` ditemui. Author boleh me-maintain list supaya up-to-date ketika versi baru package sudah dirilis. Author package juga berhak menentukan untuk tidak men-support package tersebut jika author menganggap impor * dari package tidak diperlukan. Contoh, file `sound/effects/__init__.py` dapat berisi kode berikut:

_**nama file: `6.4.1-1.py`**_
```python
__all__ = ["echo", "surround", "reverse"]
```
Ini berarti `sound.effects import *` akan mengimpor 3 submodul dari package sound.
- - - - - -
Jika `__all__` tidak didefinisikan, statement `sound.effects import *` tidak mengimpor semua submodul dari package `sound.effects` ke dalam namespace; statement tersebut hanya memastikan jika package `sound.effects` sudah diimpor sekaligus mengimpor nama apapun yang telah didefinisikan di dalam package. Hal ini juga termasuk semua nama yang didefinisikan oleh `__init__.py`, dan semua submodule package yang dimuat secara eksplisit oleh statement import sebelumnya. Perhatikan kode berikut:

_**nama file: `6.4.1-2.py`**_
```python
import sound.effects.echo
import sound.effects.surround
from sound.effects import *
```
Dalam contoh kode tersebut, modul `echo` dan `surround ` diimpor di dalam current namespace karena modules tersebut didefinisikan di package `sound.effects` ketika statement `from...import` dieksekusi.
- - - - - - - -
### 6.4.2. Referensi Intra-Package
Ketika package disusun ke dalam subpackages, kita bisa melakukan impor absolut untuk untuk me-refer ke submodul _package sibling_. Contohnya, jika modul `sound.filters.vocoder` memerlukan modul `echo` di package `sound.effects`, maka `sound.filters.vocoder` dapat menggunakan `from sound.effects import echo`.

Kita juga dapat menulis import relatif dengan statement `from module import name`. Varian import ini menggunakan dot (tanda titik) untuk menandakan package current dan parent yang berperan di dalam _relative import_ (impor relatif). Dari modul `surround`, kita bisa menggunakan:

_**nama file: `6.4.2.py`**_
```python
from . import echo
from .. import formats
from ..filters import equalizer
```
Bisa kita perhatikan bahwa _relative imports_ berdasar pada nama _current module_. Karena nama _main module_ selalu `"__main__"`, maka modul yang akan digunakan sebagai _main module_ pada aplikasi Python harus menggunakan _absolute imports_ (impor absolut).
- - - - - -
### 6.4.3. Package di dalam Beberapa Direktori
Package mendukung _special attribute_ yaitu `__path__`. `__path__` diinisialisasi sebagai list berisi nama direktori yang memegang `__init__.py` di sebuah package sebelum kode di file tersebut dieksekusi. Variabel ini bisa dimodifikasi; yang jika dilakukan akan memengaruhi pencarian untuk modul dan subpackage yang ada di dalam package. Walau fitur `__path__` ini jarang dibutuhkan, tetap saja fitur tersebut dapat diandalkan untuk memperluas kumpulan modul dan subpackage.
- - - - - - - -
### Bab 6 sudah selesai! Danke schön! :smile:








