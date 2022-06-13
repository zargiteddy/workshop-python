# Pengenalan machine learning dengan scikit-learn

Pada minggu ini, kita mempelajari kosakata [machine learning](https://en.wikipedia.org/wiki/Machine_learning) yang kita gunakan dalam scikit-learn dan juga mengerjakan beberapa contoh _learning_ sederhana.

Sebelum memulai, kita install scikit-learn terlebih dahulu:

```python
(workshop) zargiteddy@shield:~$ conda install -c anaconda scikit-learn
Collecting package metadata (current_repodata.json): done
Solving environment: failed with initial frozen solve. Retrying with flexible solve.
Solving environment: failed with repodata from current_repodata.json, will retry with next repodata source.
Collecting package metadata (repodata.json): done
Solving environment: done


==> WARNING: A newer version of conda exists. <==
  current version: 4.12.0
  latest version: 4.13.0

Please update conda by running

    $ conda update -n base -c defaults conda



## Package Plan ##

  environment location: /home/zargiteddy/miniconda3/envs/workshop

  added / updated specs:
    - scikit-learn


The following packages will be downloaded:

    package                    |            build
    ---------------------------|-----------------
    certifi-2021.5.30          |  py310h06a4308_0         152 KB  anaconda
    joblib-1.1.0               |     pyhd3eb1b0_0         211 KB  anaconda
    scikit-learn-1.0.1         |  py310h00e6091_0        20.9 MB  anaconda
    scipy-1.7.3                |  py310hfa59a62_0        59.5 MB  anaconda
    threadpoolctl-2.2.0        |     pyh0d69192_0          16 KB  anaconda
    ------------------------------------------------------------
                                           Total:        80.7 MB

The following NEW packages will be INSTALLED:

  joblib             anaconda/noarch::joblib-1.1.0-pyhd3eb1b0_0
  scikit-learn       anaconda/linux-64::scikit-learn-1.0.1-py310h00e6091_0
  scipy              anaconda/linux-64::scipy-1.7.3-py310hfa59a62_0
  threadpoolctl      anaconda/noarch::threadpoolctl-2.2.0-pyh0d69192_0

The following packages will be UPDATED:

  certifi            anaconda/noarch::certifi-2020.6.20-py~ --> anaconda/linux-64::certifi-2021.5.30-py310h06a4308_0


Proceed ([y]/n)? y


Downloading and Extracting Packages
certifi-2021.5.30    | 152 KB    | ##################################### | 100% 
joblib-1.1.0         | 211 KB    | ##################################### | 100% 
threadpoolctl-2.2.0  | 16 KB     | ##################################### | 100% 
scipy-1.7.3          | 59.5 MB   | ##################################### | 100% 
scikit-learn-1.0.1   | 20.9 MB   | ##################################### | 100% 
Preparing transaction: done
Verifying transaction: done
Executing transaction: | 

    Installed package of scikit-learn can be accelerated using scikit-learn-intelex.
    More details are available here: https://intel.github.io/scikit-learn-intelex

    For example:

        $ conda install scikit-learn-intelex
        $ python -m sklearnex my_application.py

    

done
```

----------------------

## Machine learning: the problem setting

Pada umumnya, masalah _learning_ mempertimbangkan kumpulan sample n data lalu mencoba untuk memprediksi properti dari data yang tidak diketahui. Jika setiap sample lebih dari satu angka dan berupa entry multi-dimensional, maka bisa dianggap memiliki beberapa atribut atau fitur.

Permasalahan dalam _learning_ bisa dikelompokkan menjadi beberapa kategori:

* [supervised learning](https://en.wikipedia.org/wiki/Supervised_learning), dimana data datang dengan atribut tambahan yang kita ingin prediksi. Permasalahan ini bisa berupa:
    * [klasifikasi](https://en.wikipedia.org/wiki/Statistical_classification): sample adalah milik dua atau lebih kelas dan kita ingin mempelajari data yang telah dilabel untuk mengetahui bagaimana cara memprediksi kelas dari data yang tidak dilabel. Contoh dari masalah klasifikasi adalah pengenalan digit tulisan tangan, yang tujuannya adalah untuk menempatkan setiap vektor input ke salah satu kategori diskrit. Cara lain untuk mengenali klaifikasi adalah sebagai bentuk diskrit dari _supervised-learning_ dimana klasifikasi memiliki jumlah kategori yang terbatas dan untuk setiap sample n yang disediakan, salah satunya akan mencoba untuk melabeli dengan kategori dan kelas yang benar.
    * [regresi](https://en.wikipedia.org/wiki/Regression_analysis): jika output yang diinginkan memiliki satu atau lebih variabel _continous_, maka tugas tersebut bisa kita panggil dengan nama _regresi_. Salah satu contoh masalah regresi adalah prediksi panjang salmon sebagai fungsi dari umur dan beratnya.

* [unsupervised learning](https://en.wikipedia.org/wiki/Unsupervised_learning), dimana data latih memiliki kumpulan vektor input x tanpa nilai target yang sesuai. Tujuannya adalah mencari kelompok berisi contoh-contoh yang mirip di dalam data, yang dinamai [clustering](https://en.wikipedia.org/wiki/Cluster_analysis), atau untuk menentukan distribusi data di dalam ruang input, yang dikenal dengan [density estimation](https://en.wikipedia.org/wiki/Density_estimation), atau untuk memproyeksikan data dari ruang berdimensi tinggi ke dalam dua atau tiga dimensi untuk visualisasi.

> **Training set dan testing set**
Machine learning adalah segala sesuatu tentang mempelajari beberapa properti dataset dan menguji properti tersebut pada dataset lain. Praktik yang biasanya dilakukan di dalam machine learning adalah mengevaluasi algoritma dengan memisah dataset menjadi dua. Kita sebut salah satu dari dataset yang dipisah tersebut dengan nama **training set** dimana kita mempelajari beberapa properti, dan dataset satunya yang kita panggil dengan nama **testing set** dimana kita menguji properti yang sudah dipelajari.

----------------------

## Loading an example dataset

`scikit learn` memiliki beberapa dataset standar, contohnya adalah dataset [iris](https://en.wikipedia.org/wiki/Iris_flower_data_set) dan [digits](https://archive.ics.uci.edu/ml/datasets/Pen-Based+Recognition+of+Handwritten+Digits) untuk klasifikasi dan [dataset diabetes](https://www4.stat.ncsu.edu/~boos/var.select/diabetes.html) untuk regresi.

Pada contoh di bawah, kita menggunakan Jupyter Notebook untuk memuat dataset `iris` dan `digits`.

```python
In [1]: from sklearn import datasets
        iris = datasets.load_iris()
        digits = datasets.load_digits()
```
Dataset adalah objek yang mirip dictionary yang berisi semua data dan beberapa metadata tentang data tersebut. Data tersebut disimpan di dalam member `.data`, yang merupakan `n_samples`, array `n_features`. Di dalam kasus masalah _supervised_, satu atau lebih variabel respon disimpan di dalam member `.target`. Detail informasi tentang dataset yang berbeda bisa dilihat di [dedicated section](https://scikit-learn.org/stable/datasets.html#datasets).

Misalnya, dalam kasus dataset digits, `digits.data` memberikan akses ke fitur yang bisa digunakan untuk mengklasifikasi sample digit:

```python
In [2]: print(digits.data)
        [[ 0.  0.  5. ...  0.  0.  0.]
         [ 0.  0.  0. ... 10.  0.  0.]
         [ 0.  0.  0. ... 16.  9.  0.]
        ...
         [ 0.  0.  1. ...  6.  0.  0.]
         [ 0.  0.  2. ... 12.  0.  0.]
         [ 0.  0. 10. ... 12.  1.  0.]]
```
`digits.target` memberikan _ground truth_ untuk dataset digit, yaitu angka yang sesuai dengan setiap gambar digit yang kita coba pelajari:

```python
In [3]: digits.target
Out[3]: array([0, 1, 2, ..., 8, 9, 8])
```
**Shape array data**
Data selalu berbentuk array 2D, yaitu shape (`n_samples`, `n_features`), walaupun data asli mungkin memiliki shape yang berbeda. Pada kasus digit ini, setiap sample original adalah gambar shape (8, 8) dan bisa diakses menggunakan:

```python
In [4]: digits.images[0]
Out[4]: 
array([[ 0.,  0.,  5., 13.,  9.,  1.,  0.,  0.],
       [ 0.,  0., 13., 15., 10., 15.,  5.,  0.],
       [ 0.,  3., 15.,  2.,  0., 11.,  8.,  0.],
       [ 0.,  4., 12.,  0.,  0.,  8.,  8.,  0.],
       [ 0.,  5.,  8.,  0.,  0.,  9.,  8.,  0.],
       [ 0.,  4., 11.,  0.,  1., 12.,  7.,  0.],
       [ 0.,  2., 14.,  5., 10., 12.,  0.,  0.],
       [ 0.,  0.,  6., 13., 10.,  0.,  0.,  0.]])
```
--------------------

## Learning and predicting

Pada kasus dataset digits, tugasnya adalah untuk memprediksi digit mana yang direpresentasikan oleh sebuah _image_. Kita diberikan sample berupa setiap 10 kelas yang memungkinkan (digit nol sampai sembilan) dimana kita menggunakan [estimator](https://en.wikipedia.org/wiki/Estimator) supaya bisa memprediksi kelas yang menjadi milik sampel yang tidak terlihat.

Di scikit-learn, _estimator_ untuk klasifikasi adalah objek Python yang mengimplementasikan method `fit(X, y)` dan `predict(T)`.

Contoh estimator adalah kelas `sklearn.svm.SVC`, yang mengimplementasikan [klasifikasi support vector](https://en.wikipedia.org/wiki/Support-vector_machine). Konstruktor estimator mengambil sebagai argumen parameter model.

Untuk saat ini, kita anggap estimator sebagai _black box_:

```python
In [5]: from sklearn import svm
        clf = svm.SVC(gamma=0.001, C=100.)
```
instance estimator `clf` (untuk classifier) adalah yang pertama dipasang ke dalam model yang harus _learn_ dari model. Hal ini dilakukan dengan memasukkan training set kita ke dalam method `fit`. Untuk training set, kita menggunakan semua gambar dari dataset kita kecuali gambar terakhir, yang akan kita simpan untuk prediksi nanti. Kita pilih training set dengan sintaks Python `[:-1]`, yang menciptakan array yang berisi semua item (kecuali item terakhir) dari `digits.data`:

```python
In [6]: clf.fit(digits.data[:-1], digits.target[:-1])
Out[6]: SVC(C=100.0, gamma=0.001)
```
Sekarang kita bisa memprediksi nilai baru. Pada kasus ini, kita akan memprediksi menggunakan gambar terakhir dari `digits.data`. Dengan memprediksi, kita akan menentukan gambar dari training set yang paling cocok dengan gambar terakhir.

```python
In [7]: clf.predict(digits.data[-1:])
Out[7]: array([8])
```
--------------------

## Conventions
Estimator scikit-learn mengikuti aturan tertentu untuk membuat "perilaku" menjadi lebih prediktif. Hal ini dijelaskan di [Glossary of Common Terms and API Elements](https://scikit-learn.org/stable/glossary.html#glossary).

### Type casting
Jika tidak ditentukan, input akan default `float64`.

```python
In [8]: import numpy as np
        from sklearn import kernel_approximation

In [9]: rng = np.random.RandomState(0)
        X = rng.rand(10, 2000)
        X = np.array(X, dtype='float32')
        X.dtype
Out[9]: dtype('float32')

In [10]: transformer = kernel_approximation.RBFSampler()
         X_new = transformer.fit_transform(X)
         X_new.dtype
Out[10]: dtype('float64')
```
Pada contoh tersebut, `X` adalah `float32`, yang dilempar ke `float64` dengan `fit_transform(X)`.

Target regresi dilempar ke `float64` dan target klasifikasi dipertahankan:

```python
In [11]: from sklearn import datasets
         from sklearn.svm import SVC
         iris = datasets.load_iris()
         clf = SVC()
         clf.fit(iris.data, iris.target)
Out[11]: SVC()

In [12]: list(clf.predict(iris.data[:3]))
Out[12]: [0, 0, 0]

In [13]: clf.fit(iris.data, iris.target_names[iris.target])
Out[13]: SVC()

In [14]: list(clf.predict(iris.data[:3]))
Out[14]: ['setosa', 'setosa', 'setosa']
```
Pada contoh tersebut, `predict()` me-return array integer, karena `iris.target` (array integer) digunakan di `fit`. Lalu `predict()` kedua me-return array string, karena `iris.target_names` digunakan untuk _fitting_.

### Refitting and updating parameters
Hyper-parameter pada estimator bisa di-update setelah dikonstruksi via method [set_params()](https://scikit-learn.org/stable/glossary.html#term-set_params). Memanggil `fit()` lebih dari sekali akan meng-overwrite yang sudah dipelajari oleh `fit()` sebelumnya:

```python
In [15]: import numpy as np
         from sklearn.datasets import load_iris
         from sklearn.svm import SVC
         X, y = load_iris(return_X_y=True)
In [16]: clf = SVC()
         clf.set_params(kernel='linear').fit(X, y)
Out[16]: SVC(kernel='linear')
In [17]: clf.predict(X[:5])
Out[17]: array([0, 0, 0, 0, 0])
In [18]: clf.set_params(kernel='rbf').fit(X, y)
Out[18]: SVC()
In [19]: clf.predict(X[:5])
Out[19]: array([0, 0, 0, 0, 0])
```
Pada kode tersebut, kernel default adalah `rbf` pertama-tama diganti menjadi `linear` via [SVC.set_params()](https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html#sklearn.svm.SVC.set_params) setelah estimator dibentuk, dan berubah lagi menjadi `rbf` untuk fit kembali estimator dan melakukan prediksi kedua.

### Multiclass vs. multilabel fitting
Ketika menggunakan [multiclass classifiers](https://scikit-learn.org/stable/modules/classes.html#module-sklearn.multiclass), tugas learning dan prediksi yang dibentuk bergantung kepada format yang fit dengan data target:

```python
In [20]: from sklearn.svm import SVC
         from sklearn.multiclass import OneVsRestClassifier
         from sklearn.preprocessing import LabelBinarizer
In [21]: X = [[1, 2], [2, 4], [4, 5], [3, 2], [3, 1]]
         y = [0, 0, 1, 1, 2]
In [22]: classif = OneVsRestClassifier(estimator=SVC(random_state=0))
         classif.fit(X, y).predict(X)
Out[22]: array([0, 0, 1, 1, 2])
```
Pada kasus di atas, classifier fit pada array 1d label multiclass dan maka dari itu method `predict()` menyediakan prediksi multiclass yang sesuai. Ada juga kemungkinan untuk fit pada array 2d indikator label biner:

```python
In [23]: y = LabelBinarizer().fit_transform(y)
         classif.fit(X, y).predict(X)
Out[23]: array([[1, 0, 0],
                [1, 0, 0],
                [0, 1, 0],
                [0, 0, 0],
                [0, 0, 0]])
```
Pada kode tersebut, classifier `fit()` pada representasi label biner 2d untuk y, menggunakan [LabelBinarizer](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.LabelBinarizer.html#sklearn.preprocessing.LabelBinarizer). Pada kasus tersebut `predict()` me-return array 2d yang merepresentasikan prediksi multilabel yang sesuai.

Perhatikan bahwa instance keempat dan kelimat me-return semua nilai nol, mengindikasikan bahwa kedua instance tersebut tidak fit dengan ketiga label. Dengan output multilabel, memungkinkan sebuah intance untuk diberi label:

```python
In [24]: from sklearn.preprocessing import MultiLabelBinarizer
         y = [[0, 1], [0, 2], [1, 3], [0, 2, 3], [2, 4]]
         y = MultiLabelBinarizer().fit_transform(y)
         classif.fit(X, y).predict(X)
Out[24]: array([[1, 1, 0, 0, 0],
                [1, 0, 1, 0, 0],
                [0, 1, 0, 1, 0],
                [1, 0, 1, 0, 0],
                [1, 0, 1, 0, 0])
```
Pada kasus tersebut, classifier `fit` pada instance yang masing-masing diberi beberapa label. [MultiLabelBinarizer](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.MultiLabelBinarizer.html#sklearn.preprocessing.MultiLabelBinarizer) digunakan untuk binarisasi array 2d multilabel untuk `fit`. Sebagai hasilnya, `predict()` me-return array 2d dengan beberapa label yang telah diprediksi untuk setiap instance.

----------------------

#### Thank You.



