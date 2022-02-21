def fib2(n):  # return deret Fibonacci sampai n
     """Return a list containing the Fibonacci series up to n."""
     result = []
     a, b = 0, 1
     while a < n:
         result.append(a) 
         a, b = b, a+b
     return result

f100 = fib2(100)    # memanggil fungsi
f100                # menampilkan hasil