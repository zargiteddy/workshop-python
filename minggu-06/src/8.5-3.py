try:
    open('database.sqlite')
except OSError:
    raise RuntimeError from None