import file_reader
import os

hashtags_occ = {}

for f in os.listdir('cleansed'):
    x = file_reader.read_csv('cleansed/'+f)
    for row in x:
        if len(row)>6 and row[6] != 'NULL':
            s = row[6]
            tmp = s.split()
            for word in tmp:
                for c in word:
                    if c=='#':
                        if word in hashtags_occ:
                            hashtags_occ[word] += 1
                        else:
                            hashtags_occ[word] = 1



