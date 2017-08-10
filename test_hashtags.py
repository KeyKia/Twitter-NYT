import file_reader
import os

#for f in os.listdir('cleansed'):
    #x = file_reader.read_csv('cleansed/'+f)
    x = file_reader.read_csv('/home/user/Desktop/Twitter-NYT/cleansed/G5--2016-5-27--5.csv')
    for row in x:
        s = row[6]
        tmp = s.split(" ")
        for word in tmp:
            if word[0]=='#' :
                print(word)

