# 12. Virtual Environment dan Package
Perhatian: Saya menggunakan file .txt di dalam folder src karena di pertemuan ini semua pengerjaan menggunakan command di terminal. Terima kasih atas perhatiannya.
## 12.1. Pendahuluan
Aplikasi Python biasanya menggunakan package dan modul yang bukan merupakan pustaka standar. Aplikasi terkadang membutuhkan versi spesifik suatu _library_, karena aplikasi bisa saja membutuhkan kondisi dimana bug tertentu sudah diatasi atau juga aplikasi harus ditulis menggunakan versi terdahulu dari antarmuka _library_.

Hal tersebut berarti bisa saja ada ketidakmungkinan untuk instalasi satu Python untuk memenuhi kebutuhan setiap aplikasi. Jika sebuah aplikasi membutuhkan versi 1.0 dari modul tertentu tetapi aplikasi B membutuhkan versi 2.0, maka akan menimbulkan konflik dan menginstall salah satu dari kedua versi tersebut saja akan menyebabkan satu aplikasi tidak bisa berjalan.

Solusi dari permasalahan tersebut adalah dengan membuat [virtual environment](https://docs.python.org/3/glossary.html#term-virtual-environment), yaitu pohon direktori terisolasi yang berisi instalasi Python untuk versi tertentu Python, ditambah dengan beberapa package tambahan.

- - - - - - - - 

## 12.2. Membuat Virtual Environment
Modul yang digunakan untuk membuat dan mengelola _virtual environment_ adalah [venv](https://docs.python.org/3/library/venv.html#module-venv). `venv` biasanya akan menginstall versi terbaru Python yang kita miliki. Jika kita memiliki beberapa versi Python pada sistem, kita bisa memilih versi Python tertentu dengan menjalankan `python3` atau versi berapapun yang kita inginkan.

Untuk membuat _virtual environment_, tentukan di direktori mana kita ingin menempatkannya, dan jalankan modul `venv` dalam bentuk script dengan path direktori:

```python
python3 -m venv tutorial-env
```
Hal tersebut akan membuat direktori `tutorial-env`, sekaligus membuat direktori di dalamnya yang berisi sebuah salinan interpreter Python dan beberapa file pendukung.

Lokasi direktori yang umum digunakan dalam virtual environment adalah `.venv`. Nama itu membuat direktori tetap tersembunyi di dalam shell. Hal itu juga mencegah bentrok dengan file definisi variabel environment `.env`.

Setelah kita berhasil membuat virtual environment, kita bisa menyalakannya.

Pada windows, jalankan:
```python
tutorial-env\Scripts\activate.bat
```
Pada Unix atau MacOS, jalankan:
```python
source tutorial-env/bin/activate
```
Mengaktifkan virtual environment akan membuat prompt pada shell menunjukkan virtual environment yang kita gunakan, dan memodifikasi environment supaya saat kita menjalankan `python` maka akan muncul versi dan instalasi Python tertentu. contoh:
```python
zargiteddy@shield:~$ source tutorial-env/bin/activate
(tutorial-env) zargiteddy@shield:~$ python
Python 3.10.2 (main, Feb  5 2022, 12:29:58) [GCC 9.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import sys
>>> sys.path
['', '/usr/local/lib/python310.zip', '/usr/local/lib/python3.10', '/usr/local/lib/python3.10/lib-dynload', '/home/zargiteddy/tutorial-env/lib/python3.10/site-packages']
>>> 
```
## 12.3. Mengelola Package dengan pip
Kita bisa install, upgrade, dan remove package dengan program bernama `pip`. `pip` akan menginstall package dari Python Package Index.

`pip` memiliki beberapa subcommands:  “install”, “uninstall”, “freeze”, dll.

Kita bisa menginstall versi terbaru package dengan menuliskan nama package:
```python
(tutorial-env) zargiteddy@shield:~$ python -m pip install novas
Collecting novas
  Downloading novas-3.1.1.5.tar.gz (135 kB)
     |████████████████████████████████| 135 kB 1.9 MB/s 
Using legacy 'setup.py install' for novas, since package 'wheel' is not installed.
Installing collected packages: novas
    Running setup.py install for novas ... done
Successfully installed novas-3.1.1.5
```
Kita juga bisa menginstall versi tertentu sebuah package dengan menuliskan nama package diikuti dengan `==` dan nomor versi:
```python
(tutorial-env) zargiteddy@shield:~$ python -m pip install requests==2.6.0
Collecting requests==2.6.0
  Downloading requests-2.6.0-py2.py3-none-any.whl (469 kB)
     |████████████████████████████████| 469 kB 794 kB/s 
Installing collected packages: requests
Successfully installed requests-2.6.0
```
Jika kita menjalankan command tersebut lagi, `pip` akan tahu jika versi tersebut sudah diinstall dan `pip` tidak akan melakukan apapun. Kita bisa memasukkan nomor versi lain, atau kita bisa menjalankan `pip install --upgrade` untuk mengupgrade package ke versi terbaru:
```python
(tutorial-env) zargiteddy@shield:~$ python -m pip install --upgrade requests
Requirement already satisfied: requests in ./tutorial-env/lib/python3.10/site-packages (2.6.0)
Collecting requests
  Using cached requests-2.27.1-py2.py3-none-any.whl (63 kB)
Requirement already satisfied: charset-normalizer~=2.0.0 in ./tutorial-env/lib/python3.10/site-packages (from requests) (2.0.12)
Requirement already satisfied: certifi>=2017.4.17 in ./tutorial-env/lib/python3.10/site-packages (from requests) (2021.10.8)
Requirement already satisfied: idna<4,>=2.5 in ./tutorial-env/lib/python3.10/site-packages (from requests) (3.3)
Requirement already satisfied: urllib3<1.27,>=1.21.1 in ./tutorial-env/lib/python3.10/site-packages (from requests) (1.26.9)
Installing collected packages: requests
  Attempting uninstall: requests
    Found existing installation: requests 2.6.0
    Uninstalling requests-2.6.0:
      Successfully uninstalled requests-2.6.0
Successfully installed requests-2.27.1
```
`pip uninstall` yang diikuti dengan satu atau lebih nama package akan menghapus package dari virtual environment.

`pip show` akan menampilkan informasi tentang package tertentu:
```python
(tutorial-env) zargiteddy@shield:~$ pip show requests
Name: requests
Version: 2.27.1
Summary: Python HTTP for Humans.
Home-page: https://requests.readthedocs.io
Author: Kenneth Reitz
Author-email: me@kennethreitz.org
License: Apache 2.0
Location: /home/zargiteddy/tutorial-env/lib/python3.10/site-packages
Requires: charset-normalizer, urllib3, idna, certifi
Required-by:
```
`pip list` akan menampilkan semua package yang terinstall di virtual environment:
```python
(tutorial-env) zargiteddy@shield:~$ pip list
Package            Version
------------------ ---------
certifi            2021.10.8
charset-normalizer 2.0.12
idna               3.3
novas              3.1.1.5
pip                21.2.4
requests           2.27.1
setuptools         58.1.0
urllib3            1.26.9
```
`pip freeze` akan menghasilkan list package yang terinstall juga, tetapi outputnya menggunakan format yang diharapkan `pip install`. Cara umumnya adalah dengan meletakkan list ini dalam file requirements.txt:
```python
(tutorial-env) zargiteddy@shield:~$ pip freeze > requirements.txt
(tutorial-env) zargiteddy@shield:~$ cat requirements.txt
certifi==2021.10.8
charset-normalizer==2.0.12
idna==3.3
novas==3.1.1.5
requests==2.27.1
urllib3==1.26.9
```
`requirements.txt` bisa di-commit ke _version control_ dan dimasukkan sebagai bagian dari aplikasi. Pengguna bisa menginstall semua package yang dibutuhkan dengan `install -r`:
```python
(tutorial-env) zargiteddy@shield:~$ python -m pip install -r requirements.txt
Requirement already satisfied: certifi==2021.10.8 in ./tutorial-env/lib/python3.10/site-packages (from -r requirements.txt (line 1)) (2021.10.8)
Requirement already satisfied: charset-normalizer==2.0.12 in ./tutorial-env/lib/python3.10/site-packages (from -r requirements.txt (line 2)) (2.0.12)
Requirement already satisfied: idna==3.3 in ./tutorial-env/lib/python3.10/site-packages (from -r requirements.txt (line 3)) (3.3)
Requirement already satisfied: novas==3.1.1.5 in ./tutorial-env/lib/python3.10/site-packages (from -r requirements.txt (line 4)) (3.1.1.5)
Requirement already satisfied: requests==2.27.1 in ./tutorial-env/lib/python3.10/site-packages (from -r requirements.txt (line 5)) (2.27.1)
Requirement already satisfied: urllib3==1.26.9 in ./tutorial-env/lib/python3.10/site-packages (from -r requirements.txt (line 6)) (1.26.9)
```
# Memulai dengan Conda
Conda adalah package manager dan environment manager yang bisa kita gunakan dengan perintah command line pada Anaconda Prompt pada Windows, atau terminal pada macOS atau Linux.
## Memulai conda
Windows
- Pada Start menu, cari dan buka "Anaconda Prompt".

MacOS
- Buka Launchpad, lalu klik icon terminal

Linux
- Buka terminal

## Mengelola conda
Pastikan conda sudah terinstall dan dapat dijalankan pada sistem dengan mengetikkan:
```python
conda --version
```
Conda menampilkan nomor versi yang sudah terinstall. Kita tidak perlu navigasi ke direktori Anaconda.

`Catatan:
Jika kita mendapatkan pesan error, pastikan kita sudah menutup dan membuka ulang terminal setelah penginstallan, atau bisa juga lakukan sekarang. Lalu pastikan kita sudah masuk dengan akun user yang sama dengan yang kita gunakan untuk menginstall Anaconda atau Miniconda.`

Update conda ke _current version_. Ketik perintah berikut:
```python
conda update conda
```
Conda membandingkan versi, lalu menampilkan apa yang tersedia untuk diinstall.
Jika tersedia versi conda yang lebih baru, ketik `y` untuk update:
```python
Proceed ([y]/n)? y
```
## Mengelola environment
Conda memungkinkan kita untuk membuat environment terpisah yang memuat file, package, dan dependency yang tidak akan berinteraksi dengan environment lain.

Ketika kita mulai menggunakan conda, kita telah memiliki default environment bernama `base`. Kita tidak akan meletakkan program ke dalam base environment. Kita harus membuat environment terpisah untuk membuat program tetap terisolasi.
- - - - - -
(1) _Buat environment dan install package di dalamnya_

Kita akan menamai environment dengan nama `snowflakes` dan menginstall package BioPython. Pada Anaconda Prompt atau terminal, ketik:
```Python
conda create --name snowflakes biopython
```
Conda memeriksa apa yang dibutuhkan package tambahan  ("dependencies"), dan mengonfirmasi apakah kita mau _proceed_:
```Python
Proceed ([y]/n)? y
```
Ketik "y" dan klik Enter untuk _proceed_.
- - - - - - -
(2) _Untuk menggunakan atau mengaktifkan environment baru, ketik_:
- Windows: `conda activate snowflakes`
- macOS and Linux: `conda activate snowflakes`

Untuk versi conda sebelum 4.6, ketik:
- Windows: `activate snowflakes`
- macOS and Linux: `source activate snowflakes`

Sekarang kita sudah berada di dalam environment `snowflakes`. Semua command conda yang kita ketik akan masuk ke environment itu hingga kita meng-deactivate-kan nya.
- - - - - - -
(3) _Untuk melihat list semua environment, ketik_:
```Python
`conda info --envs`
```
List environment muncul seperti ini:
```Python
conda environments:

    base           /home/username/Anaconda3
    snowflakes   * /home/username/Anaconda3/envs/snowflakes
```
- - - - - - - - -
(4) _Kembali ke environment default (base)_: `conda activate`
- - - - - - - -
## Mengelola Python
Ketika kita membuat environment baru, conda menginstall versi Python yang sama dengan yang kita gunakan untuk men-download dan menginstall Anaconda/Miniconda. Jika kita ingin menggunakan versi Python berbeda, buat environment baru dan tulis versi Python yang kita inginkan.
- - - - - - - -
(1) _Buat environment bernama "snakes" yang berisi Python 3.9_:
```Python
conda create --name snakes python=3.9
```
Lalu ketik "y" dan klik Enter untuk proceed.
- - - - - - - -
(2) _Aktifkan environment baru_:
- Windows: `conda activate snakes`
- macOS and Linux: `conda activate snakes`

Untuk versi conda sebelum 4.6, ketik:
- Windows: `activate snakes`
- macOS and Linux: `source activate snakes`
- - - - - - - -
(3) _Pastikan environment snakes sudah ditambahkan dan sudah aktif_:
```Python
conda info --envs
```
Conda menampilkan list semua environment dengan tanda asterik (*) pada nama environment yang aktif
```Python
# conda environments:
#
base                     /home/username/anaconda3
snakes                *  /home/username/anaconda3/envs/snakes
snowflakes               /home/username/anaconda3/envs/snowflakes
```
- - - - - - - -
(4) _Pastikan versi Python apa yang ada di dalam environment saat ini_:
```Python
python --version
```
- - - - - - - - - -
(5) _Deactivate environment snakes dan kembali ke environment base_: `conda activate`
- - - - - - - - -
## Mengelola Package
Kita akan memeriksa package yang sudah kita install, periksa apa yang tersedia dan cari package tertentu dan menginstallnya.
- - - - - - - - 
(1) _Untuk mencari package yang sudah terinstall, aktifkan environment yang ingin kita cari_.
- - - - - - - - -
(2) _Periksa apakah package yang belum kita install bernama "beautifulsoup4" tersedia di repository Anaconda_:
```python
conda search beautifulsoup4
```
Conda menampilkan list semua package dengan nama tersebut pada repository Anaconda.
- - - - - - - - - 
(3) _Install package ini ke dalam environment_:
```python
conda install beautifulsoup4
```
- - - - - - - - -
(4) _Periksa apakah program yang baru diinstall ada di dalam environment ini_:
```python
conda list
```
