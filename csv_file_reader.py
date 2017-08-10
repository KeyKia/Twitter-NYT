"""
Written by Benyamin Bashari
"""

import csv


def read_csv(path):
    file = open(path, newline='')
    data = csv.reader(file)
    ret = []
    for row in data:
        ret.append(row)
    file.close()
    return ret
