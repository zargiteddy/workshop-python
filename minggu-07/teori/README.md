# 9. KELAS
Kelas menyediakan sarana untuk menggabungkan data dan fungsionalitas secara bersamaan. Pembuatan kelas baru akan membuat jenis objek baru, yang memungkinkan _instance_ baru dari jenis objek tersebut dibuat. Setiap _instance_ kelas bisa memiliki atribut yang terikat ke _instance_ tersebut untuk untuk mempertahankan statusnya. _Instance_ kelas juga bisa memiliki method (didefinisikan oleh kelasnya) untuk memodifikasi status.

Kelas di Python menyediakan seluruh fitur standar _Object Oriented Programming_: mekanisme turunan/warisan kelas memungkinkan adanya beberapa kelas _base_, kelas _derived_ bisa meng-_override_ semua method milik kelas _base_ atau kelas yang lain, dan sebuah method dapat memanggil method dari kelas _base_ dengan nama yang sama.

## 9.1. Beberapa hal Tentang Nama dan Objek
Objek memiliki individualitas, dan beberapa nama (di dalam beberapa scope) dapat terikat ke objek yang sama. Hal ini biasa dikenal dengan nama _aliasing_. Hal ini bisa diabaikan ketika berhadapan dengan number, string, atau tuple. Walau begitu, _aliasing_ memeiliki kemampuan atau efek pada kode semantik Python seperti objek _mutable_ (list, dictionary, dll).

## 9.2. Scope dan Namespace pada Python
_Namespace_ adalah kumpulan nama yang digunakan untuk mengenali atau me-refer ke objek. Contoh dari _namespace_: kumpulan nama built-in (berisi fungsi seperti [abs()](https://docs.python.org/3/library/functions.html#abs)), dan nama _exception_ built-in; nama global di modul; dan nama lokal di invokasi fungsi. Hal yang patut diperhatikan pada _namespace_ adalah tidak ada hubungan antara setiap nama pada _namespace_ yang berbeda. Misalnya, dua modul berbeda bisa mendefinisikan sebuah fungsi `maximize` tanpa terjadi kekeliruan.

Kita bisa menggunakan `attribute` untuk nama setelah titik. Contohnya, pada ekspresi `z.real`, `real` adalah atribut dari objek `z`. Referensi ke nama dalam modul adalah referensi atribut. Pada ekspresi `modname.funcname`, `modname` adalah objek modul dan `funcname` adalah atributnya. Pada kasus tersebut ada proses _mapping_ diantara atribut modul dan nama global yang didefinisikan di dalam modul: dua hal tersebut memiliki _namespace_ yang sama.

Atribut bisa bersifat _read-only_ (dibaca) atau _writable_ (ditulis). Pada kasus _writable_, kita bisa menulis `modname.the_answer = 42`. Atribut _writable_ juga bisa dihapus dengan statement [del](https://docs.python.org/3/reference/simple_stmts.html#del). Contohnya, `del modname.the_answer` akan menghapus atribut `the_answer` dari objek yang bernama `modname`.

_Namespace_ dibuat pada waktu yang berbeda dan memiliki umur yang berbeda pula. _Namespace_ yang berisi nama-nama _built-in_ dibuat ketika Python interpreter dijalankan, dan tidak pernah dihapus. _Namespace_ global untuk modul dibuat ketika definisi modul dimasukkan; biasanya, _namespace_ modul bertahan hingga interpreter berhenti. Statement yang dieksekusi oleh invokasi _top-level_ interpreter, yang dibaca dari file script atau secara interaktif, akan dianggap sebagai bagian dari modul bernama `__main__`, sehingga statement tersebut memiliki _namespace_ global sendiri.

_Namespace_ lokal untuk fungsi dibuat ketika fungsi dipanggil, dan dihapus ketika fungsi me-return atau memunculkan sebuah _exception_ yang tidak ditangani di dalam fungsi.

_Scope_ adalah bagian tekstual dari program Python dimana _namespace_ dapat langsung diakses. "dapat langsung diakses" berarti referensi yang tidak dikualifikasi pada sebuah nama mencoba untuk menemukan nama di dalam _namespace_.

Walaupun scope ditentukan secara statis, scope digunakan secara dinamis. Pada proses eksekusi, ada 3 atau 4 _nested scope_ yang _namespace_-nya dapat langsung diakses:
- Scope _innermost_ (bagian paling dalam), yang dicari pertama dan berisi nama lokal.
- Scope dari fungsi _enclosing_ (dilampirkan), yang proses pencariannya dimulai dari _enclosing scope_ terdekat, berisi nama non-lokal dan nama non-global.
- Scope _outermost_ (bagian paling luar) dicari paling akhir. Scope ini adalah _namespace_ yang berisi nama-nama built-in.

Jika nama dideklarasikan secara global, maka semua referensi dan _assignment_ langsung berpindah ke _middle scope_ yang berisi nama global modul. Untuk menyatukan ulang variabel yang ada di luar _innermost scope_, statement [nonlocal](https://docs.python.org/3/reference/simple_stmts.html#nonlocal) bisa digunakan; jika tidak dideklarasikan secara nonlokal, maka variabel tersebut bersifat _read-only_.

Biasanya, scope lokal mereferensikan nama lokal milik fungsi. Di luar fungsi, scope lokal mereferensikan _namespace_ yang sama sebagai scope global: _namespace_ milik modul.

Jika statement [global](https://docs.python.org/3/reference/simple_stmts.html#global) atau [nonlocal](https://docs.python.org/3/reference/simple_stmts.html#nonlocal) berlaku – _assignment_ ke nama akan selalu berpindah ke dalam scope _innermost_. _Assignment_ tidak menyalin data — tetapi hanya mengikat nama ke objek. Hal yang sama berlaku untuk penghapusan: statement `del x` menghapus pengikatan `x` dari _namespace_ yang direferensikan oleh scope lokal. Semua operasi yang memperkenalkan nama baru pasti menggunakan scope lokal: contohnya, statement [import](https://docs.python.org/3/reference/simple_stmts.html#import) dan definisi fungsi mengikat modul atau nama fungsi di dalam scope lokal.

Statement `global` bisa digunakan untuk menunjukkan variabel tertentu yang ada di dalam scope global dan harus _rebound_ di sana; statement `nonlocal` menunjukkan variabel tertentu yang ada di dalam _enclosing scope_ dan harus _rebound_ dari sana.

### 9.2.1. Contoh Scope dan Namespace
Di bawah ini adalah contoh demonstrasi untuk mereferensikan scope dan namespace yang berbeda, dan bagaimana `global` dan `nonlocal` mempengaruhi pengikatan variabel:

_**nama file: `9.2.1.py`**_
```python
def scope_test():
    def do_local():
        spam = "local spam"

    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"

    def do_global():
        global spam
        spam = "global spam"

    spam = "test spam"
    do_local()
    print("After local assignment:", spam)
    do_nonlocal()
    print("After nonlocal assignment:", spam)
    do_global()
    print("After global assignment:", spam)

scope_test()
print("In global scope:", spam)
```
Output:
```python
After local assignment: test spam
After nonlocal assignment: nonlocal spam
After global assignment: nonlocal spam
In global scope: global spam
```
Bisa kita perhatikan bahwa _assignment_ lokal tidak mengganti _binding_ (pengikatan) _scope-test_ milik _spam_. _Assignment_ `nonlocal` mengganti _binding_ _scope-test_ milik _spam_, dan _assignment_ global mengganti _binding_ dari _module-level_.

## 9.3. Pendahuluan tentang Kelas
Kelas memperkenalkan kita kepada sintaks baru, tiga jenis objek baru, dan beberapa semantik baru.

### 9.3.1. Syntax Definisi Kelas
Bentuk paling sederhana dari definisi kelas adalah seperti berikut:

_**nama file: `9.3.1.py`**_
```python
class ClassName:
    <statement-1>
    .
    .
    .
    <statement-N>
```
Definisi kelas, seperti definisi fungsi harus dieksekusi sebelum definisi kelas memberi efek saat dijalankan. Statement di dalam definisi kelas biasanya akan menjadi definisi fungsi, tetapi statement lain juga dibolehkan, dan bisa berguna.

Ketika definisi kelas dimasuki, _namespace_ baru dibuat, dan digunakan sebagai scope lokal — jadinya, semua _assignment_ yang menuju variabel lokal akan berpindah ke _namespace_ baru tersebut. Pada praktik tersebut, definisi fungsi mengikat nama dari fungsi baru.

Ketika definisi kelas ditinggalkan, maka objek kelas dibuat. Hal ini pada dasarnya adalah _wrapper_ (pembungkusan) diantara konten dari _namespace_ yang dibuat oleh definisi kelas. Scope lokal original dipulihkan, dan objek kelas terikat ke nama kelas yanf ada di _header_ definisi kelas. (Contoh: `ClassName`).

### 9.3.2. Objek Kelas
Kelas objek mendukung dua jenis operasi: referensi atribut dan instansiasi (pembuatan objek).

Referensi atribut menggunakan syntax standar yang digunakan untuk seluruh referensi atribut di Python: `obj.name`. Nama atribut valid adalah semua nama yang ada di dalam _namespace_ kelas ketika objek kelas dibuat. Contoh definisi kelas:

_**nama file: `9.3.2-1.py`**_
```python
class MyClass:
    """A simple example class"""
    i = 12345

    def f(self):
        return 'hello world'
```
`MyClass.i` dan `MyClass.f` adalah referensi atribut valid yang me-return integer dan objek fungsi. Atribut kelas juga bisa ditetapkan, jadi kita bisa mengganti nilai milik `MyClass.i` dengan _assignment_. `__doc__` juga merupakan atribut valid yang me-return docstring milik kelas: `"A simple example class"`.
- - - - 
Instansiasi kelas menggunakan notasi fungsi. Pada dasarnya, objek kelas adalah fungsi tanpa parameter yang me-return _instance_ baru milik kelas. Contoh:

_**nama file: `9.3.2-2.py`**_
```python
x = MyClass()
```
Kode tersebut menciptakan _instance_ baru milik kelas dan memasukkan objek ke variabel lokal x.
- - - - -
Operasi instansiasi ("memanggil" objek kelas) menciptakan objek kosong. Sebuah kelas bisa mendefinisikan method istimewa bernama `__init__()`, seperti ini:

_**nama file: `9.3.2-3.py`**_
```python
def __init__(self):
    self.data = []
```
- - - - - -
Ketika sebuah kelas mendefinisikan method `__init__()`, instansiasi kelas secara otomatis membangkitkan `__init__()` untuk _instance_ kelas yang baru dibuat. _Instance_ baru yang diinisialisasi bisa diperoleh dengan:

_**nama file: `9.3.2-2.py`**_
```python
x = MyClass()
```
- - - - -
Method `__init__()` bisa memiliki argumen untuk fleksibilitas yang lebih baik. Pada kasus seperti itu, argumen yang diberikan ke operator instansiasi kelas diteruskan ke `__init__()`. Contoh:

_**nama file: `9.3.2-4.py`**_
```python
>>> class Complex:
...     def __init__(self, realpart, imagpart):
...         self.r = realpart
...         self.i = imagpart
...
>>> x = Complex(3.0, -4.5)
>>> x.r, x.i
(3.0, -4.5)
```

### 9.3.3. Objek Instance
Ada dua jenis nama atribut valid: atribut data dan method. Atribut data tidak perlu dideklarasikan; seperti variabel lokal, atribut data muncul ketika pertama kali dipanggil. Sebagai contoh, jika x adalah _instance_ dari `MyClass`, potongan kode berikut akan mencetak value `16`, tanpa menyisakan jejak:

_**nama file: `9.3.3.py`**_
```python
x.counter = 1
while x.counter < 10:
    x.counter = x.counter * 2
print(x.counter)
del x.counter
```
Jenis lain dari referensi atribut _instance_ adalah method. Method adalah fungsi yang "dimiliki" oleh sebuah objek.

Nama method valid dari sebuah objek _instance_ bergantung pada kelasnya. Menurut definisi, semua atribut dari kelas yang merupakan objek fungsi mendefinisikan method yang sesuai dari _instance_-nya. Contohnya, `x.f` adalah sebuah referensi method valid karena `MyClass.f` adalah fungsi, tapi `x.i` bukan referensi method valid karena `MyClass.i` bukan sebuah fungsi. Tetapi, `x.f` bukanlah hal yang sama dengan `MyClass.f` — `x.f` adalah objek method, bukan objek fungsi.

### 9.3.4. Objek Method
Biasanya, sebuah method dipanggil setelah method tersebut 'terikat':

```python
x.f()
```
Pada contoh `MyClass`, hal tersebut akan me-return string `'hello world'`. Kita tidak perlu langsung memanggil method: `x.f ` adalah objek method, dan bisa disimpan dan dipanggil suatu saat. Contoh:

_**nama file: `9.3.4.py`**_
```python
xf = x.f
while True:
    print(xf())
```
Kode di atas akan terus mencetak `'hello world'` selamanya.

Hal istimewa tentang method adalah objek _instance_ diteruskan sebagai argumen pertama dari fungsi. Pada contoh tersebut, `x.f()` setara dengan `MyClass.f(x)`. Secara umum, memanggil method dengan list berisi argumen `n` setara dengan memanggil fungsi yang sesuai dengan list argumen yang dibuat dengan memasukkan _instance_ method sebelum argumen pertama.

Ketika atribut non-data dari sebuah _instance_ direferensikan, kelas dari _instance_ akan langsung dicari. Jika namanya menunjukkan atribut kelas valid yang merupakan objek fungsi, objek method dibuat dengan membungkus objek _instance_ dan objek _fungsi_ yang ditemukan bersamaan di dalam objek abstrak. Ketika objek method dipanggil dengan list argumen, list argumen baru dibangun dari objek _instance_ dan list argumen, dan objek fungsi dipanggil dengan list argumen baru tersebut.

### 9.3.5. Kelas dan Variabel Instance
Variabel instance adalah untuk data yang unik terhadap setiap _instance_ dan variabel kelas adalah untuk atribut dan method yang dibagikan oleh semua _instance_ milik kelas:

_**nama file: `9.3.5-1.py`**_
```python
class Dog:

    kind = 'canine'         # class variable shared by all instances

    def __init__(self, name):
        self.name = name    # instance variable unique to each instance

>>> d = Dog('Fido')
>>> e = Dog('Buddy')
>>> d.kind                  # shared by all dogs
'canine'
>>> e.kind                  # shared by all dogs
'canine'
>>> d.name                  # unique to d
'Fido'
>>> e.name                  # unique to e
'Buddy'
```
- - - - - 
Data bersama (data yang saling dibagikan) bisa memiliki efek mengejutkan dengan menyertakan objek [mutable](https://docs.python.org/3/glossary.html#term-mutable) seperti list dan dictionary. Sebagai contoh, list _tricks_ pada kode di bawah tidak seharusnya digunakan sebagai variabel kelas karena satu list saja bisa dibagikan oleh _instance_ Dog:

_**nama file: `9.3.5-2.py`**_
```python
class Dog:

    def __init__(self, name):
        self.name = name
        self.tricks = []    # creates a new empty list for each dog

    def add_trick(self, trick):
        self.tricks.append(trick)

>>> d = Dog('Fido')
>>> e = Dog('Buddy')
>>> d.add_trick('roll over')
>>> e.add_trick('play dead')
>>> d.tricks
['roll over']
>>> e.tricks
['play dead']
```
## 9.4. Remark Acak
Jika nama atribut yang sama muncul dalam sebuah _instance_ dan dalam sebauh kelas, maka pencarian atribut memprioritaskan _instance_:

_**nama file: `9.4-1.py`**_
```python
>>> class Warehouse:
        purpose = 'storage'
        region = 'west'

>>> w1 = Warehouse()
>>> print(w1.purpose, w1.region)
storage west
>>> w2 = Warehouse()
>>> w2.region = 'east'
>>> print(w2.purpose, w2.region)
storage east
```
Atribut data bisa direferensikan dengan method atau oleh "client" dari objek. Kelas tidak bisa digunakan untuk mengimplementasikan tipe data abstrak.

Client harus menggunakan atribut data dengan hati-hati — client bisa mengacaukan invarian yang dimaintain oleh metode dengan memberi _stamp_ (cap) pada atribut datanya. Client bias menambahkan atribut data mereka sendiri pada objek _instance_ tanpa memengaruhi validitas method, selama konflik nama bisa dihindari.
- - - - - - -
Seringkali argumen pertama bernama `self`. Hal tersebut hanyalah konvensi: nama `self` tidak memiliki arti spesial.

Setiap fungsi yang merupakan atribut kelas mendefinisikan sebuah method untuk _instance_ kelas tersebut. Definisi fungsi tidak perlu terlampir secara tekstual di dalam definisi kelas: memasukkan objek fungsi ke variabel lokal di dalam kelas juga diperbolehkan. Contoh:

_**nama file: `9.4-2.py`**_
```python
# Function defined outside the class
def f1(self, x, y):
    return min(x, x+y)

class C:
    f = f1

    def g(self):
        return 'hello world'

    h = g
```
`f`,`g`, dan `h` adalah atribut milik kelas C yang me-refer ke objek fungsi, yang membuat atribut-atribut tersebut menjadi method _instance_ milik C — dengan `h` menjadi setara dengan `g`.
- - - - - -
Method bisa memanggil method lain dengan atribut method milik argumen `self`:

_**nama file: `9.4-3.py`**_
```python
class Bag:
    def __init__(self):
        self.data = []

    def add(self, x):
        self.data.append(x)

    def addtwice(self, x):
        self.add(x)
        self.add(x)
```
Method bisa mereferensikan nama global seperti fungsi lain. Scope global yang diasosiasikan dengan method adalah modul yang berisi definisi.

Setiap value adalah objek yang memiliki kelas yang disimpan dengan nama `object.__class__`.

## 9.5. Inheritance (Pewarisan)
Tampilan syntax dari kelas sub (derived):

_**nama file: `9.5-1.py`**_
```python
class DerivedClassName(BaseClassName):
    <statement-1>
    .
    .
    .
    <statement-N>
```
Nama `BaseClassName` harus didefinisikan di dalam scope yang mengandung definisi subclass. Kita juga bisa menuliskan ekspresi lain di tempat `BaseClassName`. Hal ini bisa berguna ketika base class didefinisikan di dalam modul lain:

_**nama file: `9.5-2.py`**_
```python
class DerivedClassName(modname.BaseClassName):
```
Eksekusi definisi derived class (subclass) berlangsung sama seperti base class. Ketika objek kelas dibentuk, case class akan diingat. Hal tersebut berguna untuk mengatasi referensi atribut.

`DerivedClassName()` membuat _instance_ baru pada kelas. Referensi method diatasi dengan cara berikut: atribut kelas dicari, dan referensi method valid jika proses ini menghasilkan objek fungsi.

Derived class bisa meng-override method milik base class. Karena method tidak memiliki hak istimewa ketika memanggil objek lain milik objek yang sama, method milik base class yang memanggil method lain yang didefinisikan di dalam base class yang sama bisa memanggil method milik derived class yang meng-override method.

Ada cara sederhana untuk memanggil method base class yaitu dengan memanggil `BaseClassName.methodname(self, arguments)`.

Python memiliki dua fungsi built-in pada inheritance:
- Gunakan [isinstance()](https://docs.python.org/3/library/functions.html#isinstance) untuk memeriksa tipe _instance_: `isinstance(obj, int)` akan bernilai `True` jika `obj.__class__ is` bertipe int atau ada derived class dari int.
- Gunakan [issubclass()](https://docs.python.org/3/library/functions.html#issubclass) untuk memeriksa inheritance: `issubclass(bool, int)` bernilai `True` karena `bool` adalah subclass dari `int`. Tetapi `issubclass(float, int)` bernilai False karena `float` bukanlah subclass dari `int`.

### 9.5.1. Multiple Inheritance
Python mendukung bentuk multiple inheritance (pewarisan banyak/ganda). Berikut tampilan definisi kelas dengan beberapa base class:

_**nama file: `9.5.1.py`**_
```python
class DerivedClassName(Base1, Base2, Base3):
    <statement-1>
    .
    .
    .
    <statement-N>
```

## 9.6. Variabel Privat
Di Python, tidak ada variabel _instance_ "privat" yang tidak bisa diakses kecuali dari dalam objek. Walau begitu, ada konvensi yang diikuti oleh kebanyakan kode Python: nama yang di-prefix atau diawali dengan underscore (Contoh: `_spam`) harus diperlakukan sebagai bagian non-public dari API. Hal tersebut harus dianggap sebagai detail implementasi dan dapat berubah tanpa pemberitahuan.

Pembagian/pemotongan (mangling) nama digunakan untuk memungkinkan subclass untuk meng-override method tanpa memengaruhi pemanggilan method intraclass. Contoh:

_**nama file: `9.6.py`**_
```python
class Mapping:
    def __init__(self, iterable):
        self.items_list = []
        self.__update(iterable)

    def update(self, iterable):
        for item in iterable:
            self.items_list.append(item)

    __update = update   # private copy of original update() method

class MappingSubclass(Mapping):

    def update(self, keys, values):
        # provides new signature for update()
        # but does not break __init__()
        for item in zip(keys, values):
            self.items_list.append(item)
```
Contoh di atas bisa bekerja bahkan jika `MappingSubclass` memperkenalkan identifier `__update` karena diganti dengan `_Mapping__update` di dalam `Mapping class` dan `_MappingSubclass__update` di dalam `MappingSubclass`.

Perhatikan jika kode yang diteruskan ke `exec()` atau `eval()` tidak menganggap classname kelas yang di-invoke untuk menjadi current class; hal ini mirip dengan efek statement global.

## 9.7. Odds dan Ends
Ada manfaatnya memiliki tipe data yang mirip dengan "record" pada Pascal dan "struct pada C, yang membungkus beberapa item data. Definisi kelas empty:

_**nama file: `9.7.py`**_
```python
class Employee:
    pass

john = Employee()  # Create an empty employee record

# Fill the fields of the record
john.name = 'John Doe'
john.dept = 'computer lab'
john.salary = 1000
```
Kode Python yang memerlukan tipe data tertentu dapat diteruskan ke kelas yang meniru method dari tipe data tersebut. Misalnya, jika kita memiliki fungsi yang mem-format beberapa data dari objek file, kita bisa mendefinisikan sebuah kelas dengan method `read()` dan `readline()` yang mendapatkan data dari string buffer, dan meneruskannya sebagai argumen.

Objek method _instance_ memiliki atribut juga: `m.__self__` adalah objek _instance_ dengan method `m()`, dan `m.__func__` adalah objek fungsi yang sesuai dengan method.

## 9.8. Iterator
Kebanyakan objek container bisa di-loop menggunakan statement [for](https://docs.python.org/3/reference/compound_stmts.html#for):
_**nama file: `9.8-1.py`**_
```python
for element in [1, 2, 3]:
    print(element)
for element in (1, 2, 3):
    print(element)
for key in {'one':1, 'two':2}:
    print(key)
for char in "123":
    print(char)
for line in open("myfile.txt"):
    print(line, end='')
```
Style akses tersebut jelas, ringkas, dan mudah dibuat. Penggunaan iterator meliputi dan menyatukan Python. statement `for` memanggil [iter()](https://docs.python.org/3/library/functions.html#iter) pada objek container. Fungsi me-return objek iterator yang mendefinisikan method `__next__()` yang mengakses elemen di dalam container. Ketika tidak ada lagi elemen, `__next__()`memunculkan _exception_ [StopIteration](https://docs.python.org/3/library/exceptions.html#StopIteration) yang memberi tahu loop `for` untuk mengakhiri proses. Kita bisa memanggil method `__next__()` menggunakan fungsi built-in `__next__()`, berikut contohnya:

_**nama file: `9.8-2.py`**_
```python
>>> s = 'abc'
>>> it = iter(s)
>>> it
<str_iterator object at 0x10c90e650>
>>> next(it)
'a'
>>> next(it)
'b'
>>> next(it)
'c'
>>> next(it)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    next(it)
StopIteration
```
Setelah melihat cara kerja protokol iterator, kita dapat dengan mudah menambahkan behavior iterator ke kelas. Definisikan method `__iter__()` yang me-return objek dengan method `__next__()`. Jika kelas mendefinisikan `__next__()`, maka `__iter__()` dapat hanya me-return `self`:

_**nama file: `9.8-3.py`**_
```python
class Reverse:
    """Iterator for looping over a sequence backwards."""
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]

>>> rev = Reverse('spam')
>>> iter(rev)
<__main__.Reverse object at 0x00A1DB50>
>>> for char in rev:
...     print(char)
...
m
a
p
s
```

## 9.9. Generator
[Generator](https://docs.python.org/3/glossary.html#term-generator) adalah tool untuk membuat iterator. Tool tersebut ditulis seperti fungsi pada umumnya menggunakan statement [yield](https://docs.python.org/3/reference/simple_stmts.html#yield) kapanpun generator ingin me-return data. Setiap kali `next()` dipanggil, generator melanjutkan dari titik yang ditinggalkan. Contoh membuat generator:

_**nama file: `9.9.py`**_
```python
def reverse(data):
    for index in range(len(data)-1, -1, -1):
        yield data[index]

>>> for char in reverse('golf'):
...     print(char)
...
f
l
o
g
```
Apapun yang bisa dilakukan dengan generator juga bisa dilakukan dengan iterator class-based. Yang membuat generator sangat _compact_ adalah method `__iter__()` dan `__next__()` dibuat secara otomatis.

Fitur lainnya adalah variabel lokal dan status eksekusi secara otomatis disimpan diantara panggilan-panggilan. Hal ini membuat fungsi dapat ditulis dengan lebih mudah dan jelas daripada menggunakan variabel _instance_ seperti `self.index` dan `self.data`.

## 9.10. Ekspresi Generator
Ekspresi generator lebih ringkas tetapi kurang fleksibel jika dibandingkan dengan definisi generator lengkap. Ekspresi juga generator cenderung lebih ramah memori. Ekspresi generator didesain untuk situasi ketika generator langsung digunakan dengan fungsi _enclosing_.

Contoh:

_**nama file: `9.10.py`**_
```python
class Student:
    gpa = 0
    name = ""

print(sum(i*i for i in range(10)))                 

xvec = [10, 20, 30]
yvec = [7, 5, 3]
print(sum(x*y for x,y in zip(xvec, yvec)))        

page = "hello world"
unique_words = set(word for line in page  for word in line.split())
print(unique_words)

student = Student()
student.gpa = 4
student.name = "Argi"

student2 = Student()
student2.gpa = 3
student2.name = "Bun-Bun"

graduates = [student, student2]

valedictorian = max((student.gpa, student.name) for student in graduates)
print(valedictorian) #menampilkan data dengan nilai terbesar diantara 2 data

data = 'golf'
list = (list(data[i] for i in range(len(data)-1, -1, -1)))
print(list)
```
output:
```Python
285
260
{'e', 'h', 'l', 'r', 'd', 'o', 'w'}
(4, 'Argi')
['f', 'l', 'o', 'g']
```
- - - - - -
### Bab 9 sudah selesai! Echt heel erg bedankt! :sunglasses:
