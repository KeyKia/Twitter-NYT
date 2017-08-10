"""
Written by Benyamin Bashari
"""
import csv

def write_csv(path, data):
    file = open(path, 'w', newline='')
    csv_file = csv.writer(file)
    for row in data:
        csv_file.writerow(row)
    file.close()