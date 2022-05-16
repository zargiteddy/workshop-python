# Akses ke Basis Data CockroachDB menggunakan psycopg2
Tutorial ini menunjukkan kita cara untuk membuat aplikasi Python sederhana dengan CockroachDB dan driver [psycopg2](https://www.psycopg.org/).

<br>

### Tahap 1. Mulai jalankan CockroachDB
Ada dua cara untuk memulai CockroachDB, yaitu dengan menggunakan CockroachDB Serverless (beta) dan dengan menggunakan Kluster Lokal. Di pertemuan 10 ini, saya menggunakan menggunakan CockroachDB Serverless (beta), berikut tahapannya:
<br>

#### Membuat cluster gratis
1. Daftar di akun CockroachDB Cloud di [sini](https://cockroachlabs.cloud/signup?referralId=docs_python_psycopg2&_ga=2.238008000.1798206515.1652698365-1974409797.1650908626). Kita bisa daftar menggunakan akun GitHub maupun langsung mendaftar akun baru di laman tersebut. Di sini saya daftar akun langsung. Untuk mendaftar akun CockroachDB, kita diminta untuk memasukkan alamat email, nama, password, dan nama organisasi (opsional). Jika sudah diisi, klik **Get Started**.
<br>

2. CockroachDB akan mengirimkan email verifikasi ke email yang kita tuliskan untuk mendaftar tadi. Masuk ke inbox kemudian cari email dari Cockroach Labs, kemudian klik tombol **Verify my email**.
<br>

3. Kemudian secara otomatis kita akan diarahkan ke laman Clusters. klik tombol **Create Cluster**.
<br>

4. Di laman **Create Your Cluster**, pilih plan Serverless supaya gratis. Pilih AWS sebagai cloud provider, pilih Region Singapore (ap-southeast-1), pilih Spend limit $0, kemudian tentukan nama yaitu plains-sheep (sudah ditentukan dari sana).
<br>

5. Klik tombol **Create your free cluster**. Cluster kita akan dibuat dalam beberapa detik dan akan muncul dialog **Create SQL user**.
<br>

#### Membuat user SQL
dialog 'Create SQL user' memungkinkan kita untuk membuat user SQL beserta passwordnya.

1. Tulis username di field **SQL user**. Di sini saya menggunakan nama depan saya yaitu 'raden'.
<br>

2. Klik **Generate & save password**.
<br>

3. Copy password tersebut kemudian simpan di tempat yang aman.
<br>

4. Klik **Next**.
<br>

#### Mendapatkan sertifikat root
Dialog **Connect to plains-sheep** menunjukan informasi tentang cara connect ke cluster yang tadi kita buat. Pada dialog tersebut ada nama SQL user yaitu 'raden', kemudian ada select option/language yaitu General connection string. Di dalam dialog itu juga ada field untuk mendownload CA Cert sesuai sistem operasi yang dideteksi secara otomatis (otomatis terdeteksi 'Linux' di laptop saya), sehingga command yang untuk download CA Cert disesuaikan dengan Linux.

1. Pilih **General connection string** dari dropdown **Select option**.
<br>

2. Buka terminal, kemudian jalankan command untuk mendownload CA Cert yang ada di section/field **Download CA Cert**. Driver client yang digunakan di tutorial ini membutuhkan sertifikat tersebut untuk connect ke CockroachDB Cloud.
```python
zargiteddy@shield:~$ curl --create-dirs -o $HOME/.postgresql/root.crt -O https://cockroachlabs.cloud/clusters/ef3ce24c-78b4-4b58-932c-5b279aee2449/cert
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100  2728    0  2728    0     0   7598      0 --:--:-- --:--:-- --:--:--  7620
```
<br>

#### Mendapatkan connection string
Buka section **General connection string**, lalu copy connection string dan simpan di tempat aman.
```python
postgresql://raden:REVEAL_PASSWORD@free-tier8.aws-ap-southeast-1.cockroachlabs.cloud:26257/defaultdb?sslmode=verify-full&options=--cluster=plains-sheep-1769
```
<br>

### Tahap 2. Mendapatkan kode sampel
Clone repo Github kode sampel:
```Python
zargiteddy@shield:~$ git clone https://github.com/cockroachlabs/hello-world-python-psycopg2
Cloning into 'hello-world-python-psycopg2'...
remote: Enumerating objects: 73, done.
remote: Counting objects: 100% (73/73), done.
remote: Compressing objects: 100% (51/51), done.
remote: Total 73 (delta 36), reused 51 (delta 21), pack-reused 0
Unpacking objects: 100% (73/73), 16.28 KiB | 694.00 KiB/s, done.
```
Kode sampel di dalam `example.py` melakukan hal-hal berikut:
- Membuat tabel `accounts` dan menyisipkan beberapa baris
- Mentransfer dana antar dua akun di dalam [transaction](https://www.cockroachlabs.com/docs/v21.2/transactions)
- Menghapus akun dari tabel sebelum keluar sehingga kita bisa menjalankan kembali kode _example_
<br>

### Tahap 3. Install driver psycopg2
`psycopg2-binary` merupakan satu-satunya dependensi modul pihak ketiga milik _sample app_. Untuk menginstall `psycopg2-binary`, jalankan perintah berikut:
```python
zargiteddy@shield:~$ pip install psycopg2-binary
Collecting psycopg2-binary
  Downloading psycopg2_binary-2.9.3-cp38-cp38-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (3.0 MB)
     |████████████████████████████████| 3.0 MB 507 kB/s 
Installing collected packages: psycopg2-binary
Successfully installed psycopg2-binary-2.9.3
```
<br>

### Tahap 4. Jalankan kode
1. Set environment variable DATABASE_URL ke connection string yang mengarah ke cluster CockroachDB Cloud milik kita (plains-sheep)
```python
zargiteddy@shield:~$ export DATABASE_URL="{postgresql://raden:PASSWORD@free-tier8.aws-ap-southeast-1.cockroachlabs.cloud:26257/defaultdb?sslmode=verify-full&options=--cluster=plains-sheep-1769}"
```
<br>

2. Jalankan kode
```python
zargiteddy@shield:~$ cd hello-world-python-psycopg2

zargiteddy@shield:~/hello-world-python-psycopg2$ python example.py
  File "example.py", line 43
    print(f"Balances at {time.asctime()}:")
                                         ^
SyntaxError: invalid syntax
```
Hasilnya error. Seharusnya menghasilkan output seperti ini:
```python
Balances at Fri Oct 30 18:27:00 2020:
(1, 1000)
(2, 250)
Balances at Fri Oct 30 18:27:00 2020:
(1, 900)
(2, 350)
```
- - - - - - - - - -
# Akses ke Basis Data CockroachDB menggunakan SQLAlchemy
Tutorial ini menunjukkan cara membuat aplikasi CRUD Python sederhana dengan CockroachDB dan SQLAlchemy

<br>

### Tahap 1. Mulai jalankan CockroachDB
(sudah dikerjakan di 'Akses ke Basis Data CockroachDB menggunakan psycopg2'. Langsung lanjut ke Tahap 2)

<br>

### Tahap 2. Mendapatkan kode
Clone repo GitHub kode:
```python
zargiteddy@shield:~$ git clone https://github.com/cockroachlabs/example-app-python-sqlalchemy/
Cloning into 'example-app-python-sqlalchemy'...
remote: Enumerating objects: 74, done.
remote: Counting objects: 100% (74/74), done.
remote: Compressing objects: 100% (45/45), done.
remote: Total 74 (delta 32), reused 64 (delta 27), pack-reused 0
Unpacking objects: 100% (74/74), 20.26 KiB | 864.00 KiB/s, done.
```
Berikut struktur direktori proyek tersebut:
```python
├── README.md
├── dbinit.sql
├── main.py
├── models.py
└── requirements.txt
```
File `requirements.txt` berisi pustaka/library yang diperlukan untuk connect ke CockroachDB dengan SQLAlchemy, termasuk [sqlalchemy-cockroachdb Python package](https://github.com/cockroachdb/sqlalchemy-cockroachdb), yang menjelaskan beberapa perbedaan antara CockroachDB dan PostgreSQL:
```python
psycopg2-binary
sqlalchemy
sqlalchemy-cockroachdb
```
File `dbinit.sql` menginisialisasi skema database yang digunakan aplikasi:
```python
CREATE TABLE accounts (
    id UUID PRIMARY KEY,
    balance INT8
);
```
File `models.py` menggunakan SQLAlchemy untuk memetakan tabel `Accounts` ke objek Python:
```Python
from sqlalchemy import Column, Integer
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Account(Base):
    """The Account class corresponds to the "accounts" database table.
    """
    __tablename__ = 'accounts'
    id = Column(UUID(as_uuid=True), primary_key=True)
    balance = Column(Integer)
```
File `main.py` menggunakan SQLAlchemy untuk memetakan method Python ke dalam operasi MySQL:
```python
"""This simple CRUD application performs the following operations sequentially:
    1. Creates 100 new accounts with randomly generated IDs and randomly-computed balance amounts.
    2. Chooses two accounts at random and takes half of the money from the first and deposits it
     into the second.
    3. Chooses five accounts at random and deletes them.
"""

from math import floor
import os
import random
import uuid

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy_cockroachdb import run_transaction
from sqlalchemy.orm.exc import NoResultFound, MultipleResultsFound

from models import Account

# The code below inserts new accounts.


def create_accounts(session, num):
    """Create N new accounts with random account IDs and account balances.
    """
    print("Creating new accounts...")
    new_accounts = []
    while num > 0:
        account_id = uuid.uuid4()
        account_balance = floor(random.random()*1_000_000)
        new_accounts.append(Account(id=account_id, balance=account_balance))
        seen_account_ids.append(account_id)
        print(f"Created new account with id {account_id} and balance {account_balance}.")
        num = num - 1
    session.add_all(new_accounts)


def transfer_funds_randomly(session, one, two):
    """Transfer money between two accounts.
    """
    try:
        source = session.query(Account).filter(Account.id == one).one()
    except NoResultFound:
        print("No result was found")
    except MultipleResultsFound:
        print("Multiple results were found")
    dest = session.query(Account).filter(Account.id == two).first()
    print(f"Random account balances:\nAccount {one}: {source.balance}\nAccount {two}: {dest.balance}")

    amount = floor(source.balance/2)
    print(f"Transferring {amount} from account {one} to account {two}...")

    # Check balance of the first account.
    if source.balance < amount:
        raise ValueError(f"Insufficient funds in account {one}")
    source.balance -= amount
    dest.balance += amount

    print(f"Transfer complete.\nNew balances:\nAccount {one}: {source.balance}\nAccount {two}: {dest.balance}")


def delete_accounts(session, num):
    """Delete N existing accounts, at random.
    """
    print("Deleting existing accounts...")
    delete_ids = []
    while num > 0:
        delete_id = random.choice(seen_account_ids)
        delete_ids.append(delete_id)
        seen_account_ids.remove(delete_id)
        num = num - 1

    accounts = session.query(Account).filter(Account.id.in_(delete_ids)).all()

    for account in accounts:
        print(f"Deleted account {account.id}.")
        session.delete(account)


if __name__ == '__main__':
    # For cockroach demo:
    # DATABASE_URL=postgresql://demo:<demo_password>@127.0.0.1:26257?sslmode=require
    # For CockroachCloud:
    # DATABASE_URL=postgresql://<username>:<password>@<globalhost>:26257/<cluster_name>.defaultdb?sslmode=verify-full&sslrootcert=<certs_dir>/<ca.crt>
    db_uri = os.environ['DATABASE_URL'].replace("postgresql://", "cockroachdb://")
    try:
        engine = create_engine(db_uri)
    except Exception as e:
        print("Failed to connect to database.")
        print(f"{e}")

    seen_account_ids = []

    run_transaction(sessionmaker(bind=engine),
                    lambda s: create_accounts(s, 100))

    from_id = random.choice(seen_account_ids)
    to_id = random.choice([id for id in seen_account_ids if id != from_id])

    run_transaction(sessionmaker(bind=engine),
                    lambda s: transfer_funds_randomly(s, from_id, to_id))

    run_transaction(sessionmaker(bind=engine), lambda s: delete_accounts(s, 5))
```
`main.py` juga mengeksekusi method `main` di program.

<br>

### Tahap 3. Install kebutuhan aplikasi
Tutorial ini menggunakan [virtualenv](https://virtualenv.pypa.io/en/latest/) untuk manajemen dependensi.
<br>

1. Install `virtualenv`
```python
zargiteddy@shield:~$ sudo apt install python3-virtualenv
```
<br>

2. Pada level atas dari direktori proyek, buat dan aktifkan virtual environment:
```python
zargiteddy@shield:~$ virtualenv env
created virtual environment CPython3.8.10.final.0-64 in 426ms
  creator CPython3Posix(dest=/home/zargiteddy/env, clear=False, global=False)
  seeder FromAppData(download=False, pip=latest, setuptools=latest, wheel=latest, pkg_resources=latest, via=copy, app_data_dir=/home/zargiteddy/.local/share/virtualenv/seed-app-data/v1.0.1.debian.1)
  activators BashActivator,CShellActivator,FishActivator,PowerShellActivator,PythonActivator,XonshActivator

zargiteddy@shield:~$ source env/bin/activate
```
<br>

3. Install modul yang dibutuhkan ke dalam virtual environment:
```python
(env) zargiteddy@shield:~$ pip install -r requirements.txt
Collecting certifi==2021.10.8
  Using cached certifi-2021.10.8-py2.py3-none-any.whl (149 kB)
Collecting charset-normalizer==2.0.12
  Using cached charset_normalizer-2.0.12-py3-none-any.whl (39 kB)
Collecting idna==3.3
  Using cached idna-3.3-py3-none-any.whl (61 kB)
Collecting novas==3.1.1.5
  Using cached novas-3.1.1.5.tar.gz (135 kB)
Collecting requests==2.27.1
  Using cached requests-2.27.1-py2.py3-none-any.whl (63 kB)
Collecting urllib3==1.26.9
  Using cached urllib3-1.26.9-py2.py3-none-any.whl (138 kB)
Building wheels for collected packages: novas
  Building wheel for novas (setup.py) ... done
  Created wheel for novas: filename=novas-3.1.1.5-cp38-cp38-linux_x86_64.whl size=169859 sha256=c6be6cbcbd58e0704fdaad551f74b7fee5d87583aac17c03a3fc0e2811c94aca
  Stored in directory: /home/zargiteddy/.cache/pip/wheels/5f/3b/72/e7dba9d085106f46a87b5c1ce1405b6132fb10e343d8d312a0
Successfully built novas
Installing collected packages: certifi, charset-normalizer, idna, novas, urllib3, requests
Successfully installed certifi-2021.10.8 charset-normalizer-2.0.12 idna-3.3 novas-3.1.1.5 requests-2.27.1 urllib3-1.26.9
```
<br>

### Tahap 4. Inisialisasi database
1. Set environment variable DATABASE_URL ke connection string untuk cluster kita:
```python
(env) zargiteddy@shield:~$ export DATABASE_URL="{postgresql://raden:PASSWORD@free-tier8.aws-ap-southeast-1.cockroachlabs.cloud:26257/defaultdb?sslmode=verify-full&options=--cluster=plains-sheep-1769}"
```
<br>

2. Untuk inisialisasi database, gunakan perintah [cockroach sql](https://www.cockroachlabs.com/docs/v21.2/cockroach-sql) untuk mengeksekusi statement SQL di dalam file `dbinit.sql`:
```python
cat dbinit.sql | cockroach sql --url $DATABASE_URL
```
Statement tersebut mengeksekusi:
```python
CREATE TABLE

Time: 102ms
```
<br>

### Tahap 5. Jalankan kode
`main.py` menggunakan connection string yang tersimpan ke dalam environment variable DATABASE_URL untuk connect ke cluster kita dan mengeksekusi kode.
Jalankan kode:
```python
python main.py
```
Kemudian aplikasi akan connect ke CockroachDB, lalu akan melakukan insert, update, dan delete baris.

Output:
```python
Creating new accounts...
Created new account with id 3a8b74c8-6a05-4247-9c60-24b46e3a88fd and balance 248835.
Created new account with id c3985926-5b77-4c6d-a73d-7c0d4b2a51e7 and balance 781972.
...
Created new account with id 7b41386c-11d3-465e-a2a0-56e0dcd2e7db and balance 984387.
Random account balances:
Account 7ad14d02-217f-48ca-a53c-2c3a2528a0d9: 800795
Account 4040aeba-7194-4f29-b8e5-a27ed4c7a297: 149861
Transferring 400397 from account 7ad14d02-217f-48ca-a53c-2c3a2528a0d9 to account 4040aeba-7194-4f29-b8e5-a27ed4c7a297...
Transfer complete.
New balances:
Account 7ad14d02-217f-48ca-a53c-2c3a2528a0d9: 400398
Account 4040aeba-7194-4f29-b8e5-a27ed4c7a297: 550258
Deleting existing accounts...
Deleted account 41247e24-6210-4032-b622-c10b3c7222de.
Deleted account 502450e4-6daa-4ced-869c-4dff62dc52de.
Deleted account 6ff06ef0-423a-4b08-8b87-48af2221bc18.
Deleted account a1acb134-950c-4882-9ac7-6d6fbdaaaee1.
Deleted account e4f33c55-7230-4080-b5ac-5dde8a7ae41d.
```
Di dalam shell SQL yang terkoneksi ke cluster, kita bisa memeriksa jika baris telah ter insert, update, dan delete.
```python
SELECT COUNT(*) FROM accounts;
```
output:
```python
 count
---------
     95
(1 row)
```





