# 10 minutes to pandas
Chapter ini adalah sebuah pengenalan singkat yang ditujukan untuk pengguna baru pandas.

-----------------------------

*NOTE:
Beberapa data di DataFrame yang di-generate dari _np.random_ yang ditampilkan di file README ini berbeda-beda dengan yang ada di file ipynb di folder src. Hal ini dikarenakan saya run cell beberapa kali sehingga angka randomnya selalu berganti. Terima kasih.

--------------------------

Pertama kita membutuhkan NumPy. NumPy adalah sebuah package fundamental yang digunakan untuk komputasi ilmiah pada pemrograman Python. NumPy adalah library yang menyediakan objek array multidimensional, berbagai objek turunan (seperti _masked array_ dan matriks), dan berbagai macam rutinitas untuk operasi cepat pada array, termasuk matematika, logika, manipulasi bentuk, _sorting_, _selecting_, I/O, transformasi Fourier diskrit, aljabar linier dasar, operasi statistik dasar , simulasi random, dan lain-lain.

_Install NumPy:_

```python
(workshop) zargiteddy@shield:~$ conda install -c anaconda numpy
Collecting package metadata (current_repodata.json): done
Solving environment: done


==> WARNING: A newer version of conda exists. <==
  current version: 4.12.0
  latest version: 4.13.0

Please update conda by running

    $ conda update -n base -c defaults conda



## Package Plan ##

  environment location: /home/zargiteddy/miniconda3/envs/workshop

  added / updated specs:
    - numpy


The following packages will be downloaded:

    package                    |            build
    ---------------------------|-----------------
    blas-1.0                   |              mkl           6 KB  anaconda
    intel-openmp-2021.4.0      |    h06a4308_3561         8.8 MB  anaconda
    mkl-2021.4.0               |     h06a4308_640       219.1 MB  anaconda
    mkl-service-2.4.0          |  py310h7f8727e_0         213 KB  anaconda
    mkl_fft-1.3.1              |  py310hd6ae3a3_0         697 KB  anaconda
    mkl_random-1.2.2           |  py310h00e6091_0         1.2 MB  anaconda
    numpy-1.21.5               |  py310hfa59a62_2          10 KB  anaconda
    numpy-base-1.21.5          |  py310h9585f30_2        14.9 MB  anaconda
    ------------------------------------------------------------
                                           Total:       245.0 MB

The following NEW packages will be INSTALLED:

  blas               anaconda/linux-64::blas-1.0-mkl
  intel-openmp       anaconda/linux-64::intel-openmp-2021.4.0-h06a4308_3561
  mkl                anaconda/linux-64::mkl-2021.4.0-h06a4308_640
  mkl-service        anaconda/linux-64::mkl-service-2.4.0-py310h7f8727e_0
  mkl_fft            anaconda/linux-64::mkl_fft-1.3.1-py310hd6ae3a3_0
  mkl_random         anaconda/linux-64::mkl_random-1.2.2-py310h00e6091_0
  numpy              anaconda/linux-64::numpy-1.21.5-py310hfa59a62_2
  numpy-base         anaconda/linux-64::numpy-base-1.21.5-py310h9585f30_2


Proceed ([y]/n)? y


Downloading and Extracting Packages
mkl_fft-1.3.1        | 697 KB    | ##################################### | 100% 
numpy-base-1.21.5    | 14.9 MB   | ##################################### | 100% 
mkl-service-2.4.0    | 213 KB    | ##################################### | 100% 
blas-1.0             | 6 KB      | ##################################### | 100% 
numpy-1.21.5         | 10 KB     | ##################################### | 100% 
mkl_random-1.2.2     | 1.2 MB    | ##################################### | 100% 
intel-openmp-2021.4. | 8.8 MB    | ##################################### | 100% 
mkl-2021.4.0         | 219.1 MB  | ##################################### | 100% 
Preparing transaction: done
Verifying transaction: done
Executing transaction: done
```
---------------------------------------
Kita juga membutuhkan pandas. pandas merupakan library Python yang digunakan untuk melakukan operasi matematika dengan cara yang fleksibel. Pandas adalah library _open-source_ yang menawarkan tool analisis data _high-performance_ yang bisa digunakan untuk analisis data dan manipulasi data sehingga pengguna library ini bisa mendapatkan informasi dari data yang dianalisis.

_Install pandas:_

```python
(workshop) zargiteddy@shield:~$ conda install -c anaconda pandas
Collecting package metadata (current_repodata.json): done
Solving environment: done


==> WARNING: A newer version of conda exists. <==
  current version: 4.12.0
  latest version: 4.13.0

Please update conda by running

    $ conda update -n base -c defaults conda



## Package Plan ##

  environment location: /home/zargiteddy/miniconda3/envs/workshop

  added / updated specs:
    - pandas


The following packages will be downloaded:

    package                    |            build
    ---------------------------|-----------------
    bottleneck-1.3.4           |  py310h9102076_0         337 KB  anaconda
    numexpr-2.7.3              |  py310hd732450_1         443 KB  anaconda
    pandas-1.4.2               |  py310h295c915_0        33.6 MB  anaconda
    pytz-2021.3                |     pyhd3eb1b0_0         224 KB  anaconda
    ------------------------------------------------------------
                                           Total:        34.5 MB

The following NEW packages will be INSTALLED:

  bottleneck         anaconda/linux-64::bottleneck-1.3.4-py310h9102076_0
  numexpr            anaconda/linux-64::numexpr-2.7.3-py310hd732450_1
  pandas             anaconda/linux-64::pandas-1.4.2-py310h295c915_0
  pytz               anaconda/noarch::pytz-2021.3-pyhd3eb1b0_0


Proceed ([y]/n)? y


Downloading and Extracting Packages
pandas-1.4.2         | 33.6 MB   | ##################################### | 100% 
bottleneck-1.3.4     | 337 KB    | ##################################### | 100% 
numexpr-2.7.3        | 443 KB    | ##################################### | 100% 
pytz-2021.3          | 224 KB    | ##################################### | 100% 
Preparing transaction: done
Verifying transaction: done
Executing transaction: done
```
--------------------------------------
Selanjutnya, kita bisa install (opsional) IPython (Interactive Python). IPython adalah sebuah command shell untuk komputasi interaktif yang menawarkan shell interaktif, support untuk visualisasi dara interaktif dan penggunaan toolkit GUI, interpreter yang fleksibel, dan tool untuk komputasi parallel. Selain itu, IPython juga menyediakan interface notebook berbasis web dengan support untuk code, teks, ekspresi matematika, inline plots, dan media-media lain.

_Install IPython_

```python
(workshop) zargiteddy@shield:~$ conda install -c conda-forge ipython
Collecting package metadata (current_repodata.json): done
Solving environment: done


==> WARNING: A newer version of conda exists. <==
  current version: 4.12.0
  latest version: 4.13.0

Please update conda by running

    $ conda update -n base -c defaults conda



## Package Plan ##

  environment location: /home/zargiteddy/miniconda3/envs/workshop

  added / updated specs:
    - ipython


The following packages will be downloaded:

    package                    |            build
    ---------------------------|-----------------
    ipython-8.4.0              |  py310hff52083_0         1.1 MB  conda-forge
    ------------------------------------------------------------
                                           Total:         1.1 MB

The following packages will be UPDATED:

  ca-certificates    anaconda::ca-certificates-2022.4.26-h~ --> conda-forge::ca-certificates-2022.5.18.1-ha878542_0
  certifi            anaconda/noarch::certifi-2020.6.20-py~ --> conda-forge/linux-64::certifi-2022.5.18.1-py310hff52083_0
  ipython            anaconda::ipython-8.2.0-py310h06a4308~ --> conda-forge::ipython-8.4.0-py310hff52083_0
  openssl               anaconda::openssl-1.1.1n-h7f8727e_0 --> conda-forge::openssl-1.1.1o-h166bdaf_0


Proceed ([y]/n)? y


Downloading and Extracting Packages
ipython-8.4.0        | 1.1 MB    | ##################################### | 100% 
Preparing transaction: done
Verifying transaction: done
Executing transaction: done
```
------------------------
Kita import dulu numpy dan pandas dengan menjalankan kode berikut:

```python
In [1]: import numpy as np
In [2]: import pandas as pd
```

## Object Creation
Lihat [Intro to data structures section](https://pandas.pydata.org/pandas-docs/stable/user_guide/dsintro.html#dsintro).

Membuat [Series](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.html#pandas.Series) dengan memasukkan list berisi value, memungkinkan pandas untuk membuat index integer default:

```python
In [3]: s = pd.Series([1, 3, 5, np.nan, 6, 8])
In [4]: s
Out[4]: 0    1.0
        1    3.0
        2    5.0
        3    NaN
        4    6.0
        5    8.0
        dtype: float64
```
Membuat [DataFrame](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html#pandas.DataFrame) dengan memasukkan array NumPy, dengan index datetime dan kolom yang dilabel:

```python
In [5]: dates = pd.date_range("20130101", periods=6)
In [6]: dates
Out[6]: 
DatetimeIndex(['2013-01-01', '2013-01-02', '2013-01-03', '2013-01-04',
               '2013-01-05', '2013-01-06'],
              dtype='datetime64[ns]', freq='D')
In [7]: df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list("ABCD"))
In [8]: df
Out[8]: 
                   A         B         C         D
2013-01-01 -0.450825 -1.997097 	0.454911 -0.596387
2013-01-02  0.305567 -0.253346 	0.120193  1.675071
2013-01-03 -0.551129 -0.520855 -0.863102 -0.064890
2013-01-04  1.078149 -1.553706 	1.758851 -0.927765
2013-01-05  0.561016 -0.283202 	0.424848 -0.803990
2013-01-06  0.205565  1.683160 -0.506140 -0.016024
```
Membuat [DataFrame](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html#pandas.DataFrame) dengan memasukkan dictionary objek yang bisa diconvert menjadi struktur yang mirip series:

```python
In [9]: df2 = pd.DataFrame(
            {
                "A": 1.0,
                "B": pd.Timestamp("20130102"),
                "C": pd.Series(1, index=list(range(4)), dtype="float32"),
                "D": np.array([3] * 4, dtype="int32"),
                "E": pd.Categorical(["test", "train", "test", "train"]),
                "F": "foo",
            }
        )
In [10]: df2
Out[10]: 
     A          B    C  D      E    F
0  1.0 2013-01-02  1.0  3   test  foo
1  1.0 2013-01-02  1.0  3  train  foo
2  1.0 2013-01-02  1.0  3   test  foo
3  1.0 2013-01-02  1.0  3  train  foo
```
Kolom yang menghasilkan DataFrame memiliki [dtypes](https://pandas.pydata.org/pandas-docs/stable/user_guide/basics.html#basics-dtypes) yang berbeda:

```python
In [11]: df2.dtypes
Out[11]:
A           float64
B    datetime64[ns]
C           float32
D             int32
E          category
F            object
dtype: object
```
Jika kita menggunakan IPython, tab completion untuk nama kolom (juga atribut public) secara otomatis sudah terpasang. Berikut subset atribut yang akan di-completed:

```python
In [12]: df2.<TAB>  # noqa: E225, E999
df2.A                  df2.bool
df2.abs                df2.boxplot
df2.add                df2.C
df2.add_prefix         df2.clip
df2.add_suffix         df2.columns
df2.align              df2.copy
df2.all                df2.count
df2.any                df2.combine
df2.append             df2.D
df2.apply              df2.describe
df2.applymap           df2.diff
df2.B                  df2.duplicated
```
Seperti yang bisa kita lihat, kolom A, B, C, dan D secara otomatis di-tab completed. E dan F juga ada; atribut lainnya telah dipotong untuk lebih singkatnya.

----------------------

## Viewing Data
Lihat [Basics Section](https://pandas.pydata.org/pandas-docs/stable/user_guide/basics.html#basics).

Berikut cara melihat (view) bagian atas dan bawah baris frame:

```python
In [13]: df.head()
Out[13]: 
                   A         B         C         D
2013-01-01 -0.450825 -1.997097 	0.454911 -0.596387
2013-01-02  0.305567 -0.253346 	0.120193  1.675071
2013-01-03 -0.551129 -0.520855 -0.863102 -0.064890
2013-01-04  1.078149 -1.553706 	1.758851 -0.927765
2013-01-05  0.561016 -0.283202 	0.424848 -0.803990
In [14]: df.tail(3)
Out[14]: 
                   A         B         C         D
2013-01-04  1.078149 -1.553706 	1.758851 -0.927765
2013-01-05  0.561016 -0.283202 	0.424848 -0.803990
2013-01-06  0.205565  1.683160 -0.506140 -0.016024
```
Tampilkan index, kolom:

```python
In [15]: df.index
Out[15]: 
DatetimeIndex(['2013-01-01', '2013-01-02', '2013-01-03', '2013-01-04',
               '2013-01-05', '2013-01-06'],
              dtype='datetime64[ns]', freq='D')
In [16]: df.columns
Out[16]: Index(['A', 'B', 'C', 'D'], dtype='object')
```
[DataFrame.to_numpy()](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_numpy.html#pandas.DataFrame.to_numpy) memberikan NumPy representasi dari data yang mendasarinya. Perhatikan bahwa hal ini bisa menjadi operasi yang "mahal" ketika DataFrame kita memiliki kolom dengan tipe data yang berbeda yang menjadi perbedaan mendasar antara pandas dan NumPy: array NumPy memiliki satu tipe dtype untuk seluruh array, sementara DataFrame pandas memiliki satu dtype per kolom. Ketika kita memanggil [DataFrame.to_numpy()](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_numpy.html#pandas.DataFrame.to_numpy), pandas akan mencari dtype NumPy yang bisa menampung semua dtype di dalam DataFrame.

Untuk df, yaitu DataFrame berisi nilai berupa floating-point, [DataFrame.to_numpy()](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_numpy.html#pandas.DataFrame.to_numpy) cepat dan tidak membutuhkan penyalinan data:

```python
In [17]: df.to_numpy()
Out[17]: 
array([[-0.45082523, -1.99709731,  0.45491106, -0.59638695],
       [ 0.30556659, -0.25334557,  0.1201927 ,  1.67507065],
       [-0.55112863, -0.52085534, -0.86310178, -0.06488971],
       [ 1.07814874, -1.55370647,  1.75885117, -0.92776459],
       [ 0.56101602, -0.28320185,  0.42484848, -0.80398959],
       [ 0.2055645 ,  1.68315996, -0.5061398 , -0.01602386]])
```
Untuk df2, DataFrame dengan beberapa dtype, [DataFrame.to_numpy()](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_numpy.html#pandas.DataFrame.to_numpy) cenderung "mahal":

```python
In [18]: df2.to_numpy()
Out[18]: 
array([[1.0, Timestamp('2013-01-02 00:00:00'), 1.0, 3, 'test', 'foo'],
       [1.0, Timestamp('2013-01-02 00:00:00'), 1.0, 3, 'train', 'foo'],
       [1.0, Timestamp('2013-01-02 00:00:00'), 1.0, 3, 'test', 'foo'],
       [1.0, Timestamp('2013-01-02 00:00:00'), 1.0, 3, 'train', 'foo']],
      dtype=object)
```
[describe()](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.describe.html#pandas.DataFrame.describe) menampilkan summary statistik sederhana data milik kita:

```python
In [19]: df.describe()
Out[19]:
              A         B         C         D
count  6.000000  6.000000  6.000000  6.000000
mean   0.191390 -0.487508  0.231594 -0.122331
std    0.616438  1.282585  0.913756  0.957430
min   -0.551129 -1.997097 -0.863102 -0.927765
25%   -0.286728 -1.295494 -0.349557 -0.752089
50%    0.255566 -0.402029  0.272521 -0.330638
75%    0.497154 -0.260810  0.447395 -0.028240
max    1.078149  1.683160  1.758851  1.675071
```
Memindah data:

```python
In [20]: df.T
Out[20]: 
   2013-01-01  2013-01-02  2013-01-03  2013-01-04  2013-01-05  2013-01-06
A   -0.450825 	 0.305567   -0.551129 	 1.078149    0.561016 	 0.205565
B   -1.997097 	-0.253346   -0.520855 	-1.553706   -0.283202 	 1.683160
C    0.454911 	 0.120193   -0.863102 	 1.758851    0.424848 	-0.506140
D   -0.596387 	 1.675071   -0.064890 	-0.927765   -0.803990 	-0.016024
```
Mengurutkan berdasarkan axis:

```python
In [21]: df.sort_index(axis=1, ascending=False)
Out[21]: 
                   D         C         B         A
2013-01-01 -0.596387  0.454911 -1.997097 -0.450825
2013-01-02  1.675071  0.120193 -0.253346  0.305567
2013-01-03 -0.064890 -0.863102 -0.520855 -0.551129
2013-01-04 -0.927765  1.758851 -1.553706  1.078149
2013-01-05 -0.803990  0.424848 -0.283202  0.561016
2013-01-06 -0.016024 -0.506140 	1.683160  0.205565
```
Mengurutkan berdasarkan nilai:

```python
In [22]: df.sort_values(by="B")
Out[22]: 
                   A         B         C         D
2013-01-01 -0.450825 -1.997097 	0.454911 -0.596387
2013-01-04  1.078149 -1.553706 	1.758851 -0.927765
2013-01-03 -0.551129 -0.520855 -0.863102 -0.064890
2013-01-05  0.561016 -0.283202 	0.424848 -0.803990
2013-01-02  0.305567 -0.253346 	0.120193  1.675071
2013-01-06  0.205565 1.683160  -0.506140 -0.016024
```
-----------------------

## Selection
Lihat dokumentasi indexing [Indexing and Selecting Data](https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#indexing) dan [MultiIndex / Advanced Indexing](https://pandas.pydata.org/pandas-docs/stable/user_guide/advanced.html#advanced).

### Getting
Memilih satu kolom, yang menghasilkan series, ekuivalen dengan `df.A`:

```python
In [23]: df["A"]
Out[23]: 
2013-01-01   -0.450825
2013-01-02    0.305567
2013-01-03   -0.551129
2013-01-04    1.078149
2013-01-05    0.561016
2013-01-06    0.205565
Freq: D, Name: A, dtype: float64
```
Memilih via `[]`, yang memotong baris:

```python
In [24]: df[0:3]
Out[24]: 
                   A         B         C         D
2013-01-01 -0.450825 -1.997097 	0.454911 -0.596387
2013-01-02  0.305567 -0.253346 	0.120193  1.675071
2013-01-03 -0.551129 -0.520855 -0.863102 -0.064890

In [25]: df["20130102":"20130104"]
Out[25]: 
                   A         B         C         D
2013-01-02  0.305567 -0.253346 	0.120193  1.675071
2013-01-03 -0.551129 -0.520855 -0.863102 -0.064890
2013-01-04  1.078149 -1.553706 	1.758851 -0.927765
```
### Selection by label
Lihat di [Selection by Label](https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#indexing-label).

Untuk mendapatkan cross section menggunakan label:

```python
In [26]: df.loc[dates[0]]
Out[26]: 
A   -0.450825
B   -1.997097
C    0.454911
D   -0.596387
Name: 2013-01-01 00:00:00, dtype: float64
```
Memilih multi-axis dengan label:

```python
In [27]: df.loc[:, ["A", "B"]]
Out[27]: 
                   A         B
2013-01-01 -0.450825 -1.997097
2013-01-02  0.305567 -0.253346
2013-01-03 -0.551129 -0.520855
2013-01-04  1.078149 -1.553706
2013-01-05  0.561016 -0.283202
2013-01-06  0.205565  1.683160
```
Menampilkan _slicing_ label, kedua _endpoint_ juga termasuk:

```python
In [28]: df.loc["20130102":"20130104", ["A", "B"]]
Out[28]: 
                   A         B
2013-01-02  0.305567 -0.253346
2013-01-03 -0.551129 -0.520855
2013-01-04  1.078149 -1.553706
```
Pengurangan di dalam dimensi objek yang di-return:

```python
In [29]: df.loc["20130102", ["A", "B"]]
Out[29]: 
A    0.305567
B   -0.253346
Name: 2013-01-02 00:00:00, dtype: float64
```
Untuk mendapatkan nilai scalar:

```python
In [30]: df.loc[dates[0], "A"]
Out[30]: -0.45082522637014566
```
Untuk mendapatkan akses cepat ke scalar:

```python
In [31]: df.loc[dates[0], "A"]
Out[31]: -0.45082522637014566
```
### Selection by position
Lihat di [Selection by Position](https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#indexing-integer).

Pilih via posisi integer yang dimasukkan:

```python
In [32]: df.iloc[3]
Out[32]: 
A    1.078149
B   -1.553706
C    1.758851
D   -0.927765
Name: 2013-01-04 00:00:00, dtype: float64
```
Dengan slice integer:

```python
In [33]: df.iloc[3:5, 0:2]
Out[33]: 
                   A         B
2013-01-04  1.078149 -1.553706
2013-01-05  0.561016 -0.283202
```
Dengan list lokasi posisi integer:

```python
In [34]: df.iloc[[1, 2, 4], [0, 2]]
Out[34]: 
                   A         C
2013-01-02  0.305567  0.120193
2013-01-03 -0.551129 -0.863102
2013-01-05  0.561016  0.424848
```
Untuk _slicing_ baris secara eksplisit:

```python
In [35]: df.iloc[1:3, :]
Out[35]:
                   A         B         C         D
2013-01-02  0.305567 -0.253346 	0.120193  1.675071
2013-01-03 -0.551129 -0.520855 -0.863102 -0.064890
``` 
Untuk _slicing_ kolom secara eksplisit:

```python
In [36]: df.iloc[:, 1:3]
Out[36]: 
                   B         C
2013-01-01 -1.997097  0.454911
2013-01-02 -0.253346  0.120193
2013-01-03 -0.520855 -0.863102
2013-01-04 -1.553706  1.758851
2013-01-05 -0.283202  0.424848
2013-01-06  1.683160 -0.506140
```
Untuk mendapatkan nilai secara eksplisit:

```python
In [37]: df.iloc[1, 1]
Out[37]: -0.2533455737811998
```
Untuk mendapatkan akses cepat ke scalar:

```python
In [38]: df.iat[1, 1]
Out[38]: -0.2533455737811998
```
### Boolean indexing
Menggunakan nilai satu kolom untuk memilih data:

```python
In [39]: df[df["A"] > 0]
Out[39]: 
                   A         B         C         D
2013-01-02  0.305567 -0.253346 	0.120193  1.675071
2013-01-04  1.078149 -1.553706 	1.758851 -0.927765
2013-01-05  0.561016 -0.283202 	0.424848 -0.803990
2013-01-06  0.205565 1.683160  -0.506140 -0.016024
```
Memilih value dari DataFrame dimana kondisi boolean terpenuhi:

```python
In [40]: df[df > 0]
Out[40]: 
                   A         B         C         D
2013-01-01       NaN 	   NaN  0.454911       NaN
2013-01-02  0.305567 	   NaN 	0.120193  1.675071
2013-01-03       NaN 	   NaN 	     NaN       NaN
2013-01-04  1.078149 	   NaN 	1.758851       NaN
2013-01-05  0.561016 	   NaN 	0.424848       NaN
2013-01-06       NaN  0.113648       NaN  0.524988
```
Gunakan method [isin()](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.isin.html#pandas.Series.isin) untuk filtering:

```python
In [41]: df2 = df.copy()
In [42]: df2["E"] = ["one", "one", "two", "three", "four", "three"]
In [43]: df2
Out[43]: 
                   A         B         C         D      E
2013-01-01  0.450825 -1.997097 	0.454911 -0.596387    one
2013-01-02  0.305567  0.253346  0.120193  1.675071    one
2013-01-03 -0.551129 -0.520855 -0.863102 -0.064890    two
2013-01-04  1.078149 -1.553706 	1.758851 -0.927765  three
2013-01-05  0.561016 -0.283202 	0.424848 -0.803990   four
2013-01-06  0.205565  1.683160 -0.506140 -0.016024  three

In [44]: df2[df2["E"].isin(["two", "four"])]
Out[44]:
                   A         B         C         D     E
2013-01-03 -0.551129 -0.520855 -0.863102  -0.06489   two
2013-01-05  0.561016 -0.283202 	0.424848  -0.80399   four
```
### Setting
Setting kolom baru secara otomatis menyelaraskan data dengan index:

```python
In [45]: s1 = pd.Series([1, 2, 3, 4, 5, 6], index=pd.date_range("20130102", periods=6))
In [46]: s1
Out[46]:
2013-01-02    1
2013-01-03    2
2013-01-04    3
2013-01-05    4
2013-01-06    5
2013-01-07    6
Freq: D, dtype: int64
In [47]: df["F"] = s1
```
Setting nilai berdasarkan label:

```python
In [48]: df["F"] = df.at[dates[0], "A"] = 0
```
Setting nilai berdasarkan posisi:

```python
In [49]: df.iat[0, 1] = 0
```
Setting dengan assign dengan array NumPy:

```python
In [50]: df.loc[:, "D"] = np.array([5] * len(df))
```
Hasil dari operasi setting:

```python
In [51]: df
Out[51]:
                   A         B         C  D    F
2013-01-01  0.000000  0.000000 	0.454911  5  NaN
2013-01-02  0.305567 -0.253346 	0.120193  5  1.0
2013-01-03 -0.551129 -0.520855 -0.863102  5  2.0
2013-01-04  1.078149 -1.553706 	1.758851  5  3.0
2013-01-05  0.561016 -0.283202 	0.424848  5  4.0
2013-01-06  0.205565  1.683160 -0.506140  5  5.0
```
Operasi `where` dengan setting:

```python
In [52]: df2 = df.copy()
In [53]: df2[df2 > 0] = -df2
In [54]: df2
Out[54]:
                   A         B         C  D    F
2013-01-01  0.000000  0.000000 -0.454911 -5  NaN
2013-01-02 -0.305567 -0.253346 -0.120193 -5 -1.0
2013-01-03 -0.551129 -0.520855 -0.863102 -5 -2.0
2013-01-04 -1.078149 -1.553706 -1.758851 -5 -3.0
2013-01-05 -0.561016 -0.283202 -0.424848 -5 -4.0
2013-01-06 -0.205565 -1.683160 -0.506140 -5 -5.0
```
----------------------
## Missing data
pandas biasanya menggunakan nilai `np.nan` untuk merepresentasikan data yang hilang. Lihat [Missing Data section](https://pandas.pydata.org/pandas-docs/stable/user_guide/missing_data.html#missing-data).

Pengindeksan ulang memungkinkan kita untuk mengubah/menambah/menghapus index pada sumbu (axis) tertentu. Hal ini me-return salinan data:

```python
In [55]: df1 = df.reindex(index=dates[0:4], columns=list(df.columns) + ["E"])
In [56]: df1.loc[dates[0] : dates[1], "E"] = 1
In [57]: df1
Out[57]:
                   A         B         C  D    F    E
2013-01-01  0.000000  0.000000 	0.454911  5  NaN  1.0
2013-01-02  0.305567 -0.253346 	0.120193  5  1.0  1.0
2013-01-03 -0.551129 -0.520855 -0.863102  5  2.0  NaN
2013-01-04  1.078149 -1.553706 	1.758851  5  3.0  NaN
```
Untuk drop setiap baris yang memiliki data hilang:

```python
In [58]: df1.dropna(how="any")
Out[58]: 
                   A         B         C  D    F    E
2013-01-02  0.305567 -0.253346 	0.120193  5  1.0  1.0
```
Mengisi data yang hilang:

```python
In [59]: df1.fillna(value=5)
Out[59]: 
                   A         B         C  D    F    E
2013-01-01  0.000000  0.000000 	0.454911  5  5.0  1.0
2013-01-02  0.305567 -0.253346 	0.120193  5  1.0  1.0
2013-01-03 -0.551129 -0.520855 -0.863102  5  2.0  5.0
2013-01-04  1.078149 -1.553706 	1.758851  5  3.0  5.0
```
Untuk mendapatkan mask boolean dimana nilai adalah `nan`:

```python
In [60]: df1.fillna(value=5)
Out[60]: 
                A      B      C      D      F      E
2013-01-01  False  False  False  False   True  False
2013-01-02  False  False  False  False  False  False
2013-01-03  False  False  False  False  False   True
2013-01-04  False  False  False  False  False   True
```
------------------
## Operations
Lihat [Basic section on Binary Ops](https://pandas.pydata.org/pandas-docs/stable/user_guide/basics.html#basics-binop).

### Stats
Operasi pada umumnya meniadakan data yang hilang.

Melakukan statistika deskriptif:

```python
In [61]: df.mean()
Out[61]: 
A    0.266528
B   -0.154658
C    0.231594
D    5.000000
F    3.000000
dtype: float64
```
Operasi yang sama di sumbu lain:

```python
In [62]: df.mean(1)
Out[62]: 
2013-01-01    1.363728
2013-01-02    1.234483
2013-01-03    1.012983
2013-01-04    1.856659
2013-01-05    1.940533
2013-01-06    2.276517
Freq: D, dtype: float64
```
Beroperasi dengan objek yang memiliki dimensi berbeda dan membutuhkan penyelarasan. Selain itu, pandas secara otomatis mem-broadcast sepanjang dimensi yang telah ditentukan:

```python
In [63]: s = pd.Series([1, 3, 5, np.nan, 6, 8], index=dates).shift(2)
In [64]: s
Out[64]: 
2013-01-01    NaN
2013-01-02    NaN
2013-01-03    1.0
2013-01-04    3.0
2013-01-05    5.0
2013-01-06    NaN
Freq: D, dtype: float64
In [65]: 
df.sub(s, axis="index")
Out[65]: 
                   A         B         C    D    F
2013-01-01       NaN       NaN       NaN  NaN  NaN
2013-01-02       NaN       NaN       NaN  NaN  NaN
2013-01-03 -1.551129 -1.520855 -1.863102  4.0  1.0
2013-01-04 -1.921851 -4.553706 -1.241149  2.0  0.0
2013-01-05 -4.438984 -5.283202 -4.575152  0.0 -1.0
2013-01-06       NaN       NaN       NaN  NaN  NaN
```
### Apply
Aplikasikan fungsi ke data:

```python
In [66]: df.apply(np.cumsum)
Out[66]: 
                   A         B         C   D     F
2013-01-01  0.000000  0.000000 	0.454911   5   NaN
2013-01-02  0.305567 -0.253346 	0.575104  10   1.0
2013-01-03 -0.245562 -0.774201 -0.287998  15   3.0
2013-01-04  0.832587 -2.327907 	1.470853  20   6.0
2013-01-05  1.393603 -2.611109 	1.895702  25  10.0
2013-01-06  1.599167 -0.927949 	1.389562  30  15.0
In [67]: df.apply(lambda x: x.max() - x.min())
Out[67]:
A    1.629277
B    3.236866
C    2.621953
D    0.000000
F    4.000000
dtype: float64
```
### Histogramming
Lihat [Histogramming and Discretization](https://pandas.pydata.org/pandas-docs/stable/user_guide/basics.html#basics-discretization).

```python
In [68]: s = pd.Series(np.random.randint(0, 7, size=10))
In [69]: s
Out[69]: 
0    2
1    2
2    6
3    3
4    5
5    2
6    6
7    2
8    0
9    4
dtype: int64
In [70]: s.value_counts()
Out[70]: 
2    4
6    2
3    1
5    1
0    1
4    1
dtype: int64
```
### String Methods
Series dilengkapi dengan sekumpulan metode pemrosesan string di dalam atribut str yang memudahkan pengoperasian pada setiap elemen array, seperti pada _code snippet_ di bawah ini.

```python
In [71]: s = pd.Series(["A", "B", "C", "Aaba", "Baca", np.nan, "CABA", "dog", "cat"])
In [72]: s.str.lower()
Out[72]: 
0       a
1       b
2       c
3    aaba
4    baca
5     NaN
6    caba
7     dog
8     cat
dtype: object
```
----------------------------

## Merge

### Concat
pandas menyediakan berbagai fasilitas untuk menggabungkan objek Series dan DataFrame dengan berbagai jenis kumpulan logika untuk index dan fungsionalitas algebra relasional dalam kasus operasi  join/merge.

Lihat [Merging section](https://pandas.pydata.org/pandas-docs/stable/user_guide/merging.html#merging).

Menggabungkan bersama objek pandas dengan [concat()](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.concat.html#pandas.concat):

```python
In [73]: df = pd.DataFrame(np.random.randn(10, 4))
In [74]: df
Out[74]: 
          0         1         2         3
0 -0.952487  1.463192  0.065861 -1.555810
1  0.359440  1.088316 -2.275407 -0.243351
2 -2.435107  0.380202  0.395161  0.274759
3  0.788873 -0.470499 -1.384486  0.501539
4  0.241833 -0.880214 -0.197484 -0.370016
5 -0.290795 -0.513898  0.524612 -0.211213
6  0.256962 -1.604652  2.047245 -0.874247
7 -0.418789 -1.707659  1.232011 -0.710965
8 -0.079478  1.010566 -0.593022  0.004146
9  1.520088  1.932204 -0.865877 -0.434346
In [75]: pieces = [df[:3], df[3:7], df[7:]]
In [76]: pd.concat(pieces)
Out[76]: 
          0         1         2         3
0 -0.952487  1.463192  0.065861 -1.555810
1  0.359440  1.088316 -2.275407 -0.243351
2 -2.435107  0.380202  0.395161  0.274759
3  0.788873 -0.470499 -1.384486  0.501539
4  0.241833 -0.880214 -0.197484 -0.370016
5 -0.290795 -0.513898  0.524612 -0.211213
6  0.256962 -1.604652  2.047245 -0.874247
7 -0.418789 -1.707659  1.232011 -0.710965
8 -0.079478  1.010566 -0.593022  0.004146
9  1.520088  1.932204 -0.865877 -0.434346
```
### Join
Merge dengan style SQL. Lihat [Database style joining](https://pandas.pydata.org/pandas-docs/stable/user_guide/merging.html#merging-join).

```python
In [77]: left = pd.DataFrame({"key": ["foo", "foo"], "lval": [1, 2]})
In [78]: right = pd.DataFrame({"key": ["foo", "foo"], "rval": [4, 5]})
In [79]: left
Out[79]:
   key  lval
0  foo     1
1  foo     2
In [80]: right
Out[80]:
   key  rval
0  foo     4
1  foo     5
In [81]: pd.merge(left, right, on="key")
Out[81]:
   key  lval  rval
0  foo     1     4
1  foo     1     5
2  foo     2     4
3  foo     2     5
```
Contoh lain:

```python
In [82]: left = pd.DataFrame({"key": ["foo", "bar"], "lval": [1, 2]})
In [83]: right = pd.DataFrame({"key": ["foo", "bar"], "rval": [4, 5]})
In [84]: left
Out[84]:
   key  lval
0  foo     1
1  bar     2
In [85]: right
Out[85]:    
   key  rval
0  foo     4
1  bar     5
In [86]: pd.merge(left, right, on="key")
Out[86]:
   key  lval  rval
0  foo     1     4
1  bar     2     5
```
--------------------------

## Grouping
Dengan "group by" kita merujuk ke suatu proses yang melibatkan satu atau lebih langkah berikut:
- Memisahkan data ke dalam beberapa grup berdasarkan kriteria
- Mengaplikasikan fungsi ke setiap grup secara independen
- Mengombinasikan hasil ke dalam sebuah struktur data

Lihat [Grouping section](https://pandas.pydata.org/pandas-docs/stable/user_guide/groupby.html#groupby).

```python
In [87]: df = pd.DataFrame(
             {
                 "A": ["foo", "bar", "foo", "bar", "foo", "bar", "foo", "foo"],
                 "B": ["one", "one", "two", "three", "two", "two", "one", "three"],
                 "C": np.random.randn(8),
                 "D": np.random.randn(8),
             }
         )
In [88]: df
Out[88]:
     A      B         C         D
0  foo    one -2.390963  0.145885
1  bar    one  1.591024  0.303847
2  foo    two  2.512224  0.870698
3  bar  three  2.194096  1.412758
4  foo    two  0.051612  0.725426
5  bar    two  0.060363 -0.964399
6  foo    one  2.089645 -0.609173
7  foo  three  1.133125  0.413771
```
Grouping dan mengaplikasikan fungsi [sum()](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.core.groupby.GroupBy.sum.html#pandas.core.groupby.GroupBy.sum) pada grup yang dihasilkan:

```python
In [89]: df.groupby("A").sum()
Out[89]:
            C         D
A                      
bar  3.845483  0.752206
foo  3.395644  1.546608
```
Grouping dengan beberapa kolom akan membentuk index hierarkis, kemudian kita dapat mengaplikasikan fungsi `sum()`:

```python
In [90]: df.groupby(["A", "B"]).sum()
Out[90]:
                  C         D
A   B                        
bar one    1.591024  0.303847
    three  2.194096  1.412758
    two    0.060363 -0.964399
foo one   -0.301317 -0.463288
    three  1.133125  0.413771
    two    2.563836  1.596124
```
-------------------------

## Reshaping
Lihat [Hierarchical Indexing](https://pandas.pydata.org/pandas-docs/stable/user_guide/advanced.html#advanced-hierarchical) dan [Reshaping](https://pandas.pydata.org/pandas-docs/stable/user_guide/reshaping.html#reshaping-stacking).

### Stack

```python
In [91]: tuples = list(
             zip(
                *[
                    ["bar", "bar", "baz", "baz", "foo", "foo", "qux", "qux"],
                    ["one", "two", "one", "two", "one", "two", "one", "two"],
                ]
             )
         )
In [92]: index = pd.MultiIndex.from_tuples(tuples, names=["first", "second"])
In [93]: df = pd.DataFrame(np.random.randn(8, 2), index=index, columns=["A", "B"])
In [94]: df2 = df[:4]
In [95]: df2
Out[95]: 
                     A         B
first second                    
bar   one    -1.142374 	0.033097
      two    -0.977299 -0.974997
baz   one     1.439461 -0.783570
      two     0.625465 -1.343182
```
Method [stack()](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.stack.html#pandas.DataFrame.stack) meng-kompres level di kolom DataFrame:

```python
In [96]: stacked = df2.stack()
In [97]: stacked
Out[97]:
first  second   
bar    one     A   -1.142374
               B    0.033097
       two     A   -0.977299
               B   -0.974997
baz    one     A    1.439461
               B   -0.783570
       two     A    0.625465
               B   -1.343182
dtype: float64
```
Dengan DataFrame atau Series yang "stacked", operasi invers dari [stack()](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.stack.html#pandas.DataFrame.stack) adalah [unstack()](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.unstack.html#pandas.DataFrame.unstack), yang secara default meng-unstack level terakhir:

```python
In [98]: stacked.unstack()
Out[98]:
                     A         B
first second                    
bar   one    -1.142374 	0.033097
      two    -0.977299 -0.974997
baz   one     1.439461 -0.783570
      two     0.625465 -1.343182
In [99]: stacked.unstack(1)
Out[99]:
second        one       two
first                      
bar   A -1.142374 -0.977299
      B  0.033097 -0.974997
baz   A  1.439461  0.625465
      B -0.783570 -1.343182
In [100]: stacked.unstack(0)
Out[100]:
first          bar       baz
second                      
one    A -1.142374  1.439461
       B  0.033097 -0.783570
two    A -0.977299  0.625465
       B -0.974997 -1.343182
```
### Pivot tables
Lihat [Pivot Tables](https://pandas.pydata.org/pandas-docs/stable/user_guide/reshaping.html#reshaping-pivot).

```python
In [101]: df = pd.DataFrame(
              {
                  "A": ["one", "one", "two", "three"] * 3,
                  "B": ["A", "B", "C"] * 4,
                  "C": ["foo", "foo", "foo", "bar", "bar", "bar"] * 2,
                  "D": np.random.randn(12),
                  "E": np.random.randn(12),
              }         
          )
In [102]: df
Out[102]:
        A  B    C         D         E
0     one  A  foo -0.598984 -0.594010
1     one  B  foo -1.300673 -1.366121
2     two  C  foo  0.255607  0.678857
3   three  A  bar  1.435882 -0.522729
4     one  B  bar -0.905124 -0.910712
5     one  C  bar  1.311140 -0.447966
6     two  A  foo  0.120023  0.017960
7   three  B  foo -0.657025  0.723071
8     one  C  foo -0.118258 -0.902809
9     one  A  bar -0.529557  2.269417
10    two  B  bar -0.696235 -0.784247
11  three  C  bar -0.759735 -1.652989
```
Kita bisa membuat tabel pivot dari data berikut dengan sangat mudah:

```python
In [103]: pd.pivot_table(df, values="D", index=["A", "B"], columns=["C"])
Out[103]: 
C             bar       foo
A     B                    
one   A -0.529557 -0.598984
      B -0.905124 -1.300673
      C 1.311140  -0.118258
three A 1.435882 	NaN
      B       NaN -0.657025
      C -0.759735       NaN
two   A       NaN  0.120023
      B -0.696235       NaN
      C       NaN  0.255607
```
---------------------------

## Time series
pandas memiliki fungsionalitas yang sederhana, kuat, dan efisien untuk melakukan operasi _resampling_ pada saat konversi frekuensi. Lihat [Time Series section](https://pandas.pydata.org/pandas-docs/stable/user_guide/timeseries.html#timeseries).

```python
In [104]: rng = pd.date_range("1/1/2012", periods=100, freq="S")
In [105]: ts = pd.Series(np.random.randint(0, 500, len(rng)), index=rng)
In [106]: ts.resample("5Min").sum()
Out[106]: 
2012-01-01    24421
Freq: 5T, dtype: int64
```
Representasi zona waktu:

```python
In [107]: rng = pd.date_range("3/6/2012 00:00", periods=5, freq="D")
In [108]: ts = pd.Series(np.random.randn(len(rng)), rng)
In [109]: ts
Out[109]:
2012-03-06    0.103946
2012-03-07    1.252289
2012-03-08   -1.572998
2012-03-09    1.255516
2012-03-10    1.500832
Freq: D, dtype: float64
In [110]: ts_utc = ts.tz_localize("UTC")
In [111]: ts_utc
Out[111]: 
2012-03-06 00:00:00+00:00    0.103946
2012-03-07 00:00:00+00:00    1.252289
2012-03-08 00:00:00+00:00   -1.572998
2012-03-09 00:00:00+00:00    1.255516
2012-03-10 00:00:00+00:00    1.500832
Freq: D, dtype: float64
```
Konversi ke zona waktu lain:

```python
In [112]: ts_utc.tz_convert("US/Eastern")
Out[112]:
2012-03-05 19:00:00-05:00    0.103946
2012-03-06 19:00:00-05:00    1.252289
2012-03-07 19:00:00-05:00   -1.572998
2012-03-08 19:00:00-05:00    1.255516
2012-03-09 19:00:00-05:00    1.500832
Freq: D, dtype: float64
```
Mengonversi antara representasi rentang waktu:

```python
In [113]: rng = pd.date_range("1/1/2012", periods=5, freq="M")
In [114]: ts = pd.Series(np.random.randn(len(rng)), index=rng)
In [115]: ts
Out[115]:
2012-01-31   -0.041130
2012-02-29   -0.314052
2012-03-31   -0.416373
2012-04-30    0.395892
2012-05-31    0.020294
Freq: M, dtype: float64
In [116]: ps = ts.to_period()
In [117]: ps
Out[117]:
2012-01   -0.041130
2012-02   -0.314052
2012-03   -0.416373
2012-04    0.395892
2012-05    0.020294
Freq: M, dtype: float64
In [118]: ps.to_timestamp()
Out[118]:
2012-01-01   -0.041130
2012-02-01   -0.314052
2012-03-01   -0.416373
2012-04-01    0.395892
2012-05-01    0.020294
Freq: MS, dtype: float64
```
Konversi di antara periode dan timestamp memungkinkan beberapa fungsi aritmatika untuk digunakan. Di contoh berikut, kita mengonversi frekuensi triwulanan dengan tahun yang berakhir pada November menjadi 9am pada akhir bulan setelah akhir _quarter_:

```python
In [119]: prng = pd.period_range("1990Q1", "2000Q4", freq="Q-NOV")
In [120]: ts = pd.Series(np.random.randn(len(prng)), prng)
In [121]: ts.index = (prng.asfreq("M", "e") + 1).asfreq("H", "s") + 9
In [122]: ts.head()
Out[122]:
1990-03-01 09:00   -0.259463
1990-06-01 09:00    0.750457
1990-09-01 09:00   -0.920544
1990-12-01 09:00   -0.397596
1991-03-01 09:00    0.224153
Freq: H, dtype: float64
```
------------------

## Categoricals
pandas bisa berisi data categorical di dalam DataFrame.

```python
In [123]: df = pd.DataFrame(
              {"id": [1, 2, 3, 4, 5, 6], "raw_grade": ["a", "b", "b", "a", "a", "e"]}
          )
```
Mengonversi grade raw ke tipe data categorical:

```python
In [124]: df["grade"] = df["raw_grade"].astype("category")
In [125]: df["grade"]
Out[125]:
0    a
1    b
2    b
3    a
4    a
5    e
Name: grade, dtype: category
Categories (3, object): ['a', 'b', 'e']
```
Rename kategori menjadi nama yang lebih memiliki makna:

```python
In [126]: df["grade"].cat.categories = ["very good", "good", "very bad"]
```
Urutkan ulang kategori dan secara bersamaan tambahkan kategori yang hilang:

```python
In [127]: df["grade"] = df["grade"].cat.set_categories(
              ["very bad", "bad", "medium", "good", "very good"]
          )
In [128]: df["grade"]
Out[128]: 
0    very good
1         good
2         good
3    very good
4    very good
5     very bad
Name: grade, dtype: category
Categories (5, object): ['very bad', 'bad', 'medium', 'good', 'very good']
```
Sorting adalah per order dalam kategori, bukan order secara leksikal:

```python
In [129]: df.sort_values(by="grade")
Out[129]:
   id raw_grade      grade
5   6         e   very bad
1   2         b       good
2   3         b       good
0   1         a  very good
3   4         a  very good
4   5         a  very good
```
Grouping menurut kolom categorical juga menampilkan kategori empty (kosong):

```python
In [130]: df.groupby("grade").size()
Out[130]:
grade
very bad     1
bad          0
medium       0
good         2
very good    3
dtype: int64
```
----------------------

## Plotting
Kita menggunakan konvensi standar untuk merujuk ke API matplotlib:

```python
In [131]: import matplotlib.pyplot as plt
In [132]: plt.close("all")
```
method `close()` digunakan untuk menutup window figur:

```python
In [133]: ts = pd.Series(np.random.randn(1000), index=pd.date_range("1/1/2000", periods=1000))
In [134]: ts = ts.cumsum()
In [135]: ts.plot();
```
Jika menjalankan dengan Jupyter Notebook, plot akan muncul di `plot()`.

```python
In [136]: plt.show();
```
Pada DataFrame, method `plot()` baik digunakan untuk mem-plot semua kolom dengan label:

```python
In [137]: df = pd.DataFrame(
              np.random.randn(1000, 4), index=ts.index, columns=["A", "B", "C", "D"]
          )
In [138]: df = df.cumsum()
In [139]: plt.figure();
In [140]: df.plot();
In [141]: plt.legend(loc='best');
```
-------------------------

## Getting data in/out

### CSV
Mebuat file csv:

```python
In [142]: df.to_csv("foo.csv")
```
Membaca file csv:

```python
In [143]: pd.read_csv("foo.csv")
Out[143]: 
     Unnamed: 0          A          B          C          D
0    2000-01-01   0.350262   0.843315   1.798556   0.782234
1    2000-01-02  -0.586873   0.034907   1.923792  -0.562651
2    2000-01-03  -1.245477  -0.963406   2.269575  -1.612566
3    2000-01-04  -0.252830  -0.498066   3.176886  -1.275581
4    2000-01-05  -1.044057   0.118042   2.768571   0.386039
..          ...        ...        ...        ...        ...
995  2002-09-22 -48.017654  31.474551  69.146374 -47.541670
996  2002-09-23 -47.207912  32.627390  68.505254 -48.828331
997  2002-09-24 -48.907133  31.990402  67.310924 -49.391051
998  2002-09-25 -50.146062  33.716770  67.717434 -49.037577
999  2002-09-26 -49.724318  33.479952  68.108014 -48.822030

[1000 rows x 5 columns]
```
### HDF5
Membuat HDF5 Store:

```python
In [144]: df.to_hdf("foo.h5", "df")
```
Membaca HDF5 Store:

```python
In [145]: pd.read_hdf("foo.h5", "df")
Out[145]: 
                    A          B          C          D
2000-01-01   0.350262   0.843315   1.798556   0.782234
2000-01-02  -0.586873   0.034907   1.923792  -0.562651
2000-01-03  -1.245477  -0.963406   2.269575  -1.612566
2000-01-04  -0.252830  -0.498066   3.176886  -1.275581
2000-01-05  -1.044057   0.118042   2.768571   0.386039
...               ...        ...        ...        ...
2002-09-22 -48.017654  31.474551  69.146374 -47.541670
2002-09-23 -47.207912  32.627390  68.505254 -48.828331
2002-09-24 -48.907133  31.990402  67.310924 -49.391051
2002-09-25 -50.146062  33.716770  67.717434 -49.037577
2002-09-26 -49.724318  33.479952  68.108014 -48.822030

[1000 rows x 4 columns]
```
### Excel
Membuat file excel:

```python
In [146]: df.to_excel("foo.xlsx", sheet_name="Sheet1")
```
Membaca file excel:

```python
In [147]: pd.read_excel("foo.xlsx", "Sheet1", index_col=None, na_values=["NA"])
Out[147]: 
    Unnamed: 0          A          B          C          D
0   2000-01-01   0.350262   0.843315   1.798556   0.782234
1   2000-01-02  -0.586873   0.034907   1.923792  -0.562651
2   2000-01-03  -1.245477  -0.963406   2.269575  -1.612566
3   2000-01-04  -0.252830  -0.498066   3.176886  -1.275581
4   2000-01-05  -1.044057   0.118042   2.768571   0.386039
..         ...        ...        ...        ...        ...
995 2002-09-22 -48.017654  31.474551  69.146374 -47.541670
996 2002-09-23 -47.207912  32.627390  68.505254 -48.828331
997 2002-09-24 -48.907133  31.990402  67.310924 -49.391051
998 2002-09-25 -50.146062  33.716770  67.717434 -49.037577
999 2002-09-26 -49.724318  33.479952  68.108014 -48.822030

[1000 rows x 5 columns]
```
--------------------------
## Gotchas
Jika kita mencoba untuk melakukan operasi kita bisa menemukan exception seperti ini:

```python
>>> if pd.Series([False, True, False]):

...    print("I was true")
Traceback
    ...
ValueError: The truth value of an array is ambiguous. Use a.empty, a.any() or a.all().
```
---------------------------
# 5 Fungsi / Perintah di pandas:

1. `head()` merupakan fungsi pandas yang berguna untuk menampilkan data paling awal atau bisa disebut dengan data paling atas pada suatu DataFrame. Secara default, fungsi ini akan menampilkan 5 baris paling atas jika argumen tidak diisi. Dengan kata lain, kita bisa mengisi argumen dengan angka berapapun untuk menampilkan data teratas sesuai jumlah angka pada argumen yang telah kita ttentukan.
<br>

2. `tail()` bisa dibilang merupakan kebalikan dari fungsi `head()`. Funsi `tail()` ini berguna untuk menampilkan data paling bawah pada suatu DataFrame. Sama dengan `head()`, nilai default dari `tail()` adalah 5.
<br>

3. `info()` adalah fungsi pandas yang digunakan untuk memberi tahu dan menampilkan berbagai informasi detail tentang DataFrame seperti RangeIndex, total kolom, nama-nama kolom, dtypes, memory usage, dan lain-lain.
<br>

4. `mean()` adalah fungsi pandas yang berguna untuk menghitung nilai rata-rata dari kolom berisi data numerik.
<br>

5. `shape` merupakan fungsi yang digunakan untuk menampilkan dimensi (rows, columns) dari suatu DataFrame.