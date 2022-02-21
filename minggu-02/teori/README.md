# 4. CONTROL FLOW
Python menggunakan statement-statement control flow yang sama seperti di bahasa pemrograman lain, tetapi dengan beberapa perbedaan.

## 4.1. Pernyataan `if`
Statement yang paling terkenal adalah statement If. Contoh:

_**nama file: `4.1.py`**_
```python
>>> x = int(input("Please enter an integer: "))
Please enter an integer: 42
>>> if x < 0:
...     x = 0
...     print('Negative changed to zero')
... elif x == 0:
...     print('Zero')
... elif x == 1:
...     print('Single')
... else:
...     print('More')
...
More
```
Python memiliki statement kondisi yaitu `if`, `elif`, dan `else`. Kondisi `if` dapat digunakan untuk mengeksekusi kode yang bernilai `True`. Jika kondisi bernilai `False`, maka `if` tidak akan dianggap dan Python akan mengeksekusi kode milik `elif` atau `else`. 

Di Python ada satu statement kondisi yang penulisannya berbeda dari kebanyakan bahasa pemrograman yaitu `elif`. keyword `elif` merupakan kependekan dari `else if`. statement `elif` ini berguna untuk menghindari indentasi yang berlebihan atau kelewatan. Sementara _sequence_ `if … elif … elif …` merupakan pengganti dari `switch` atau `case` yang biasa ditemukan di bahasa pemrograman lain.

## 4.2. Pernyataan `for`
Statement `for` di Python berbeda dengan `for` di bahasa pemrograman lain seperti C atau Pascal. Di Python, `for` melakukan perulangan pada item-item milik _sequence_ seperti list atau string. Contoh:

_**nama file: `4.2-1.py`**_
```python
>>> # Measure some strings:
... words = ['cat', 'window', 'defenestrate']
>>> for w in words:
...     print(w, len(w))
...
cat 3
window 6
defenestrate 12
```
---------------------
Kita juga bisa melakukan perulangan pada sebuah _collection_ lalu membuat _collection_ baru:

_**nama file: `4.2-2.py`**_
```python
# Membuat sample colllection
users = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}

# Strategi:  Lakukan iterasi pada salinan
for user, status in users.copy().items():
    if status == 'inactive':
        del users[user]

# Strategy:  Buat collection baru
active_users = {}
for user, status in users.items():
    if status == 'active':
        active_users[user] = status
```
## 4.3. Fungsi `range()`
Jika kita tidak perlu melakukan iterasi pada sebuah _sequence_ berisi angka, maka kita bisa menggunakan fungsi _built-in_ `range()`. Fungsi ini menghasilkan sebuah progresi aritmatika:

_**nama file: `4.3-1.py`**_
```python
>>> for i in range(5):
...     print(i)
...
0
1
2
3
4
```
---------------------
Kita bisa membuat range memulai dari angka berapa saja atau menentukan _increment_ yang berbeda:

_**nama file: `4.3-2.py`**_
```python
>>> list(range(5, 10))
[5, 6, 7, 8, 9]

>>> list(range(0, 10, 3))
[0, 3, 6, 9]

>>> list(range(-10, -100, -30))
[-10, -40, -70]
```
---------------------
Untuk melakukan iterasi pada index sebuah _sequence_ kita bisa mengombinasikan fungsi `range()` dan `len()` seperti berikut:

_**nama file: `4.3-3.py`**_
```python
>>> a = ['Mary', 'had', 'a', 'little', 'lamb']
>>> for i in range(len(a)):
...     print(i, a[i])
...
0 Mary
1 had
2 a
3 little
4 lamb
```
Di beberapa kasus tertentu, ada baiknya kita menggunakan fungsi `enumerate()`. Silakan lihat di [Teknik Looping](https://docs.python.org/3/tutorial/datastructures.html#tut-loopidioms).
- - - - - - - -
Keanehan bisa terjadi ketika kita hanya melakukan print pada sebuah range:

_**nama file: `4.3-4.py`**_
```python
>>> range(10)
range(0, 10)
```
- - - - - - - -
Berikut contoh penggunaan `sum` dengan `range()`:

_**nama file: `4.3-5.py`**_
```python
>>> sum(range(4))  # 0 + 1 + 2 + 3
6
```
## 4.4. Pernyataan `break` dan `continue`, dan Klausa `else` pada Loop
Perintah `break` memaksa sebuah perulangan berhenti sebelum waktunya berhenti. Statement loop juga bisa memiliki sebuah klausa `else` yang dieksekusi ketika loop terhenti terjadi _exhaustion_ pada iterator (`for`) atau ketika kondisi bernilai `false` (`while`). Berikut contoh loop untuk menentukan bilangan prima:

_**nama file: `4.4-1.py`**_
```python
>>> for n in range(2, 10):
...     for x in range(2, n):
...         if n % x == 0:
...             print(n, 'equals', x, '*', n//x)
...             break
...     else:
...         # loop gagal tanpa menemukan faktor
...         print(n, 'is a prime number')
...
2 is a prime number
3 is a prime number
4 equals 2 * 2
5 is a prime number
6 equals 2 * 3
7 is a prime number
8 equals 2 * 4
9 equals 3 * 3
```
Bisa kita lihat jika klausa `else` adalah milik `for`, bukan milik statement `if`.

Ketika digunakan dengan loop, klausa `else` lebih memiliki kemiripan dengan klausa `else` milik statement `try` daripada milik statement `if`.
- - - - - - - -
Pernyataan/statement `continue`, melanjutkan iterasi selanjutnya pada sebuah loop:

_**nama file: `4.4-2.py`**_
```python
>>> for num in range(2, 10):
...     if num % 2 == 0:
...         print("Found an even number", num)
...         continue
...     print("Found an odd number", num)
...
Found an even number 2
Found an odd number 3
Found an even number 4
Found an odd number 5
Found an even number 6
Found an odd number 7
Found an even number 8
Found an odd number 9
```
## 4.5. Pernyataan `pass`
Pernyataan/statement `pass` tidak melakukan apapun. `pass` bisa digunakan jika sebuah statement dibutuhkan secara sintaks, tetapi program tidak memerlukan _action_ apapun. Contoh:

_**nama file: `4.5-1.py`**_
```python
>>> while True:
...     pass
...
```
- - - - - - -
`pass` juga biasanya digunakan untuk membuat _minimal class_:

_**nama file: `4.5-2.py`**_
```python
>>> class MyEmptyClass:
...     pass
...
```
- - - - - - -
`pass` juga bisa menjadi _place-holder_ untuk sebuah fungsi ketika kita sedang mengerjakan kode lain:

_**nama file: `4.5-3.py`**_
```python
>>> def initlog(*args):
...     pass   # Jangan lupa beri implementasi di sini!
...
```
## 4.6. Pernyataan `match`
Pernyataan/statement `match` berfungsi untuk membandingkan nilai dengan beberapa pola berbeda sampai cocok:

_**nama file: `4.6-1.py`**_
```python
def http_error(status):
    match status:
        case 400:
            return "Bad request"
        case 404:
            return "Not found"
        case 418:
            return "I'm a teapot"
        case _:
            return "Something's wrong with the internet"
```
- - - - - - -
Kita bisa mengombinasikan beberapa literal hanya dalam satu _pattern_ menggunakan | (“or”):

_**nama file: `4.6-2.py`**_
```python
case 401 | 403 | 404:
    return "Not allowed"
```
- - - - - - -
Kita juga dapat mengikat beberapa variabel:

_**nama file: `4.6-3.py`**_
```python
# point adalah tuple (x, y)
match point:
    case (0, 0):
        print("Origin")
    case (0, y):
        print(f"Y={y}")
    case (x, 0):
        print(f"X={x}")
    case (x, y):
        print(f"X={x}, Y={y}")
    case _:
        raise ValueError("Not a point")
```
- - - - - - -
Jika kita menggunakan class untuk membangun data, kita bisa menggunakan nama class yang diikuti dengan argument list yang berperan sebagai konstruktor yang memiliki kemampuan untuk mengambil atribut ke dalam variabel:

_**nama file: `4.6-4.py`**_
```python
class Point:
    x: int
    y: int

def where_is(point):
    match point:
        case Point(x=0, y=0):
            print("Origin")
        case Point(x=0, y=y):
            print(f"Y={y}")
        case Point(x=x, y=0):
            print(f"X={x}")
        case Point():
            print("Somewhere else")
        case _:
            print("Not a point")
```
- - - - - - -
Kita bisa mendefinisikan posisi tertentu untuk atribut di dalam _pattern_ dengan mengatur `__match_args__` di class yang telah kita buat. Jika sudah ter-set menggunakan (“x”, “y”), maka seluruh _pattern_ selanjutnya akan bernilai sama:

_**nama file: `4.6-5.py`**_
```python
Point(1, var)
Point(1, y=var)
Point(x=1, y=var)
Point(y=var, x=1)
```
- - - - - - -
_Pattern_ dapat dibuat dalam bentuk _nested_. Contoh, jika kita memiliki list point yang pendek, kita bisa mencocokannya seperti ini:

_**nama file: `4.6-6.py`**_
```python
match points:
    case []:
        print("No points")
    case [Point(0, 0)]:
        print("The origin")
    case [Point(x, y)]:
        print(f"Single point {x}, {y}")
    case [Point(0, y1), Point(0, y2)]:
        print(f"Two on the Y axis at {y1}, {y2}")
    case _:
        print("Something else")
```
- - - - - - -
Kita bisa menambahkan klausa `if` pada _pattern_ yang bisa kita sebut sebagai "guard". Jika "guard" bernilai `false`, `match` akan mencoba block case selanjutnya:

_**nama file: `4.6-7.py`**_
```python
match point:
    case Point(x, y) if x == y:
        print(f"Y=X at {x}")
    case Point(x, y):
        print(f"Not on the diagonal")
```
- - - - - - -
_Subpatterns_ dapat diambil menggunakan keyword `as`:

_**nama file: `4.6-8.py`**_
```python
case (Point(x1, y1), Point(x2, y2) as p2): ...
```
- - - - - - -
_Patterns_ dapat menggunakan konstanta yang sudah diberi nama:

_**nama file: `4.6-9.py`**_
```python
from enum import Enum
class Color(Enum):
    RED = 'red'
    GREEN = 'green'
    BLUE = 'blue'

color = Color(input("Enter your choice of 'red', 'blue' or 'green': "))

match color:
    case Color.RED:
        print("I see red!")
    case Color.GREEN:
        print("Grass is green")
    case Color.BLUE:
        print("I'm feeling the blues :(")
```
Jika ingin melihat penjelasan yang lebih detail beserta contoh-contohnya, bisa langsung menuju [PEP 636](https://www.python.org/dev/peps/pep-0636/)

## 4.7. Mendefinisikan Fungsi
Kita bisa membuat fungsi untuk menulis deret Fibonacci:

_**nama file: `4.7-1.py`**_
```python
>>> def fib(n):    # menulis deret Fibonacci sampai n
...     """Print a Fibonacci series up to n."""
...     a, b = 0, 1
...     while a < n:
...         print(a, end=' ')
...         a, b = b, a+b
...     print()
...
>>> # Panggil fungsi yang sudah didefinisikan:
... fib(2000)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597
```
Definisi fungsi mengasosiasikan nama fungsi dengan objek fungsi. Kita juga bisa menggunakan nama fungsi lain untuk me-_refer_ ke objek fungsi tersebut dan bisa juga digunakan untuk mengakses fungsi:
```python
>>> fib
<function fib at 10042ed0>
>>> f = fib
>>> f(100)
0 1 1 2 3 5 8 13 21 34 55 89
```
`fib` bukanlah sebuah fungsi tetapi hanyalah prosedur karena `fib` tidak me-return value. Pada faktanya, bahkan fungsi tanpa statement `return` tetap me-return value. Value ini bisa kita sebut dengan `None`:
```python
>>> fib(0)
>>> print(fib(0))
None
```
- - - - - - - 
_**nama file: `4.7-2.py`**_
```python
>>> def fib2(n):  # return deret Fibonacci sampai n
...     """Return a list containing the Fibonacci series up to n."""
...     result = []
...     a, b = 0, 1
...     while a < n:
...         result.append(a) 
...         a, b = b, a+b
...     return result
...
>>> f100 = fib2(100)    # memanggil fungsi
>>> f100                # menampilkan hasil
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
```
Kode di atas mendemonstrasikan beberapa fitur baru Python yaitu:
- Statement/pernyataan `return` return dengan sebuah value dari fungsi. `return` tanpa expresi argumen me-return `None`
- Statement `result.append(a)` memanggil _method_ dari list object `result`. Method adalah sebuah fungsi milik objek dan diberi nama `obj.methodname`, `obj` adalah objek, dan `methodname` adalah nama dari method yang didefinisikan oleh tipe objek.

## 4.8. Mendefinisikan Fungsi (Lanjutan)
Kita juga bisa mendefinisikan fungsi dengan sejumlah variabel argumen.

### 4.8.1. Nilai Default Argumen
Bentuk yang paling fungsional/berguna adalah yang menentukan nilai default untuk satu atau lebih argumen. Hal ini dapat membuat sebuah fungsi yang dapat dipanggil dengan lebih sedikit argumen. Contoh:

_**nama file: `4.8.1-1.py`**_
```python
def ask_ok(prompt, retries=4, reminder='Please try again!'):
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)
```
Fungsi tersebut dapat dipanggil dengan beberapa cara:
- hanya memberikan argumen wajib: `ask_ok('Do you really want to quit?')`
- memberikan salah satu argumen opsional: `ask_ok('OK to overwrite the file?', 2)`
- memberikan semua argumen: `ask_ok('OK to overwrite the file?', 2, 'Come on, only yes or no!')`
- - - - - - -
Nilai default dievaluasi pada point definisi fungsi di dalam _defining scope_, sehingga kode di bawah ini menghasilkan output 5:

_**nama file: `4.8.1-2.py`**_
```python
i = 5

def f(arg=i):
    print(arg)

i = 6
f()
```
- - - - - - -
**Peringatan**: nilai default hanya akan dievaluasi sekali. Hal ini akan menyebabkan perbedaan jika default adalah objek _mutable_ seperti list, dictionary, atau instance pada class. Misalnya, fungsi di bawah ini mengakumulasi argumen yang dilewatkan:

_**nama file: `4.8.1-3.py`**_
```python
def f(a, L=[]):
    L.append(a)
    return L

print(f(1))
print(f(2))
print(f(3))

#Kode tersebut akan menampilkan output:
[1]
[1, 2]
[1, 2, 3]
```
Jika tidak ingin default dibagikan lewat panggilan _subsequent_, kita bisa menulis fungsi tersebut seperti ini:

_**nama file: `4.8.1-4.py`**_
```python
def f(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L
```
- - - - - - - - - - - 
### 4.8.2. Keyword Arguments
Fungsi juga bisa dipanggil dengan [keyword arguments](https://docs.python.org/3/glossary.html#term-keyword-argument) dengan bentuk `kwarg=value`. Berikut contoh fungsinya:

_**nama file: `4.8.2-1.py`**_
```python
def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")
```
Menerima satu _required argument_ (voltage) dan tiga _optional arguments_(state, action, dan type). Fungsi ini dapat dipanggil dengan cara-cara berikut:
```python
parrot(1000)                                          # 1 positional argument
parrot(voltage=1000)                                  # 1 keyword argument
parrot(voltage=1000000, action='VOOOOOM')             # 2 keyword arguments
parrot(action='VOOOOOM', voltage=1000000)             # 2 keyword arguments
parrot('a million', 'bereft of life', 'jump')         # 3 positional arguments
parrot('a thousand', state='pushing up the daisies')  # 1 positional, 1 keyword
```
Tetapi cara pemanggilan dibawah ini tidak bisa digunakan (invalid):
```python
parrot()                     # required argument missing
parrot(voltage=5.0, 'dead')  # non-keyword argument after a keyword argument
parrot(110, voltage=220)     # duplicate value for the same argument
parrot(actor='John Cleese')  # unknown keyword argument
```
- - - - - - -
Pada pemanggilan fungsi, _keyword arguments_ harus mengikuti _positional arguments_. Semua _keyword arguments_ yang dimasukkan harus cocok setidaknya ke satu argumen yang diterima oleh fungsi. Tidak ada aargumen yang bisa menerima nilai lebih dari sekali. Berikut contoh error:

_**nama file: `4.8.2-2.py`**_
```python
>>> def function(a):
...     pass
...
>>> function(0, a=0)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: function() got multiple values for argument 'a'
```
- - - - - - -
Ketika parameter formal milik `**name` muncul, maka parameter tersebut akan menerima dictionary (lihat artikel [Mapping Types - dict](https://docs.python.org/3/library/stdtypes.html#typesmapping)) yang menampung seluruh _keyword arguments_ kecuali yang sama dengan formal parameter. Misalnya, jika kita mendefinisikan fungsi seperti ini:

_**nama file: `4.8.2-3.py`**_
```python
def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    for kw in keywords:
        print(kw, ":", keywords[kw])
```
Fungsi tersebut bisa dipanggil dengan cara berikut:
```python
cheeseshop("Limburger", "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           shopkeeper="Michael Palin",
           client="John Cleese",
           sketch="Cheese Shop Sketch")
```
hasilnya seperti berikut:
```python
-- Do you have any Limburger ?
-- I'm sorry, we're all out of Limburger
It's very runny, sir.
It's really very, VERY runny, sir.
----------------------------------------
shopkeeper : Michael Palin
client : John Cleese
sketch : Cheese Shop Sketch
```
- - - - - - - 
### 4.8.3. Parameter Spesial
Secara default, argumen dapat dikirimkan ke fungsi Python dengan posisi atau secara eksplisit dengan keyword.

Gambaran definisi fungsi:
```python
def f(pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2):
      -----------    ----------     ----------
        |             |                  |
        |        Positional or keyword   |
        |                                - Keyword only
         -- Positional only
```
catatan: / dan * bersifat opsional

#### 4.8.3.1. Positional-or-Keyword Arguments
Jika / dan * tidak ada pada definisi fungsi, argumen dapat dikirim ke fungsi dengan posisi atau keyword.

#### 4.8.3.2. Positional-Only Parameters
Jika parameter bersifat positional-only, maka urutan parameter dianggap penting dan parameter tidak dapat di-pass dengan keyword. Parameter positional-only ditempatkan sebelum `/` (_forward-slash). `/` digunakan untuk memisahkan parameter positional-only dari parameter lain. Jika tidak ada `/` di definisi fungsi, maka tidak akan ada parameter positional-only.

#### 4.8.3.3. Keyword-Only Arguments
Untuk menandai parameter sebagai keyword-only, maka saat mengindikasi parameter harus di-pass dengan keyword argument, tempatkan `*` di list argumen sebelum parameter keyword-only pertama.

#### 4.8.3.4. Contoh Fungsi
_**nama file: `4.8.3.4.py`**_
```python
>>> def standard_arg(arg):
...     print(arg)
...
>>> def pos_only_arg(arg, /):
...     print(arg)
...
>>> def kwd_only_arg(*, arg):
...     print(arg)
...
>>> def combined_example(pos_only, /, standard, *, kwd_only):
...     print(pos_only, standard, kwd_only)
```
Fungsi definisi pertama, `standard_arg`, tidak menggunakan batasan apapun pada pemanggilan konvensi dan argumen dapat di-pass menggunakan posisi ataupun keyword:
```python
>>> standard_arg(2)
2

>>> standard_arg(arg=2)
2
```
Fungsi kedua yaitu `pos_only_arg` dibatasi sehingga hanya bisa menggunakan parameter positional dan juga ada `/` di definisi fungsi:
```python
>>> pos_only_arg(1)
1

>>> pos_only_arg(arg=1)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: pos_only_arg() got some positional-only arguments passed as keyword arguments: 'arg'
```
Fungsi ketiga yaitu `kwd_only_args` yang hanya membolehkan _keyword arguments_ sebagaimana ditunjukkan oleh tanda `*` di definisi fungsi:
```python
>>> kwd_only_arg(3)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: kwd_only_arg() takes 0 positional arguments but 1 was given

>>> kwd_only_arg(arg=3)
3
```
Dan yang terakhir menggunakan ketiga pemanggilan di dalam definisi fungsi yang sama:
```python
>>> combined_example(1, 2, 3)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: combined_example() takes 2 positional arguments but 3 were given

>>> combined_example(1, 2, kwd_only=3)
1 2 3

>>> combined_example(1, standard=2, kwd_only=3)
1 2 3

>>> combined_example(pos_only=1, standard=2, kwd_only=3)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: combined_example() got some positional-only arguments passed as keyword arguments: 'pos_only'
```
Terakhir, kita tulis definisi fungsi berikut:
```python
def foo(name, **kwds):
    return 'name' in kwds
```
Tidak ada pemanggilan yang dapat me-return nilai `True` karena keyword `name` selalu menyambung ke parameter pertama. Contoh:
```python
>>> foo(1, **{'name': 2})
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: foo() got multiple values for argument 'name'
>>>
```
Tetapi dengan menggunakan `/` (argumen positional-only), pemanggilan dapat me-return nilai True karena pemanggilan membolehkan `name` sebagai positional argument dan `name` sebagai key di dalam keyword arguments:
```python
def foo(name, /, **kwds):
    return 'name' in kwds
>>> foo(1, **{'name': 2})
True
```
#### 4.8.3.5. Rekap
Use case akan menentukan parameter yang mana yang akan digunakan di dalam definisi fungsi:

_**nama file: `4.8.3.5.py`**_
```python
def f(pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2):
```
Petunjuk:
- Gunakan positional-only jika kita ingin nama parameter tidak tersedia untuk user
- Gunakan keyword-only jika nama memiliki arti dan definisi fungsi lebih mudah dipahami.
- Untuk API, gunakan positional-only untuk mencegah gangguan pada perubahan API jika nama parameter diganti.

### 4.8.4. Arbitrary Argument Lists
Terakhir, opsi yang paling jarang digunakan adalah fungsi yang bisa dipanggil dengan sejumlah argumen yang bersifat arbitrary (berubah-ubah). Argumen ini akan dikemas di dalam tuple.

_**nama file: `4.8.4.py`**_
```python
def write_multiple_items(file, separator, *args):
    file.write(separator.join(args))
```
Parameter formal apapun yang muncul setelah parameter `args` adalah argumen keyword-only, yang artinya parameter tersebut hanya dapat digunakan sebagai keyword.
```python
>>> def concat(*args, sep="/"):
...     return sep.join(args)
...
>>> concat("earth", "mars", "venus")
'earth/mars/venus'
>>> concat("earth", "mars", "venus", sep=".")
'earth.mars.venus'
```
### 4.8.5. Membuka/Membongkar Argument Lists
Fungsi built-in `range()` mengekspektasikan argumen start dan stop yang terpisah. Jika kedua argumen tersebut tidak terpisah, maka tulis pemanggilan fungsi dengan operator `*` untuk membongkar argumen dari sebuah list atau tuple:

_**nama file: `4.8.5-1.py`**_
```python
>>> list(range(3, 6)) # panggilan normal dengan argumen terpisah
[3, 4, 5]
>>> args = [3, 6]
>>> list(range(*args)) # panggil dengan argumen yang diambil dari list
[3, 4, 5]
```
- - - - - -
dictionary juga dapat mengirimkan keyword arguments dengan operator `**`:

_**nama file: `4.8.5-2.py`**_
```python
>>> def parrot(voltage, state='a stiff', action='voom'):
...     print("-- This parrot wouldn't", action, end=' ')
...     print("if you put", voltage, "volts through it.", end=' ')
...     print("E's", state, "!")
...
>>> d = {"voltage": "four million", "state": "bleedin' demised", "action": "VOOM"}
>>> parrot(**d)
-- This parrot wouldn't VOOM if you put four million volts through it. E's bleedin' demised !
```
### 4.8.6. Ekspresi Lambda
Fungsi anonim sederhana dapat dibuat dengan keyword [lambda](https://docs.python.org/3/reference/expressions.html#lambda). Fungsi ini me-return penjumlahan dua argumen: `lambda a, b: a+b`. Fungsi lambda dapat digunakan kapanpun fungsi objek dibutuhkan. Secara sintaks, lambda dibatasi hanya dapat menggunakan satu ekspresi saja. Seperti definisi fungsi nested, fungsi lambda dapat me-refer variabel dari sebuah scope:

_**nama file: `4.8.6-1.py`**_
```python
>>> def make_incrementor(n):
...     return lambda x: x + n
...
>>> f = make_incrementor(42)
>>> f(0)
42
>>> f(1)
43
```
- - - - - -
Contoh lain dari penggunaan lambda adalah untuk menjadikan sebuah fungsi sederhana sebagai argumen:

_**nama file: `4.8.6-2.py`**_
```python
>>> pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
>>> pairs.sort(key=lambda pair: pair[1])
>>> pairs
[(4, 'four'), (1, 'one'), (3, 'three'), (2, 'two')]
```
### 4.8.7. String Dokumentasi
- Baris pertama harus pendek, dan menunjukkan kesimpulan utama dari tujuan objek. 
- Jika ada baris lagi, di baris kedua harus kosong, secara visual memisahkan kesimpulan dari deskripsi
- Python parses tidak menghilangkan indentasi dari multi-line string di Python, sehingga tool yang memproses dokumentasi harus melakukan proses _strip_ sendiri.

Berikut contoh dari multi-line docstring:
_**nama file: `4.8.7.py`**_
```python
>>> def my_function():
...     """Do nothing, but document it.
...
...     No, really, it doesn't do anything.
...     """
...     pass
...
>>> print(my_function.__doc__)
Do nothing, but document it.

    No, really, it doesn't do anything.
```
### 4.8.8. Fungsi Anotasi
[Fungsi anotasi](https://docs.python.org/3/reference/compound_stmts.html#function) adalah metadata informasi opsional tentang tipe yang digunakan oleh fungsi user-defined. [Annotations/Anotasi](https://docs.python.org/3/glossary.html#term-function-annotation) disimpan di dalam atribut `__annotations__` milik fungsi sebagai dictionary dan tidak memiliki efek apapun ke bagian lain dari fungsi.

Contoh berikut memiliki required argument, optional argument, dan return value yang sudah dianotasikan:

_**nama file: `4.8.8.py`**_
```python
>>> def f(ham: str, eggs: str = 'eggs') -> str:
...     print("Annotations:", f.__annotations__)
...     print("Arguments:", ham, eggs)
...     return ham + ' and ' + eggs
...
>>> f('spam')
Annotations: {'ham': <class 'str'>, 'return': <class 'str'>, 'eggs': <class 'str'>}
Arguments: spam eggs
'spam and eggs'
```
## 4.9. Intermezzo: Gaya Coding
Di Python, [PEP 8](https://www.python.org/dev/peps/pep-0008/) telah menjadi panduan gaya coding dan sudah banyak digunakan di banyak project. PEP 8 memperkenalkan gaya coding yang sangat _readable_ dan enak dipandang mata. Berikut beberapa poin penting tentang gaya coding:
- Gunakan indentasi sejauh 4 spasi, jangan gunakan tab.
- Ringkas baris sehingga tidak melebihi 79 karakter.
- Gunakan baris kosong untuk memisahkan fungsi dan class.
- Jika memungkinkan, berikan komentar pada baris-baris yang membutuhkan komentar.
- Gunakan docstrings.
- Gunakan spasi di sekitar operator dan setelah koma.
- Beri nama class dan fungsi secara konsisten
- Jangan gunakan encoding yang _fancy_ jika kode dimaksudkan untuk environment internasional
- Jangan gunakan karakter non-ASCII pada identifier.
- - - - - - -
**Yey bab 4 sudah selesai! Thank you!** :cowboy_hat_face:


