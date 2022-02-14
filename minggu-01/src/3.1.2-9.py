word = 'Python'
print(word[0])
print(word[5])

print(word[-1])
print(word[-2])
print(word[-6])

print(word[0:2])  # karakter dari posisi 0 (included) sampai 2 (excluded)
print(word[2:5])  # karakter dari posisi 2 (included) sampai 5 (excluded)

print(word[:2])   # karakter dari awal sampai posisi 2 (excluded)
print(word[4:])   # karakter dari posisi 4 (included) sampai akhir
print(word[-2:])  # karakter kedua dari akhir (included) sampai akhir karakter)

print(word[:2] + word[2:])
print(word[:4] + word[4:])

#---- bagian error ----#
# hilangkan tanda '#' disamping kiri kode di bawah untuk melihat error
#print(word[42])
#---- bagian error ----#

print(word[4:42])
print(word[42:])

#---- bagian error ----#
# hilangkan tanda '#' disamping kiri kode di bawah untuk melihat error
#word[0] = 'J'
#word[2:] = 'py'
#---- bagian error ----#

print('J' + word[1:])
print(word[:2] + 'py')

s = 'supercalifragilisticexpialidocious'
print(len(s))
