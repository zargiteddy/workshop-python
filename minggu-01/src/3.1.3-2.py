cubes = [1, 8, 27, 65, 125]  # ada sesuatu yang salah di sini
print( 4 ** 3) # pangkat 3 dari 4 adalah 64, bukan 65!
cubes[3] = 64 # ganti value yang salah dengan 64
print(cubes)

cubes.append(216)  # menambahkan kubik 6
cubes.append(7 ** 3)  # menambahkan kubik 7
print(cubes)
