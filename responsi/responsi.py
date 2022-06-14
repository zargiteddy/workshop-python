import requests
import csv
import os

nama_file = 'responsi.csv'
url = 'https://www1.ncdc.noaa.gov/pub/data/cdo/samples/PRECIP_HLY_sample_csv.csv'
responsi = requests.get(url)

with open(nama_file, 'w') as file:
    file.write(str(responsi.content))

with open(nama_file, 'r') as file:
    csv_reader = csv.reader(file, delimiter=',')
    for line in csv_reader:
        print (line)