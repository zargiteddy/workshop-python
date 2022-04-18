import locale
print(locale.setlocale(locale.LC_ALL, 'English_United States.1252'))
conv = locale.localeconv()         
x = 1234567.8
print(locale.format("%d", x, grouping=True))
print(locale.format_string("%s%.*f", (conv['currency_symbol'],
                     conv['frac_digits'], x), grouping=True))