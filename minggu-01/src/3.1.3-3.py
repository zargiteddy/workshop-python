letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(letters)
# mengganti beberapa nilai
letters[2:5] = ['C', 'D', 'E']
print(letters)
# menghilangkan nilai
letters[2:5] = []
print(letters)
# hapus list dengan mengganti semua elemen dengan empty list
letters[:] = []
print(letters)

letters = ['a', 'b', 'c', 'd']
print(len(letters))