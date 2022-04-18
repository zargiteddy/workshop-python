from heapq import heapify, heappop, heappush
data = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
heapify(data) # mengatur ulang list ke dalam heap urutan
heappush(data, -5) # masukkan entry baru
print([heappop(data) for i in range(3)])  # ambil tiga entry terkecil