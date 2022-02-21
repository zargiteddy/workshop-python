def fib(n):    # menulis deret Fibonacci sampai n
    """Print a Fibonacci series up to n."""
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

    # Panggil fungsi yang sudah didefinisikan:
    fib(2000)

    fib
    f = fib
    f(100)

    fib(0)
    print(fib(0))