import file_reader
import os

for f in os.listdir('cleansed'):
    x = file_reader.read_csv('cleansed/'+f)
    
