# dates dapat dibuat and diformat dengan mudah
from datetime import date
now = date.today()
print(now)
print(now.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B."))

# dates mendukung perhitungan kalender
birthday = date(1964, 7, 31)
age = now - birthday
print(age.days)