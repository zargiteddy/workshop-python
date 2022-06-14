# Responsi

Code:

```python
import requests
import csv
import os

nama_file = 'responsi.csv'
url = 'https://www1.ncdc.noaa.gov/pub/data/cdo/samples/PRECIP_HLY_sample_csv.csv'
responsi = requests.get(url)

with open(nama_file, 'w') as file:
    file.write(str(responsi.content))

with open(nama_file, 'r') as file:
    csv_reader = csv.reader(file, delimiter=',')
    for line in csv_reader:
        print (line)
```
<br>

Output:

```python
(workshop) zargiteddy@shield:~$ /home/zargiteddy/miniconda3/envs/workshop/bin/python "/home/zargiteddy/BACKUP WORKSHOP/responsi/responsi.py"
["b'STATION", 'STATION_NAME', 'ELEVATION', 'LATITUDE', 'LONGITUDE', 'DATE', 'HPCP', 'Measurement Flag', 'Quality Flag\\nCOOP:310301', 'ASHEVILLE NC US', '682.1', '35.5954', '-82.5568', '20100101 00:00', '99999', ']', ' \\nCOOP:310301', 'ASHEVILLE NC US', '682.1', '35.5954', '-82.5568', '20100101 01:00', '0', 'g', ' \\nCOOP:310301', 'ASHEVILLE NC US', '682.1', '35.5954', '-82.5568', '20100102 06:00', '1', ' ', " \\n'"]
```
<br>

Penjelasan:
- import request digunakan untuk mengimport modul yang memungkinkan kita untuk mengirim request HTTP untuk kemudian HTTP tersebut me-return response object dengan data-data respon seperti content, encoding, dan sebagainya.
- import csv digunakan sebagai sarana untuk read dan write ke dalam file CSV
- import os digunakan untuk mengimport modul untuk berinteraksi dengan operating system
- Kita buat variabel bernama `nama_file` untuk menentukan nama file csv setelah di-download nanti
- Setelah itu ada variabel `url` untuk menampung link sumber file CSV
- variabel `responsi` digunakan untuk mendownload file yang ada di url tersebut menggunakan fungsi `get()` milik `requests`
- Setelah itu kita buka file CSV tersebut dengan open() lalu diberikan parameter berupa variabel `nama_file` dan `w` (write) yang lalu kita namai sebagai `file`. Lalu, write dengan kode `file.write(str(responsi.content))`.
- Terakhir kita buka file CSV tersebut dengan open() lalu diberikan parameter berupa variabel `nama_file` dan `r` (read) yang lalu kita namai sebagai `file`. Di dalamnya deklarasikan variabel `csv_reader` untuk read file tersebut sekaligus memberikan _delimiter_ atau pembatas berupa tanda koma. Lalu buat _looping_ untuk menampilkan data yang ada pada file tersebut.

-------------------

### Thank You.