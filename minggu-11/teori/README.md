# TUTORIAL FLASK

Tutorial ini akan memandu kita untuk membuat aplikasi blog sederhana bernama Flaskr. Pengguna bisa mendaftar, login, membuat post, dan mengedit atau menghapus post mereka. Kita juga bisa menginstall aplikasi pada perangkat komputer lain.

Fask sangat fleksibel. Flask tidak membutuhkan proyek atau layout kode tertentu. Walaupun begitu, lebih baik saat memulai pertama kali kita menggunakan pendekatan yang terstruktur. Tutorial ini memerlukan sedikit _boilerplate_ di awal yang dilakukan untuk menghindari beberapa jebakan yang dihadapi oleh para developer baru sekaligus untuk menciptakan proyek yang mudah untuk dikembangkan. Setelah kita merasa lebih nyaman dengan Flask, kita dapat keluar dari struktur tersebut dan memanfaatkan sepenuhnya fleksibilitas Flask.

Sebelum memulai tutorial ini, kita install Flask terlebih dahulu:
```python
(workshop) zargiteddy@shield:~$ conda install flask
Collecting package metadata (current_repodata.json): done
Solving environment: done

## Package Plan ##

  environment location: /home/zargiteddy/miniconda3/envs/workshop

  added / updated specs:
    - flask


The following packages will be downloaded:

    package                    |            build
    ---------------------------|-----------------
    click-8.0.4                |  py310h06a4308_0         156 KB
    dataclasses-0.8            |     pyh6d0b6a4_7           8 KB
    flask-2.0.3                |     pyhd3eb1b0_0          76 KB
    itsdangerous-2.0.1         |     pyhd3eb1b0_0          18 KB
    jinja2-3.0.3               |     pyhd3eb1b0_0         106 KB
    markupsafe-2.0.1           |  py310h7f8727e_0          35 KB
    werkzeug-2.0.3             |     pyhd3eb1b0_0         221 KB
    ------------------------------------------------------------
                                           Total:         619 KB

The following NEW packages will be INSTALLED:

  click              pkgs/main/linux-64::click-8.0.4-py310h06a4308_0
  dataclasses        pkgs/main/noarch::dataclasses-0.8-pyh6d0b6a4_7
  flask              pkgs/main/noarch::flask-2.0.3-pyhd3eb1b0_0
  itsdangerous       pkgs/main/noarch::itsdangerous-2.0.1-pyhd3eb1b0_0
  jinja2             pkgs/main/noarch::jinja2-3.0.3-pyhd3eb1b0_0
  markupsafe         pkgs/main/linux-64::markupsafe-2.0.1-py310h7f8727e_0
  werkzeug           pkgs/main/noarch::werkzeug-2.0.3-pyhd3eb1b0_0


Proceed ([y]/n)? y


Downloading and Extracting Packages
flask-2.0.3          | 76 KB     | ######################################### | 100% 
itsdangerous-2.0.1   | 18 KB     | ######################################### | 100% 
werkzeug-2.0.3       | 221 KB    | ######################################### | 100% 
markupsafe-2.0.1     | 35 KB     | ######################################### | 100% 
dataclasses-0.8      | 8 KB      | ######################################### | 100% 
click-8.0.4          | 156 KB    | ######################################### | 100% 
jinja2-3.0.3         | 106 KB    | ######################################### | 100% 
Preparing transaction: done
Verifying transaction: done
Executing transaction: done
```
----------------------------------

## 1. Layout Proyek
Buat direktori proyek dengan memasukkan command berikut:
```python
(workshop) zargiteddy@shield:~$ mkdir flask-tutorial
(workshop) zargiteddy@shield:~$ cd flask-tutorial
```
Tutorial ini dilakukan di direktori `flask-tutorial`.

Aplikasi flask paling sederhana terdiri dari satu file.

`hello.py`

```python
from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, World!'
```
Saat proyek semakin besar dan rumit, maka semakin sulit pula untuk menyimpan kode di satu file. Proyek Python menggunakan _packages_ untuk membagi kode ke dalam beberapa modul yang bisa diimport ketika dibutuhkan.

Direktori proyek berisi:
- `flaskr/`, package Python yang berisi kode aplikasi dan file milik kita.
- `tes/`, direktori yang berisi modul test.
- `workshop/`, virtual environment Python tempat Flask dan dependensi lainnya diinstal.
- File instalasi yang memberi tahu ke Python cara menginstall proyek.
- Konfigurasi _version control_ seperti git. Kita harus terbiasa menggunakan beberapa jenis _version control_ untuk semua proyek, berapa pun ukurannya.
- File proyek lain yang mungkin akan kita tambahkan di masa yang akan datang.

Di akhir, layout proyek kita akan terlihat seperti ini:
```python
/home/zargiteddy/flask-tutorial
├── flaskr/
│   ├── __init__.py
│   ├── db.py
│   ├── schema.sql
│   ├── auth.py
│   ├── blog.py
│   ├── templates/
│   │   ├── base.html
│   │   ├── auth/
│   │   │   ├── login.html
│   │   │   └── register.html
│   │   └── blog/
│   │       ├── create.html
│   │       ├── index.html
│   │       └── update.html
│   └── static/
│       └── style.css
├── tests/
│   ├── conftest.py
│   ├── data.sql
│   ├── test_factory.py
│   ├── test_db.py
│   ├── test_auth.py
│   └── test_blog.py
├── venv/
├── setup.py
└── MANIFEST.in
```

Jika kita menggunakan `version control`, file yang dihasilkan ketika menjalankan proyek harus diabaikan. Bisa jadi ada file lain dari editor yang kita gunakan. Pada umumnya, kita harus mengabaikan file yang tidak kita tulis. Misalnya, dengan git:

`.gitignore`
```
python
venv/

*.pyc
__pycache__/

instance/

.pytest_cache/
.coverage
htmlcov/

dist/
build/
*.egg-info/
```
----------------------------------

## 2. Setup Aplikasi
Aplikasi Flask adalah _instance_ dari kelas Flask. Apapun tentang aplikasi, seperti konfigurasi dan URL, akan didaftarkan dengan kelas ini.

Cara paling cepat membuat aplikasi Flask adalah dengan membuat _instance_ Flask global langsung di sebelah atas kode kita, seperti contoh "Hello, World" tadi. Walau cara ini seringkali digunakan, tetapi cara ini bisa mengakibatkan beberapa masalah saat proyek sudah lebih berkembang.

Daripada membuat instance Flask secara global, kita lebih baik membuatnya di dalam suatu fungsi. FUngsi ini dikenal dengan nama _application factory_. Semua konfigurasi, registrasi, dan setup lain yang dibutuhkan oleh aplikasi akan berjalan di dalam fungsi tersebut, lalu aplikasi akan dikembalikan.

### Application Factory
Kita langsung saja membuat direkroti `flaskr` dan langsung tambahkan file `__init__.py`. File `__init__.py` melakukan dua pekerjaan: menampung _application factory_ dan memberi tahu Python bahwa direktori `flaskr` harus diperlakukan sebagai _package_.

```python
(workshop) zargiteddy@shield:~/flask-tutorial$ mkdir flaskr
```

`flaskr/__init__.py`

```python
import os

from flask import Flask


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    return app
```
`create_app` adalah fungsi _application factory_. Kita akan menambahkannya nanti.
<br>

1. `app = Flask(__name__, instance_relative_config=True)` membuat _instance_ Flask.
    - `__name__` adalah nama modul Python yang sedang digunakan. Aplikasi harus mengetahui di mana letaknya untuk menyiapkan beberapa _path_, dan `__name__` adalah cara yang bagus untuk memberitahukannya.
    - `instance_relative_config=True` memberi tahu aplikasi bahwa file konfigurasi relatif ke folder _instance_. Folder _instance_ terletak di luar package `flaskr` dan bisa menyimpan data lokal yang tidak seharusnya di-commit ke _version control_, seperti rahasia konfigurasi dan file database.
<br>

2. `app.config.from_mapping()` membuat beberapa konfigurasi default yang akan digunakan oleh aplikasi:
    - `SECRET_KEY` digunakan oleh Flask dan extension untuk menjaga data supaya tetap aman. Key tersebut di-set ke `dev` untuk menyediakan nilai yang sesuai saat pengembangan, tetapi harus di-override dengan nilai random ketika tahap _deployment_.
    - `DATABASE` adalah path di mana file database SQLite akan disimpan. Path tersebut ada di bawah `app.instance_path`, yang merupakan path yang sudah dipilih oleh Flask untuk folder _instance_.
<br>

3. `app.config.from_pyfile()` meng-override konfigurasi degault dengan nilai yang diambil dari file `config.py` di dalam folder _instance_. Contohnya, ketika _deploying_, bisa digunakan untuk membuat `SECRET_KEY`.
    - `test_config` juga bisa dimasukkan ke _factory_, dan akan digunakan (tidak menggunakan konfigurasi _instance_). Hal ini supaya _test_ yang nanti kita akan tulis bisa dikonfigurasi secara independen dari setiap nilai _development_ yang sudah dikonfigurasi.
<br>

4. `os.makedirs()` memastikan bahwa ada `app.instance_path`. Flask tidak membuat folder _instance_ secara otomatis, tetapi harus dibuat secara manual karena proyek kita akan membuat file database SQLite di dalamnya.
<br>

5. `@app.route()` membuat rute sederhana sehingga kita bisa melihat bagaimana aplikasi bekerja. `@app.route()` membuat koneksi antara `URL /hello` dan sebuah fungsi yang mengembalikan respon yaitu `'Hello, World!'`.

### Jalankan Aplikasi
Sekarang kita dapat menjalankan aplikasi menggunakan perintah flask. Dari terminal, beri tahu Flask di mana lokasi aplikasi kita, lalu jalankan dalam mode development. Kita harus tetap berada di direktori `flask-tutorial`, bukan di package `flask`.

Mode development menunjukkan debugger interaktif setiap kali halaman memunculkan _exception_, dan me-restart server setiap kali kita membuat perubahan pada kode. Kita bisa membiarkannya berjalan dan langsung _reload_ halaman browser.

```python
(workshop) zargiteddy@shield:~/flask-tutorial$ export FLASK_APP=flaskr
(workshop) zargiteddy@shield:~/flask-tutorial$ export FLASK_ENV=development
(workshop) zargiteddy@shield:~/flask-tutorial$ flask run
 * Serving Flask app 'flaskr' (lazy loading)
 * Environment: development
 * Debug mode: on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 406-411-116
```

Kunjungi http://127.0.0.1:5000/hello di browser dan kita akan melihat pesan "Hello, World!”.

Jika program lain sudah menggunakan port 5000, maka kita akan melihat `OSError: [Errno 98]` atau `OSError: [WinError 10013]` ketika server dimulai.

----------------------------------

## 3. Mendefinisikan dan Mengakses Database
Aplikasi akan menggunakan database SQLite untuk menyimpan user dan post. Python hadir dengan support built-in untuk SQLite dalam modul sqlite3.

SQLite bagus karena tidak memerlukan pengaturan server database terpisah dan sudah terintegrasi dengan Python. Tetapi, jika beberapa request mencoba menulis ke database pada saat bersamaan, request tersebut akan melambat karena setiap penulisan terjadi secara berurutan.

### Koneksi ke Database
Hal pertama yang harus dilakukan ketika bekerja dengan database SQLite adalah membuat koneksi ke database SQLite. Setiap kueri dan operasi dijalankan menggunakan koneksi, yang nantinya akan diakhiri setelah pekerjaan selesai.

Di dalam aplikasi web, koneksi ini biasanya dihubungkan ke request. Koneksi itu dibuat ketika meng-handle sebuah request, dan diakhiri sebelum request dikirim.

`flaskr/db.py`

```python
import sqlite3

import click
from flask import current_app, g
from flask.cli import with_appcontext


def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row

    return g.db


def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()
```
`g` adalah objek istimewa yang unik untuk setiap request. `g` digunakan untuk menampung data yang bisa diakses dengan beberapa fungsi saat proses request. Koneksi disimpan dan digunakan ulang jika `get_db` dipanggil untuk kedua kalinya di dalam request yang sama.

`current_app` adalah objek istimewa yang menunjuk ke aplikasi Flask yang menangani request. Karena kita menggunakan _application factory_, maka tidak ada objek aplikasi ketika menulis sisa kode. `get_db` akan dipanggil ketika aplikasi sudah dibuat dan sedang meng-handle request, jadi `current_app` bisa digunakan.

`sqlite3.connect()` membangun koneksi ke file yang ditunjuk oleh key konfigurasi `DATABASE`. File ini tidak tersedia kecuali jika kita sudah menginisialisasi database.

`sqlite3.Row` memberi tahu koneksi untuk me-return baris yang bersifat seperti dictionary. Hal ini memungkinkan kita untuk mengakses kolom menggunakan nama.

`close_db` memeriksa jika koneksi sudah dibuat dengan memeriksa jika `g.db` sudah dibuat. Jika koneksi ada, maka akan diakhiri.

### Membuat Tabel
Di dalam SQLite, data disimpan di dalam tabel dan kolom. Kedua tempat penyimpanan tersebut harus dibuat sebelum kita bisa menyimpan dan mengambil data. Flaskr akan menyimpan user di dalam tabel `user`, dan post di dalam tabel `post`. Buat file dengan perintah SQL untuk membuat tabel kosong:

`flaskr/schema.sql`

```python
DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS post;

CREATE TABLE user (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  username TEXT UNIQUE NOT NULL,
  password TEXT NOT NULL
);

CREATE TABLE post (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  author_id INTEGER NOT NULL,
  created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  title TEXT NOT NULL,
  body TEXT NOT NULL,
  FOREIGN KEY (author_id) REFERENCES user (id)
);
```
Tambahkan fungsi Python yang akan menjalankan perintah SQL tersebut ke dalam file `db.py`:

`flaskr/db.py`

```python
def init_db():
    db = get_db()

    with current_app.open_resource('schema.sql') as f:
        db.executescript(f.read().decode('utf8'))


@click.command('init-db')
@with_appcontext
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()
    click.echo('Initialized the database.')
```
`open_resource()` membuka file yang relatif ke package `flaskr`. `get_db` me-return koneksi database, yang digunakan untuk mengeksekusi perintah yang dibaca dari file.

`click.command()` mendefinisikan perintah baris perintah bernama `init-db` yang memanggil fungsi `init_db` dan menunjukkan pesan sukses kepada user.

### Registrasi dengan Aplikasi
Fungsi `close_db` dan `init_db_command` harus didaftarkan dengan _instance_ aplikasi; jika tidak, kedua fungsi tersebut tidak akan digunakan oleh aplikasi. Karena kita menggunakan fungsi factory, instance tersebut tidak tersedia ketika kita menulis fungsi. Maka dari itu, tulislah fungsi yang mengambil aplikasi dan sekaligus bisa melakukan registrasi.

`flaskr/db.py`

```python
def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)
```

`app.teardown_appcontext()` memberi tahu Flask untuk memanggil fungsi tersebut ketika proses pembersihan setelah me-return respon.

`app.cli.add_command()` menambahkan perintah baru yang bisa dipanggil dengan perintah `flask`.

Import dan panggil fungsi ini dari factory. Letakkan kode baru pada akhir fungsi factory sebelum me-return aplikasi.

`flask/__init__.py`

```python
def create_app():
    app = ...
    # existing code omitted

    from . import db
    db.init_app(app)

    return app
```
### Inisialisasi File Database
Sekarang `init-db` sudah diregister dengan aplikasi, dan bisa dipanggil dengan perintah `flask`.

Catatan:
Jika kita masih menjalankan server dari tahap "Setup Aplikasi", kita bisa menghentikan server tersebut, atau menjalankan perintah di terminal baru. Jika kita menggunakan terminal baru, kita harus mengganti direktori proyek dan mengaktifkan env. Kita juga harus set `FLASK_APP` dan `FLASK_ENV` lagi.

Jalankan perintah `init-db`:

```python
(workshop) zargiteddy@shield:~/flask-tutorial$ export FLASK_APP=flaskr
(workshop) zargiteddy@shield:~/flask-tutorial$ export FLASK_ENV=development
(workshop) zargiteddy@shield:~/flask-tutorial$ flask init-db
Initialized the database.
```
Sekarang sudah muncul file `flaskr.sqlite` di dalam folder `instance` di proyek kita.

----------------------------------

## 4. Blueprint dan View
Fungsi view adalah kode yang kita tulis untuk merespon request ke aplikasi. Flask menggunakan _pattern__ untuk mencocokkan URL request yang masuk dengan view. View me-return data yang diubah Flask menjadi respon _outgoing_. Flask juga bisa menuju ke arah lain dan menghasilkan URL ke view berdasarkan nama dan argumen.

### Membuat Blueprint
`Blueprint` adalah cara untuk mengorganisir sebuah grup yang berkaitan dengan view dan kode lain. Grup-grup tersebut diregister atau didaftar dengan blueprint. Lalu blueprint diregister dengan aplikasi ketika tersedia di dalam fungsi factory.

Flaskr akan memiliki dua blueprint, satu untuk fungsi autentikasi dan satu untuk fungsi posting blog. Kode untuk setiap blueprint akan menuju ke dalam modul yang terpisah. Karena blog harus tahu tentang autentikasi, maka kita harus menulis autentikasi terlebih dahulu.

`flaskr/auth.py`

```python
import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

from flaskr.db import get_db

bp = Blueprint('auth', __name__, url_prefix='/auth')
```
Kode diatas membuat Blueprint bernama '`auth`'. Seperti objek aplikasi, blueprint harus mengetahui dimana blueprint tersebut didefinisikan, jadi `__name__` dimasukkan sebagai argumen kedua. `url_prefix` akan ditambahkan ke semua URL yang terkait dengan blueprint.

Import dan register blueprint dari factory menggunakan `app.register_blueprint()`. Letakkan kode baru pada akhir fungsi factory sebelum me-return aplikasi.

`flaskr/__init__.py`

```python
def create_app():
    app = ...
    # existing code omitted

    from . import auth
    app.register_blueprint(auth.bp)

    return app
```
Blueprint autentikasi akan memiliki view untuk me-register user baru dan juga untuk login maupun logout/.

### View Pertama: Register
Ketika user mengunjungi URL `/auth/register`, tampilan register akan me-return HTML dengan form untuk diisi. Ketika user mengirimkan form tersebut, hal itu akan memvalidasi input dan menampilkan formulir lagi dengan pesan error atau membuat user baru dan pergi ke halaman login.

`flaskr/auth.py`

```python
@bp.route('/register', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = get_db()
        error = None

        if not username:
            error = 'Username is required.'
        elif not password:
            error = 'Password is required.'

        if error is None:
            try:
                db.execute(
                    "INSERT INTO user (username, password) VALUES (?, ?)",
                    (username, generate_password_hash(password)),
                )
                db.commit()
            except db.IntegrityError:
                error = f"User {username} is already registered."
            else:
                return redirect(url_for("auth.login"))

        flash(error)

    return render_template('auth/register.html')
```
Berikut hal-hal yang dilakukan oleh fungsi register:

1. `@bp.route` mengaitkan URL `/register` dengan fungsi view `register`. Ketika Flask menerima request ke `/auth/register`, ia akan memanggil view `register` dan menggunakan return value sebagai respon.

2. Jika user mengirimkan form, `request.method` akan menjadi 'POST'. Dari sini mulailah memvalidasi input.

3. `request.form` adalah key dan value pemetaan form tipe spesial `dict` sudah di-submit.

4. Validasi (pastikan) `username` dan `password` tidak kosong.

5. Jika validasi sukses, masukkan data baru user ke dalam database.
    - `db.execute` mengambil kueri SQL dengan placeholder `?` untuk setiap input dari user, dan tupel berisi nilai untuk menggantikan placeholder. Library database akan menangani pelepasan nilai sehingga kita tidak rentan terhadap serangan _SQL Injection_.
    - Untuk keamanan, password tidak boleh disimpan dalam database secara langsung. Sebagai gantinya, `generate_password_hash()` kita gunakan untuk hash password, lalu hash itu disimpan. Karena kueri ini memodifikasi data, `db.commit()` harus dipanggil setelahnya untuk menyimpan perubahan.
    - `sqlite3.IntegrityError` akan muncul jika nama user sudah ada, yang harus ditampilkan kepada user sebagai error validasi lain.

6. Setelah menyimpan user, user-user tersebut diarahkan ke halaman login. `url_for()` menghasilkan URL untuk view login berdasarkan namanya. Hal tersebut lebih diminati daripada menulis URL secara langsung karena memungkinkan kita untuk mengubah URL tanpa mengubah semua kode yang terhubung ke sana. `redirect()` menghasilkan respon redirect ke generated URL.

7. Jika validasi gagal, error akan ditampilkan kepada user. `flash()` menyimpan pesan yang dapat diambil ketika me-render template.

8. Ketika user bernavigasi ke `auth/register`, atau ada error validasi, halaman HTML dengan formu registrasi akan ditampilkan. `render_template()` akan me-render template yang berisi HTML.

### Login
View ini mengikuti pola yang sama dengan pola register tadi.

`flaskr/auth.py`

```python
@bp.route('/login', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = get_db()
        error = None
        user = db.execute(
            'SELECT * FROM user WHERE username = ?', (username,)
        ).fetchone()

        if user is None:
            error = 'Incorrect username.'
        elif not check_password_hash(user['password'], password):
            error = 'Incorrect password.'

        if error is None:
            session.clear()
            session['user_id'] = user['id']
            return redirect(url_for('index'))

        flash(error)

    return render_template('auth/login.html')
```
Ada beberapa perbedaan dari view `register`:

1. User dikueri terlebih dahulu dan disimpan di dalam variabel untuk digunakan nanti. `fetchone()` me-return satu baris dari kueri. Jika kueri tidak me-return hasil apapun, maka kueri mengembalikan `None`. Kemudian, `fetchall()` akan digunakan untuk me-return list semua hasil.

2. `check_password_hash()` meng-hash password yang sudah di-submit dengan cara yang sama dengan hash yang telah disimpan, kemudian membandingkan keduanya dengan cara yang aman. Jika cocok, maka password dianggap valid.

3. `session` adalah `dict` yang menyimpan data di seluruh request. Saat validasi berhasil, id user disimpan di sesi baru. Data disimpan di dalam cookie yang dikirim ke browser, kemudian browser mengirimkannya kembali dengan request berikutnya. Flask melakukan sign pada data dengan aman sehingga data tidak dapat dirusak.

Karena id user sudah disimpan di dalam `session`, maka id tersebut akan tersedia pada request berikutnya. Di awal setiap request, jika user login, informasi mereka harus dimuat dan harus tersedia untuk view lain.

`flaskr/auth.py`

```python
@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')

    if user_id is None:
        g.user = None
    else:
        g.user = get_db().execute(
            'SELECT * FROM user WHERE id = ?', (user_id,)
        ).fetchone()
```
`bp.before_app_request()` meregister fungsi yang berjalan sebelum fungsi view. `load_logged_in_user` memeriksa apakah id user disimpan di dalam sesi dan mendapatkan data user tersebut dari database, menyimpannya di `g.user`, yang berlangsung selama proses request. Jika tidak ada id user, atau jika id tidak ada, maka `g.user` akan menjadi `None`.

### Logout
Untuk logout, kita harus menghapus id user dari session. Lalu, `load_logged_in_user` tidak akan memuat user pada request.

`flaskr/auth.py`

```python
@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))
```

### Memerlukan Autentikasi di View Lain
Membuat, mengedit, dan menghapus posting blog akan mengharuskan user untuk login. _decorator_ dapat digunakan untuk memeriksa hal ini untuk setiap view yang diterapkan.

`flaskr/auth.py`

```python
def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('auth.login'))

        return view(**kwargs)

    return wrapped_view
```
_decorator_ me-return fungsi view baru yang membungkus view asli yang diterapkannya. Fungsi baru memeriksa apakah user dimuat dan dialihkan ke halaman login. Jika user dimuat, view asli dipanggil dan berlanjut secara normal.

### Endpoint dan URL
Fungsi `url_for()` menghasilkan URL ke view berdasarkan nama dan argumen. Nama yang terkait dengan view juga disebut sebagai endpoint, dan secara default sama dengan nama fungsi view.

Sebagai contoh, tampilan `hello()` yang ditambahkan ke factory aplikasi sebelumnya memiliki nama `'hello'` dan dapat dihubungkan dengan `url_for('hello')`. Jika dibutuhkan argumen, yang akan kita lihat nanti akan dihubungkan dengan menggunakan `url_for('hello', who='World')`.

Saat menggunakan blueprint, nama blueprint ditambahkan ke nama fungsi. Jadi, endpoint untuk fungsi login yang kita tulis di atas adalah `'auth.login'` karena kita menambahkannya ke blueprint 'auth'.

----------------------------------

## 5. Template
Kita telah menuliskan view autentikasi untuk aplikasi kita, tetapi jika kita menjalankan server dan mencoba untuk pergi ke URL apapun, kita akan melihat error `TemplateNotFound`. Hal tersebut terjadi karena view memanggil `render_template()`, tetapi kita belum membuat template. File template akan disimpan di dalam direktori template di dalam package flaskr.

Template adalah file yang berisi data statis serta placeholder untuk data dinamis. Sebuah template di-render dengan data tertentu untuk menghasilkan dokumen final. Flask menggunakan library template `Jinja` untuk me-render template. Di dalam aplikasi ini, Kita akan menggunakan template untuk me-render HTML yang akan ditampilkan di browser milik user. Di Flask, Jinja dikonfigurasi untuk _autoescape_ semua data yang di-render di dalam template HTML.

### Layout Dasar
Setiap halaman dalam aplikasi akan memiliki layout dasar yang sama di sekitar body yang berbeda. Setiap template akan memperluas template dasar dan meng-override bagian tertentu.

`flaskr/templates/base.html`

```python
<!doctype html>
<title>{% block title %}{% endblock %} - Flaskr</title>
<link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
<nav>
  <h1>Flaskr</h1>
  <ul>
    {% if g.user %}
      <li><span>{{ g.user['username'] }}</span>
      <li><a href="{{ url_for('auth.logout') }}">Log Out</a>
    {% else %}
      <li><a href="{{ url_for('auth.register') }}">Register</a>
      <li><a href="{{ url_for('auth.login') }}">Log In</a>
    {% endif %}
  </ul>
</nav>
<section class="content">
  <header>
    {% block header %}{% endblock %}
  </header>
  {% for message in get_flashed_messages() %}
    <div class="flash">{{ message }}</div>
  {% endfor %}
  {% block content %}{% endblock %}
</section>
```
Secara otomatis, `g` tersedia di template. Berdasarkan jika `g.user` di-set (dari `load_logged_in_user`), username dan link untuk logout akan ditampilkan, atau link untuk registrasi dan login akan ditampilkan. `url_for()` juga tersedia secara otomatis, dan digunakan untuk menghasilkan URL ke view.

Setelah judul halaman, dan sebelum konten, template melakukan loop pada setiap pesan yang di-return oleh `get_flash_messages()`. Kita menggunakan `flash()` dalam view untuk menampilkan pesan error.

Ada tiga blok yang akan di-override di template lain:

1. `{% block title %}` akan mengganti judul yang ditampilkan di tab browser dan judul window.

2. `{% block header %}` mirip dengan `title` tetapi akan mengganti judul yang ditampilkan pada halaman.

3. `{% block content %}` adalah di mana konten setiap halaman menuju, seperti form login atau post blog.

### Register
`flaskr/templates/auth/register.html`

```python
{% extends 'base.html' %}

{% block header %}
  <h1>{% block title %}Register{% endblock %}</h1>
{% endblock %}

{% block content %}
  <form method="post">
    <label for="username">Username</label>
    <input name="username" id="username" required>
    <label for="password">Password</label>
    <input type="password" name="password" id="password" required>
    <input type="submit" value="Register">
  </form>
{% endblock %}
```
`{% extends 'base.html' %}` memberi tahu Jinja jika template ini harus menggantikan blok dari template dasar. Semua konten yang di-render harus muncul di dalam tag `{% block %}` yang meng-override blok dari template dasar.

pola `{% block title %}` di dalam `{% block header %}` akan membuat blok judul (title) dan kemudian menampilkan nilainya ke dalam blok header, sehingga window dan halaman akan memiliki judul yang sama tanpa harus dituliskan dua kali.

Tag `input` menggunakan atribut yang diperlukan. Hal tersebut memberitahu browser untuk tidak mengirimkan formu sampai field tersebut diisi.

### Log In
Sama dengan template register, hanya beda di tombol title dan submit.

`flaskr/templates/auth/login.html`

```python
{% extends 'base.html' %}

{% block header %}
  <h1>{% block title %}Log In{% endblock %}</h1>
{% endblock %}

{% block content %}
  <form method="post">
    <label for="username">Username</label>
    <input name="username" id="username" required>
    <label for="password">Password</label>
    <input type="password" name="password" id="password" required>
    <input type="submit" value="Log In">
  </form>
{% endblock %}
```

### Daftarkan User
Karena template autentikasi sudah ditulis, kita dapat mendaftarkan user. Pastikan bahwa server masih berjalan, lalu langsung menuju ke http://127.0.0.1:5000/auth/register.

Coba klik tombol "Register" tanpa mengisi form dan lihat bahwa browser akan menunjukkan pesan error. Coba hapus atribut `required` dari `register.html` dan klik "Register" lagi. Halaman akan reload dan error dari `flash()` akan ditampilkan di dalam view.

Isi username dan password kemudian kita langsung akan diarahkan ke halaman login. Coba username yang salah, atau username yang benar dan kata sandi yang salah. Jika kita login, kita akan mendapatkan error karena belum ada view index untuk dialihkan.

------------------
## 6. File Statis
View dan template autentikasi dapat bekerja dengan baik, tetapi masih kelihatan sangat _plain_. Kita bisa menambahkan CSS untuk memberi style ke layout HTML yang sudah kita buat.

Secara otomatis, Flask menambahkan view `static` yang mengambil path relatif ke direktori `flaskr/static`. Template `base.html` sudah memiliki link ke file `style.css`.

```python
{{ url_for('static', filename='style.css') }}
```
Tutorial ini tidak berfokus pada cara menulis CSS, jadi kita cukup copy kode berikut ke dalam file flaskr/static/style.css:

`flaskr/static/style.css`

```python
html { font-family: sans-serif; background: #eee; padding: 1rem; }
body { max-width: 960px; margin: 0 auto; background: white; }
h1 { font-family: serif; color: #377ba8; margin: 1rem 0; }
a { color: #377ba8; }
hr { border: none; border-top: 1px solid lightgray; }
nav { background: lightgray; display: flex; align-items: center; padding: 0 0.5rem; }
nav h1 { flex: auto; margin: 0; }
nav h1 a { text-decoration: none; padding: 0.25rem 0.5rem; }
nav ul  { display: flex; list-style: none; margin: 0; padding: 0; }
nav ul li a, nav ul li span, header .action { display: block; padding: 0.5rem; }
.content { padding: 0 1rem 1rem; }
.content > header { border-bottom: 1px solid lightgray; display: flex; align-items: flex-end; }
.content > header h1 { flex: auto; margin: 1rem 0 0.25rem 0; }
.flash { margin: 1em 0; padding: 1em; background: #cae6f6; border: 1px solid #377ba8; }
.post > header { display: flex; align-items: flex-end; font-size: 0.85em; }
.post > header > div:first-of-type { flex: auto; }
.post > header h1 { font-size: 1.5em; margin-bottom: 0; }
.post .about { color: slategray; font-style: italic; }
.post .body { white-space: pre-line; }
.content:last-child { margin-bottom: 0; }
.content form { margin: 1em 0; display: flex; flex-direction: column; }
.content label { font-weight: bold; margin-bottom: 0.5em; }
.content input, .content textarea { margin-bottom: 1em; }
.content textarea { min-height: 12em; resize: vertical; }
input.danger { color: #cc2f2e; }
input[type=submit] { align-self: start; min-width: 10em; }
```
Kita bisa langsung menuju ke http://127.0.0.1:5000/auth/login untuk melihat tampilan yang sudah berubah.

--------------------------------
## 7. Blog Blueprint
Blog harus mencantumkan semua post, mengizinkan user yang sudah login untuk membuat post, dan mengizinkan penulis post untuk mengedit atau menghapus postnya.

### The Blueprint
definisikan blueprint dan register ke application factory.

`flaskr/blog.py`

```python
from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from flaskr.auth import login_required
from flaskr.db import get_db

bp = Blueprint('blog', __name__)
```
Import dan register blueprint dari factory menggunakan `app.register_blueprint()`. Letakkan kode baru pada akhir fungsi factory sebelum me-return app.

`flaskr/__init__.py`

```python
def create_app():
    app = ...
    # existing code omitted

    from . import blog
    app.register_blueprint(blog.bp)
    app.add_url_rule('/', endpoint='index')

    return app
```
Tidak seperti blueprint auth, blueprint blog tidak memiliki `url_prefix`. Jadi view `index` akan berada di `/`, view `create` di `/create`, dan seterusnya. Blog adalah fitur utama Flaskr, jadi indeks blog merupakan indeks utama.

### Index
Index akan menunjukkan semua post, diutamakan yang baru saja dibuat (recent). `JOIN` digunakan supaya informasi penulis dari tabel `user` tersedia di hasil.

`flaskr/blog.py`

```python
@bp.route('/')
def index():
    db = get_db()
    posts = db.execute(
        'SELECT p.id, title, body, created, author_id, username'
        ' FROM post p JOIN user u ON p.author_id = u.id'
        ' ORDER BY created DESC'
    ).fetchall()
    return render_template('blog/index.html', posts=posts)
```
`flaskr/templates/blog/index.html`

```python
{% extends 'base.html' %}

{% block header %}
  <h1>{% block title %}Posts{% endblock %}</h1>
  {% if g.user %}
    <a class="action" href="{{ url_for('blog.create') }}">New</a>
  {% endif %}
{% endblock %}

{% block content %}
  {% for post in posts %}
    <article class="post">
      <header>
        <div>
          <h1>{{ post['title'] }}</h1>
          <div class="about">by {{ post['username'] }} on {{ post['created'].strftime('%Y-%m-%d') }}</div>
        </div>
        {% if g.user['id'] == post['author_id'] %}
          <a class="action" href="{{ url_for('blog.update', id=post['id']) }}">Edit</a>
        {% endif %}
      </header>
      <p class="body">{{ post['body'] }}</p>
    </article>
    {% if not loop.last %}
      <hr>
    {% endif %}
  {% endfor %}
{% endblock %}
```
Ketika user sudah login, blok `header` menambahkan link ke view `create`. Saat user adalah penulis post, mereka akan melihat link “Edit” ke view `update` untuk postingan tersebut. `loop.last` adalah variabel spesial yang tersedia di dalam [Jinja for loops](https://jinja.palletsprojects.com/en/3.1.x/templates/#for) yang digunakan untuk menampilkan baris setelah setiap post kecuali yang terakhir.

### Create
View `create` berfungsi sama dengan view `register` auth. Baik form yang ditampilkan, atau data yang telah dipost langsung divalidasi dan post itu ditambahkan ke database atau pesan error akan ditampilkan.

_decorator_ `login_required` yang telah kita tulis sebelumnya digunakan pada view blog. User harus login untuk mengunjungi view tersebut. Jika tidak, mereka akan diarahkan ke halaman login.

`flaskr/blog.py`

```python
@bp.route('/create', methods=('GET', 'POST'))
@login_required
def create():
    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        error = None

        if not title:
            error = 'Title is required.'

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                'INSERT INTO post (title, body, author_id)'
                ' VALUES (?, ?, ?)',
                (title, body, g.user['id'])
            )
            db.commit()
            return redirect(url_for('blog.index'))

    return render_template('blog/create.html')
```

`flaskr/templates/blog/create.html`

```python
{% extends 'base.html' %}

{% block header %}
  <h1>{% block title %}New Post{% endblock %}</h1>
{% endblock %}

{% block content %}
  <form method="post">
    <label for="title">Title</label>
    <input name="title" id="title" value="{{ request.form['title'] }}" required>
    <label for="body">Body</label>
    <textarea name="body" id="body">{{ request.form['body'] }}</textarea>
    <input type="submit" value="Save">
  </form>
{% endblock %}
```

### Update
Baik view `update` dan `delete` perlu mengambil post dengan id dan memeriksa apakah penulisnya cocok dengan user yang login. 

`flaskr/blog.py`

```python
def get_post(id, check_author=True):
    post = get_db().execute(
        'SELECT p.id, title, body, created, author_id, username'
        ' FROM post p JOIN user u ON p.author_id = u.id'
        ' WHERE p.id = ?',
        (id,)
    ).fetchone()

    if post is None:
        abort(404, f"Post id {id} doesn't exist.")

    if check_author and post['author_id'] != g.user['id']:
        abort(403)

    return post
```
`abort()` akan memunculkan excpetion yang me-return kode status HTTP. 404 berarti "Not Found", dan 403 berarti "Forbidden".

Argumen `check_author` didefinisikan sehingga fungsi tersebut dapat digunakan untuk mendapatkan post tanpa memeriksa penulisnya.

`flaskr/blog.py`

```python
@bp.route('/<int:id>/update', methods=('GET', 'POST'))
@login_required
def update(id):
    post = get_post(id)

    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        error = None

        if not title:
            error = 'Title is required.'

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                'UPDATE post SET title = ?, body = ?'
                ' WHERE id = ?',
                (title, body, id)
            )
            db.commit()
            return redirect(url_for('blog.index'))

    return render_template('blog/update.html', post=post)
```
View `create` dan `update` terlihat sangat mirip. Perbedaan utamanya adalah tampilan `update` menggunakan objek post dan kueri `UPDATE`, bukan `INSERT`.

`flaskr/templates/blog/update.html`

```python
{% extends 'base.html' %}

{% block header %}
  <h1>{% block title %}Edit "{{ post['title'] }}"{% endblock %}</h1>
{% endblock %}

{% block content %}
  <form method="post">
    <label for="title">Title</label>
    <input name="title" id="title"
      value="{{ request.form['title'] or post['title'] }}" required>
    <label for="body">Body</label>
    <textarea name="body" id="body">{{ request.form['body'] or post['body'] }}</textarea>
    <input type="submit" value="Save">
  </form>
  <hr>
  <form action="{{ url_for('blog.delete', id=post['id']) }}" method="post">
    <input class="danger" type="submit" value="Delete" onclick="return confirm('Are you sure?');">
  </form>
{% endblock %}
```
Template ini memiliki dua form. Yang pertama memposting data yang diedit ke halaman saat ini (`/<id>/update`). Form lainnya hanya berisi tombol dan menentukan atribut `action` yang memposting ke view `delete` sebagai gantinya.

Pola `{{ request.form['title'] or post['title'] }}` digunakan untuk memilih data apa yang muncul di form.

### Delete
View `delete` tidak memiliki template, tombol delete adalah bagian dari `update.html` dan post ke URL `/<id>/delete`. Karena tidak punya template, delete hanya akan menangani metode POST dan kemudian mengarahkan ulang ke view index.

`flaskr/blog.py`

```python
@bp.route('/<int:id>/delete', methods=('POST',))
@login_required
def delete(id):
    get_post(id)
    db = get_db()
    db.execute('DELETE FROM post WHERE id = ?', (id,))
    db.commit()
    return redirect(url_for('blog.index'))
```
-------------------------------------

## 8. Membuat Proyek Bisa di-install
Menginstall membawa beberapa manfaat seperti:

- Python dan Flask memahami cara menggunakan package flaskr hanya karena kita menjalankan dari direktori proyek.
- Kita dapat mengelola dependensi proyek seperti package lain.
- Tool test bisa mengisolasi environment test dari environment development.

### Jelaskan Proyek
File `setup.py` menjelaskan tentang proyek dan file yang bersangkutan.

`setup.py`

```python
from setuptools import find_packages, setup

setup(
    name='flaskr',
    version='1.0.0',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'flask',
    ],
)
```
Python membutuhkan file lain bernama `MANIFEST.in` untuk memberi tahu tentang data lain.

`MANIFEST.in`

```python
include flaskr/schema.sql
graft flaskr/static
graft flaskr/templates
global-exclude *.pyc
```
Kode di atas memberi tahu Python untuk menyalin semua di direktori `static` dan `templates`, dan file `schema.sql`, dan meninggalkan file bytecode.

### Install Proyek
Gunakan `pip` untuk install proyek kita di virtual environment.

```python
(workshop) zargiteddy@shield:~/flask-tutorial$ pip install -e .
Obtaining file:///home/zargiteddy/flask-tutorial
Requirement already satisfied: flask in /home/zargiteddy/miniconda3/envs/workshop/lib/python3.10/site-packages (from flaskr==1.0.0) (2.0.3)
Requirement already satisfied: Werkzeug>=2.0 in /home/zargiteddy/miniconda3/envs/workshop/lib/python3.10/site-packages (from flask->flaskr==1.0.0) (2.0.3)
Requirement already satisfied: Jinja2>=3.0 in /home/zargiteddy/miniconda3/envs/workshop/lib/python3.10/site-packages (from flask->flaskr==1.0.0) (3.0.3)
Requirement already satisfied: click>=7.1.2 in /home/zargiteddy/miniconda3/envs/workshop/lib/python3.10/site-packages (from flask->flaskr==1.0.0) (8.0.4)
Requirement already satisfied: itsdangerous>=2.0 in /home/zargiteddy/miniconda3/envs/workshop/lib/python3.10/site-packages (from flask->flaskr==1.0.0) (2.0.1)
Requirement already satisfied: MarkupSafe>=2.0 in /home/zargiteddy/miniconda3/envs/workshop/lib/python3.10/site-packages (from Jinja2>=3.0->flask->flaskr==1.0.0) (2.0.1)
Installing collected packages: flaskr
  Running setup.py develop for flaskr
Successfully installed flaskr-1.0.0
```
Kita bisa mengobservasi proyek yang sudah diinstall dengan `pip list`.

```python
(workshop) zargiteddy@shield:~/flask-tutorial$ pip list
Package      Version     Location
------------ ----------- -------------------------------
certifi      2022.5.18.1
click        8.0.4
Flask        2.0.3
flaskr       1.0.0       /home/zargiteddy/flask-tutorial
itsdangerous 2.0.1
Jinja2       3.0.3
MarkupSafe   2.0.1
pip          21.2.4
setuptools   61.2.0
Werkzeug     2.0.3
wheel        0.37.1
```
-------------------------------------
## 9. Test Coverage
Kita akan menggunakan [pytest](https://docs.pytest.org/en/7.1.x/) dan [coverage](https://coverage.readthedocs.io/en/6.4/)

```python
(workshop) zargiteddy@shield:~$ conda install -c conda-forge pytest-cov
Collecting package metadata (current_repodata.json): done
Solving environment: done

## Package Plan ##

  environment location: /home/zargiteddy/miniconda3/envs/workshop

  added / updated specs:
    - pytest-cov


The following packages will be downloaded:

    package                    |            build
    ---------------------------|-----------------
    attrs-21.4.0               |     pyhd8ed1ab_0          49 KB  conda-forge
    ca-certificates-2022.5.18.1|       ha878542_0         144 KB  conda-forge
    certifi-2022.5.18.1        |  py310hff52083_0         150 KB  conda-forge
    coverage-6.3.2             |  py310h7f8727e_0         270 KB
    iniconfig-1.1.1            |     pyh9f0ad1d_0           8 KB  conda-forge
    openssl-1.1.1o             |       h166bdaf_0         2.1 MB  conda-forge
    packaging-21.3             |     pyhd8ed1ab_0          36 KB  conda-forge
    pluggy-1.0.0               |  py310hff52083_3          25 KB  conda-forge
    py-1.11.0                  |     pyh6c4a22f_0          74 KB  conda-forge
    pyparsing-3.0.9            |     pyhd8ed1ab_0          79 KB  conda-forge
    pytest-7.1.2               |  py310hff52083_0         465 KB  conda-forge
    pytest-cov-3.0.0           |     pyhd8ed1ab_0          21 KB  conda-forge
    python_abi-3.10            |          2_cp310           4 KB  conda-forge
    toml-0.10.2                |     pyhd8ed1ab_0          18 KB  conda-forge
    tomli-2.0.1                |     pyhd8ed1ab_0          16 KB  conda-forge
    ------------------------------------------------------------
                                           Total:         3.4 MB

The following NEW packages will be INSTALLED:

  attrs              conda-forge/noarch::attrs-21.4.0-pyhd8ed1ab_0
  coverage           pkgs/main/linux-64::coverage-6.3.2-py310h7f8727e_0
  iniconfig          conda-forge/noarch::iniconfig-1.1.1-pyh9f0ad1d_0
  packaging          conda-forge/noarch::packaging-21.3-pyhd8ed1ab_0
  pluggy             conda-forge/linux-64::pluggy-1.0.0-py310hff52083_3
  py                 conda-forge/noarch::py-1.11.0-pyh6c4a22f_0
  pyparsing          conda-forge/noarch::pyparsing-3.0.9-pyhd8ed1ab_0
  pytest             conda-forge/linux-64::pytest-7.1.2-py310hff52083_0
  pytest-cov         conda-forge/noarch::pytest-cov-3.0.0-pyhd8ed1ab_0
  python_abi         conda-forge/linux-64::python_abi-3.10-2_cp310
  toml               conda-forge/noarch::toml-0.10.2-pyhd8ed1ab_0
  tomli              conda-forge/noarch::tomli-2.0.1-pyhd8ed1ab_0

The following packages will be UPDATED:

  ca-certificates    pkgs/main::ca-certificates-2022.4.26-~ --> conda-forge::ca-certificates-2022.5.18.1-ha878542_0

The following packages will be SUPERSEDED by a higher-priority channel:

  certifi            pkgs/main::certifi-2022.5.18.1-py310h~ --> conda-forge::certifi-2022.5.18.1-py310hff52083_0
  openssl              pkgs/main::openssl-1.1.1o-h7f8727e_0 --> conda-forge::openssl-1.1.1o-h166bdaf_0


Proceed ([y]/n)? y


Downloading and Extracting Packages
pytest-cov-3.0.0     | 21 KB     | ######################################### | 100% 
pluggy-1.0.0         | 25 KB     | ######################################### | 100% 
pytest-7.1.2         | 465 KB    | ######################################### | 100% 
pyparsing-3.0.9      | 79 KB     | ######################################### | 100% 
tomli-2.0.1          | 16 KB     | ######################################### | 100% 
openssl-1.1.1o       | 2.1 MB    | ######################################### | 100% 
attrs-21.4.0         | 49 KB     | ######################################### | 100% 
certifi-2022.5.18.1  | 150 KB    | ######################################### | 100% 
ca-certificates-2022 | 144 KB    | ######################################### | 100% 
python_abi-3.10      | 4 KB      | ######################################### | 100% 
iniconfig-1.1.1      | 8 KB      | ######################################### | 100% 
coverage-6.3.2       | 270 KB    | ######################################### | 100% 
py-1.11.0            | 74 KB     | ######################################### | 100% 
toml-0.10.2          | 18 KB     | ######################################### | 100% 
packaging-21.3       | 36 KB     | ######################################### | 100% 
Preparing transaction: done
Verifying transaction: done
Executing transaction: done
```
### Setup dan Fixture
Setiap test akan membuat file database temporary (sementara) baru dan sekaligus mengisi beberapa data yang akan digunakan dalam test. Tulis file SQL untuk memasukkan data tersebut.

`tests/data.sql`

```python
INSERT INTO user (username, password)
VALUES
  ('test', 'pbkdf2:sha256:50000$TCI4GzcX$0de171a4f4dac32e3364c7ddc7c14f3e2fa61f2d17574483f7ffbb431b4acb2f'),
  ('other', 'pbkdf2:sha256:50000$kJPKsz6N$d2d4784f1b030a9761f5ccaeeaca413f27f2ecb76d6168407af962ddce849f79');

INSERT INTO post (title, body, author_id, created)
VALUES
  ('test title', 'test' || x'0a' || 'body', 1, '2018-01-01 00:00:00');
```
Fixture aplikasi akan memanggil factory dan memasukkan `test_config` untuk mengonfigurasi aplikasi dan database untuk testing.

`tests/conftest.py`

```python
import os
import tempfile

import pytest
from flaskr import create_app
from flaskr.db import get_db, init_db

with open(os.path.join(os.path.dirname(__file__), 'data.sql'), 'rb') as f:
    _data_sql = f.read().decode('utf8')


@pytest.fixture
def app():
    db_fd, db_path = tempfile.mkstemp()

    app = create_app({
        'TESTING': True,
        'DATABASE': db_path,
    })

    with app.app_context():
        init_db()
        get_db().executescript(_data_sql)

    yield app

    os.close(db_fd)
    os.unlink(db_path)


@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture
def runner(app):
    return app.test_cli_runner()
```
`tempfile.mkstemp()` membuat dan membuka temporary file, mengembalikan deskriptor file dan path.

`TESTING` memberi tahu Flask bahwa aplikasi dalam mode test.

Fixture client memanggil `app.test_client()` dengan objek aplikasi yang dibuat oleh fixture aplikasi.

`app.test_cli_runner()` membuat runner yang dapat memanggil perintah Click yang terdaftar dengan aplikasi.

### Factory
Jika config tidak diteruskan, harus ada beberapa konfigurasi default. Jika tidak, konfigurasi harus di-override.

`tests/test_factory.py`

```python
from flaskr import create_app


def test_config():
    assert not create_app().testing
    assert create_app({'TESTING': True}).testing


def test_hello(client):
    response = client.get('/hello')
    assert response.data == b'Hello, World!'
```
### Database
Dalam context aplikasi, `get_db` harus mengembalikan koneksi yang sama setiap kali dipanggil. Setelah context, koneksi harus diakhiri.

`tests/test_db.py`

```python
import sqlite3

import pytest
from flaskr.db import get_db


def test_get_close_db(app):
    with app.app_context():
        db = get_db()
        assert db is get_db()

    with pytest.raises(sqlite3.ProgrammingError) as e:
        db.execute('SELECT 1')

    assert 'closed' in str(e.value)
```
Perintah `init-db` harus memanggil fungsi `init_db` dan menampilkan pesan.

`tests/test_db.py`

```python
def test_init_db_command(runner, monkeypatch):
    class Recorder(object):
        called = False

    def fake_init_db():
        Recorder.called = True

    monkeypatch.setattr('flaskr.db.init_db', fake_init_db)
    result = runner.invoke(args=['init-db'])
    assert 'Initialized' in result.output
    assert Recorder.called
```
Test ini menggunakan fixture Pytest yaitu `monkeypatch` untuk menggantikan fungsi `init_db` dengan fungsi yang mencatat bahwa ia telah dipanggil.

### Autentikasi
Pada sebagian besar view, user harus login. Cara termudah untuk melakukan ini dalam test adalah dengan membuat permintaan POST ke view login dengan client.

`test/conftest.py`

```python
class AuthActions(object):
    def __init__(self, client):
        self._client = client

    def login(self, username='test', password='test'):
        return self._client.post(
            '/auth/login',
            data={'username': username, 'password': password}
        )

    def logout(self):
        return self._client.get('/auth/logout')


@pytest.fixture
def auth(client):
    return AuthActions(client)
```
View register harus berhasil di-render pada GET. Pada POST dengan data form yang valid, view register harus diarahkan ke URL login dan data user harus ada di database. Data yang tidak valid harus menampilkan pesan error.

`tests/test_auth.py`

```python
import pytest
from flask import g, session
from flaskr.db import get_db


def test_register(client, app):
    assert client.get('/auth/register').status_code == 200
    response = client.post(
        '/auth/register', data={'username': 'a', 'password': 'a'}
    )
    assert response.headers["Location"] == "/auth/login"

    with app.app_context():
        assert get_db().execute(
            "SELECT * FROM user WHERE username = 'a'",
        ).fetchone() is not None


@pytest.mark.parametrize(('username', 'password', 'message'), (
    ('', '', b'Username is required.'),
    ('a', '', b'Password is required.'),
    ('test', 'test', b'already registered'),
))
def test_register_validate_input(client, username, password, message):
    response = client.post(
        '/auth/register',
        data={'username': username, 'password': password}
    )
    assert message in response.data
```
`client.get()` membuat request `GET` dan me-return objek `Response` yang di-return oleh Flask. `client.post()` membuat request POST, mengubah dict `data` menjadi data form.

Untuk menguji apakah halaman berhasil di-render, simple request dibuat dan diperiksa untuk `status_code` 200 OK. Jika rendering gagal, Flask akan me-return kode `500 Internal Server Error`.

header akan memiliki header `Location` dengan URL login saat view register dialihkan ke view login.

`pytest.mark.parametrize` memberi tahu Pytest untuk menjalankan fungsi test yang sama dengan argumen yang berbeda.

Test untuk view login sangat mirip dengan test untuk register. `session` harus memiliki `user_id` yang ditetapkan setelah login.

`tests/test_auth.py`

```python
def test_login(client, auth):
    assert client.get('/auth/login').status_code == 200
    response = auth.login()
    assert response.headers["Location"] == "/"

    with client:
        client.get('/')
        assert session['user_id'] == 1
        assert g.user['username'] == 'test'


@pytest.mark.parametrize(('username', 'password', 'message'), (
    ('a', 'test', b'Incorrect username.'),
    ('test', 'a', b'Incorrect password.'),
))
def test_login_validate_input(auth, username, password, message):
    response = auth.login(username, password)
    assert message in response.data
```

Testing logout adalah kebalikan dari login. `session` tidak boleh berisi user_id setelah logout.

`tests/test_auth.py`

```python
def test_logout(client, auth):
    auth.login()

    with client:
        auth.logout()
        assert 'user_id' not in session
```
### Blog
Kita bisa menguji beberapa perilaku autentikasi saat menguji view index. Saat tidak dalam keadaan login, setiap halaman menampilkan link untuk login atau register. Saat sudah login, ada link untuk logout.

`tests/test_blog.py`

```python
import pytest
from flaskr.db import get_db


def test_index(client, auth):
    response = client.get('/')
    assert b"Log In" in response.data
    assert b"Register" in response.data

    auth.login()
    response = client.get('/')
    assert b'Log Out' in response.data
    assert b'test title' in response.data
    assert b'by test on 2018-01-01' in response.data
    assert b'test\nbody' in response.data
    assert b'href="/1/update"' in response.data
```
User harus login untuk create, update, dan delete views. User yang telah login harus menjadi author (penulis) post untuk mengakses `update` dan `delete`. Jika tidak, status `403 Forbidden` akan muncul. Jika post dengan id yang diberikan tidak ada, `update` dan `delete` akan memunculkan `404 Not Found`.

`tests/test_blog.py`

```python
@pytest.mark.parametrize('path', (
    '/create',
    '/1/update',
    '/1/delete',
))
def test_login_required(client, path):
    response = client.post(path)
    assert response.headers["Location"] == "/auth/login"


def test_author_required(app, client, auth):
    # change the post author to another user
    with app.app_context():
        db = get_db()
        db.execute('UPDATE post SET author_id = 2 WHERE id = 1')
        db.commit()

    auth.login()
    # current user can't modify other user's post
    assert client.post('/1/update').status_code == 403
    assert client.post('/1/delete').status_code == 403
    # current user doesn't see edit link
    assert b'href="/1/update"' not in client.get('/').data


@pytest.mark.parametrize('path', (
    '/2/update',
    '/2/delete',
))
def test_exists_required(client, auth, path):
    auth.login()
    assert client.post(path).status_code == 404
```
View `create` dan `update` harus me-render dan me-return status 200 OK untuk permintaan GET. Ketika data valid dikirim dalam request POST, create harus memasukkan data post baru ke dalam database, dan `update` harus memodifikasi data yang ada. Kedua halaman harus menampilkan pesan error pada data yang tidak valid.

`tests/test_blog.py`

```python
def test_create(client, auth, app):
    auth.login()
    assert client.get('/create').status_code == 200
    client.post('/create', data={'title': 'created', 'body': ''})

    with app.app_context():
        db = get_db()
        count = db.execute('SELECT COUNT(id) FROM post').fetchone()[0]
        assert count == 2


def test_update(client, auth, app):
    auth.login()
    assert client.get('/1/update').status_code == 200
    client.post('/1/update', data={'title': 'updated', 'body': ''})

    with app.app_context():
        db = get_db()
        post = db.execute('SELECT * FROM post WHERE id = 1').fetchone()
        assert post['title'] == 'updated'


@pytest.mark.parametrize('path', (
    '/create',
    '/1/update',
))
def test_create_update_validate(client, auth, path):
    auth.login()
    response = client.post(path, data={'title': '', 'body': ''})
    assert b'Title is required.' in response.data
```
View `delete` harus mengalihkan ke URL index dan post harus tidak ada lagi di dalam database.

`tests/test_blog.py`

```python
def test_delete(client, auth, app):
    auth.login()
    response = client.post('/1/delete')
    assert response.headers["Location"] == "/"

    with app.app_context():
        db = get_db()
        post = db.execute('SELECT * FROM post WHERE id = 1').fetchone()
        assert post is None
```

### Menjalankan Test
Beberapa konfigurasi tambahan, yang tidak dibutuhkan tetapi membuat proses menjalankan test dengan coverage yang kurang verbose, bisa ditambahkan ke file `setup.cfg`.

`setup.cfg`

```python
[tool:pytest]
testpaths = tests

[coverage:run]
branch = True
source =
    flaskr
```
Untuk menjalankan test, gunakan perintah `pytest` yang akan mencari dan menjalankan semua fungsi test yang telah kita tulis.

```python
(workshop) zargiteddy@shield:~/flask-tutorial$ pytest
======================================== test session starts ========================================
platform linux -- Python 3.10.4, pytest-7.1.2, pluggy-1.0.0
rootdir: /home/zargiteddy/flask-tutorial, configfile: setup.cfg, testpaths: tests
plugins: cov-3.0.0
collected 24 items                                                                                  

tests/test_auth.py F...F...                                                                   [ 33%]
tests/test_blog.py .FFF.......F                                                               [ 83%]
tests/test_db.py ..                                                                           [ 91%]
tests/test_factory.py .. 
```
Gunakan `pytest -v` untuk mendapatkan list setiap fungsi test

```python
(workshop) zargiteddy@shield:~/flask-tutorial$ pytest -v
======================================== test session starts ========================================
platform linux -- Python 3.10.4, pytest-7.1.2, pluggy-1.0.0 -- /home/zargiteddy/miniconda3/envs/workshop/bin/python
cachedir: .pytest_cache
rootdir: /home/zargiteddy/flask-tutorial, configfile: setup.cfg, testpaths: tests
plugins: cov-3.0.0
collected 24 items                                                                                  

tests/test_auth.py::test_register FAILED                                                      [  4%]
tests/test_auth.py::test_register_validate_input[--Username is required.] PASSED              [  8%]
tests/test_auth.py::test_register_validate_input[a--Password is required.] PASSED             [ 12%]
tests/test_auth.py::test_register_validate_input[test-test-already registered] PASSED         [ 16%]
tests/test_auth.py::test_login FAILED                                                         [ 20%]
tests/test_auth.py::test_login_validate_input[a-test-Incorrect username.] PASSED              [ 25%]
tests/test_auth.py::test_login_validate_input[test-a-Incorrect password.] PASSED              [ 29%]
tests/test_auth.py::test_logout PASSED                                                        [ 33%]
tests/test_blog.py::test_index PASSED                                                         [ 37%]
tests/test_blog.py::test_login_required[/create] FAILED                                       [ 41%]
tests/test_blog.py::test_login_required[/1/update] FAILED                                     [ 45%]
tests/test_blog.py::test_login_required[/1/delete] FAILED                                     [ 50%]
tests/test_blog.py::test_author_required PASSED                                               [ 54%]
tests/test_blog.py::test_exists_required[/2/update] PASSED                                    [ 58%]
tests/test_blog.py::test_exists_required[/2/delete] PASSED                                    [ 62%]
tests/test_blog.py::test_create PASSED                                                        [ 66%]
tests/test_blog.py::test_update PASSED                                                        [ 70%]
tests/test_blog.py::test_create_update_validate[/create] PASSED                               [ 75%]
tests/test_blog.py::test_create_update_validate[/1/update] PASSED                             [ 79%]
tests/test_blog.py::test_delete FAILED                                                        [ 83%]
tests/test_db.py::test_get_close_db PASSED                                                    [ 87%]
tests/test_db.py::test_init_db_command PASSED                                                 [ 91%]
tests/test_factory.py::test_config PASSED                                                     [ 95%]
tests/test_factory.py::test_hello PASSED                                                      [100%]
```
Untuk memperkirakan coverage kode dari test, gunakan perintah `coverage` untuk menjalankan `pytest`.

```python
(workshop) zargiteddy@shield:~/flask-tutorial$ coverage run -m pytest
======================================== test session starts ========================================
platform linux -- Python 3.10.4, pytest-7.1.2, pluggy-1.0.0
rootdir: /home/zargiteddy/flask-tutorial, configfile: setup.cfg, testpaths: tests
plugins: cov-3.0.0
collected 24 items                                                                                  

tests/test_auth.py F...F...                                                                   [ 33%]
tests/test_blog.py .FFF.......F                                                               [ 83%]
tests/test_db.py ..                                                                           [ 91%]
tests/test_factory.py ..                                                                      [100%]
```
Kita juga bisa melihat laporan coverage di terminal

```python
(workshop) zargiteddy@shield:~/flask-tutorial$ coverage report
Name                 Stmts   Miss Branch BrPart  Cover
------------------------------------------------------
flaskr/__init__.py      23      0      2      0   100%
flaskr/auth.py          60      0     20      0   100%
flaskr/blog.py          58      0     16      0   100%
flaskr/db.py            25      0      6      0   100%
------------------------------------------------------
TOTAL                  166      0     44      0   100%
```
Laporan HTML memungkinkan kita untuk melihat baris mana yang di-cover di setiap file:

```python
(workshop) zargiteddy@shield:~/flask-tutorial$ coverage html
Wrote HTML report to htmlcov/index.html
```
Perintah tersebut menghasilkan file di direktori `htmlcov`. Buka `htmlcov/index.html` di browser untuk melihat laporan.

-----------------------------------

## 10. Deploy ke Produksi

### Build dan Install
Ketika kita ingin deploy aplikasi di tempat lain, kita membangun file distribusi. Standar saat ini untuk distribusi Python adalah format wheel, dengan ekstensi .whl. Pastikan library wheel sudah terinstall:

```python
(workshop) zargiteddy@shield:~$ conda install -c conda-forge wheel
Collecting package metadata (current_repodata.json): done
Solving environment: done

## Package Plan ##

  environment location: /home/zargiteddy/miniconda3/envs/workshop

  added / updated specs:
    - wheel


The following packages will be downloaded:

    package                    |            build
    ---------------------------|-----------------
    wheel-0.37.1               |     pyhd8ed1ab_0          31 KB  conda-forge
    ------------------------------------------------------------
                                           Total:          31 KB

The following packages will be SUPERSEDED by a higher-priority channel:

  wheel                pkgs/main::wheel-0.37.1-pyhd3eb1b0_0 --> conda-forge::wheel-0.37.1-pyhd8ed1ab_0


Proceed ([y]/n)? y


Downloading and Extracting Packages
wheel-0.37.1         | 31 KB     | ########################################################## | 100% 
Preparing transaction: done
Verifying transaction: done
Executing transaction: done
```
Menjalankan `setup.py` dengan Python memberi kita tool baris perintah untuk mengeluarkan perintah build-related. Perintah `bdist_wheel` akan membuat file distribusi wheel.

```python
(workshop) zargiteddy@shield:~/flask-tutorial$ python setup.py bdist_wheel
running bdist_wheel
running build
running build_py
creating build
creating build/lib
creating build/lib/flaskr
copying flaskr/__init__.py -> build/lib/flaskr
copying flaskr/auth.py -> build/lib/flaskr
copying flaskr/db.py -> build/lib/flaskr
copying flaskr/blog.py -> build/lib/flaskr
running egg_info
writing flaskr.egg-info/PKG-INFO
writing dependency_links to flaskr.egg-info/dependency_links.txt
writing requirements to flaskr.egg-info/requires.txt
writing top-level names to flaskr.egg-info/top_level.txt
reading manifest file 'flaskr.egg-info/SOURCES.txt'
reading manifest template 'MANIFEST.in'
warning: no previously-included files matching '*.pyc' found anywhere in distribution
writing manifest file 'flaskr.egg-info/SOURCES.txt'
copying flaskr/schema.sql -> build/lib/flaskr
creating build/lib/flaskr/static
copying flaskr/static/style.css -> build/lib/flaskr/static
creating build/lib/flaskr/templates
copying flaskr/templates/base.html -> build/lib/flaskr/templates
creating build/lib/flaskr/templates/auth
copying flaskr/templates/auth/login.html -> build/lib/flaskr/templates/auth
copying flaskr/templates/auth/register.html -> build/lib/flaskr/templates/auth
creating build/lib/flaskr/templates/blog
copying flaskr/templates/blog/create.html -> build/lib/flaskr/templates/blog
copying flaskr/templates/blog/index.html -> build/lib/flaskr/templates/blog
copying flaskr/templates/blog/update.html -> build/lib/flaskr/templates/blog
/home/zargiteddy/miniconda3/envs/workshop/lib/python3.10/site-packages/setuptools/command/install.py:34: SetuptoolsDeprecationWarning: setup.py install is deprecated. Use build and pip and other standards-based tools.
  warnings.warn(
installing to build/bdist.linux-x86_64/wheel
running install
running install_lib
creating build/bdist.linux-x86_64
creating build/bdist.linux-x86_64/wheel
creating build/bdist.linux-x86_64/wheel/flaskr
creating build/bdist.linux-x86_64/wheel/flaskr/templates
creating build/bdist.linux-x86_64/wheel/flaskr/templates/blog
copying build/lib/flaskr/templates/blog/index.html -> build/bdist.linux-x86_64/wheel/flaskr/templates/blog
copying build/lib/flaskr/templates/blog/create.html -> build/bdist.linux-x86_64/wheel/flaskr/templates/blog
copying build/lib/flaskr/templates/blog/update.html -> build/bdist.linux-x86_64/wheel/flaskr/templates/blog
creating build/bdist.linux-x86_64/wheel/flaskr/templates/auth
copying build/lib/flaskr/templates/auth/login.html -> build/bdist.linux-x86_64/wheel/flaskr/templates/auth
copying build/lib/flaskr/templates/auth/register.html -> build/bdist.linux-x86_64/wheel/flaskr/templates/auth
copying build/lib/flaskr/templates/base.html -> build/bdist.linux-x86_64/wheel/flaskr/templates
copying build/lib/flaskr/__init__.py -> build/bdist.linux-x86_64/wheel/flaskr
copying build/lib/flaskr/auth.py -> build/bdist.linux-x86_64/wheel/flaskr
copying build/lib/flaskr/db.py -> build/bdist.linux-x86_64/wheel/flaskr
copying build/lib/flaskr/schema.sql -> build/bdist.linux-x86_64/wheel/flaskr
copying build/lib/flaskr/blog.py -> build/bdist.linux-x86_64/wheel/flaskr
creating build/bdist.linux-x86_64/wheel/flaskr/static
copying build/lib/flaskr/static/style.css -> build/bdist.linux-x86_64/wheel/flaskr/static
running install_egg_info
Copying flaskr.egg-info to build/bdist.linux-x86_64/wheel/flaskr-1.0.0-py3.10.egg-info
running install_scripts
creating build/bdist.linux-x86_64/wheel/flaskr-1.0.0.dist-info/WHEEL
creating 'dist/flaskr-1.0.0-py3-none-any.whl' and adding 'build/bdist.linux-x86_64/wheel' to it
adding 'flaskr/__init__.py'
adding 'flaskr/auth.py'
adding 'flaskr/blog.py'
adding 'flaskr/db.py'
adding 'flaskr/schema.sql'
adding 'flaskr/static/style.css'
adding 'flaskr/templates/base.html'
adding 'flaskr/templates/auth/login.html'
adding 'flaskr/templates/auth/register.html'
adding 'flaskr/templates/blog/create.html'
adding 'flaskr/templates/blog/index.html'
adding 'flaskr/templates/blog/update.html'
adding 'flaskr-1.0.0.dist-info/METADATA'
adding 'flaskr-1.0.0.dist-info/WHEEL'
adding 'flaskr-1.0.0.dist-info/top_level.txt'
adding 'flaskr-1.0.0.dist-info/RECORD'
removing build/bdist.linux-x86_64/wheel
```
Kita dapat menemukan file tersebut di `dist/flaskr-1.0.0-py3-none-any.whl`. Nama file dalam format {project name}-{version}-{python tag} -{abi tag}-{platform tag}.

Salin file itu ke mesin lain, buat virtualenv baru, dan install dengan pip

```python
$ pip install flaskr-1.0.0-py3-none-any.whl
```

pip akan menginstall proyek kita sekaligus dengan dependensinya. Karena berbeda mesin, kita harus menjalankan `init-db` lagi.

```python
$ export FLASK_APP=flaskr
$ flask init-db
```

### Konfigurasi Secret key
Kita bisa menggunakan perintah berikut untuk menghasilkan random secret key:

```python
(workshop) zargiteddy@shield:~/flask-tutorial$ python -c 'import secrets; print(secrets.token_hex())'
433dfcce4b3aeb793454ac476587a587665ae22cd17eccae082e8b9ef66ef754
```
Buat file `config.py` di dalam folder instance. Masukkan secret key ke dalamnya.

```python
SECRET_KEY = '433dfcce4b3aeb793454ac476587a587665ae22cd17eccae082e8b9ef66ef754'
```
### Jalankan dengan Production Server
Install Waitress di virtual environment:

```python
(workshop) zargiteddy@shield:~$ conda install -c conda-forge waitress
Collecting package metadata (current_repodata.json): done
Solving environment: done

## Package Plan ##

  environment location: /home/zargiteddy/miniconda3/envs/workshop

  added / updated specs:
    - waitress


The following packages will be downloaded:

    package                    |            build
    ---------------------------|-----------------
    waitress-2.1.1             |     pyhd8ed1ab_0          46 KB  conda-forge
    ------------------------------------------------------------
                                           Total:          46 KB

The following NEW packages will be INSTALLED:

  waitress           conda-forge/noarch::waitress-2.1.1-pyhd8ed1ab_0


Proceed ([y]/n)? y


Downloading and Extracting Packages
waitress-2.1.1       | 46 KB     | ####################################################################################### | 100% 
Preparing transaction: done
Verifying transaction: done
Executing transaction: done
```
Kita harus memberi tahu Waitress tentang aplikasi kita. Kita harus memberi tahunya untuk mengimport dan memanggil application factory untuk mendapatkan application object.

```python
(workshop) zargiteddy@shield:~/flask-tutorial$ waitress-serve --call 'flaskr:create_app'
INFO:waitress:Serving on http://0.0.0.0:8080
```
-----------------------------------
## 11. Keep Developing!
Jika kita ingin terus mengembangkan proyek Flaskr, berikut adalah beberapa ide yang bisa dicoba:
- detail view untuk menampilkan post tunggal. Klik judul post untuk menuju ke halaman.
- Like atau unlike post
- Komentar
- Tag. Menekan tag akan menunjukkan semua post dengan tag tersebut
- Search box yang memfilter halaman index dengan nama
- Hanya menampilkan 5 post setiap halaman
- Upload gambar untuk disertakan dengan post
- Format post dengan Markdown
- RSS feed pada post baru

Thank you!












