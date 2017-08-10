import file_reader
import os

#for f in os.listdir('cleansed'):
    #x = file_reader.read_csv('cleansed/'+f)
x = file_reader.read_csv('cleansed/G5--2016-5-27--1.csv')
for row in x:
    if len(row)>6 and row[6] != 'NULL':
        print('__________________________________')
        s = row[6]
        print(s)
        tmp = s.split()
        for word in tmp:
            for c in word:
                if c=='#':
                    print(word)

