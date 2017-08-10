import csv_file_reader
import csv_file_writer
import os

x = csv_file_reader.read_csv('cleansed/G5--2016-5-27--1.csv')
s = set()
for i in range(0,len(x),5):
    s.add(x[i][2])
print(len(s))
print(len(x)/5)