import csv_file_reader
import csv_file_writer
import os

hashtags_occ = {}

for f in os.listdir('cleansed'):
    x = csv_file_reader.read_csv('cleansed/' + f)
    print(f)
    for i in range(0,len(x),5):
        if len(x[i])>6 and x[i][6] != 'NULL' and x[i][3]=='en':
            s = x[i][6]
            tmp = s.split()
            for word in tmp:
                for c in word:
                    if c=='#':
                        if word in hashtags_occ:
                            hashtags_occ[word] += 1
                        else:
                            hashtags_occ[word] = 1
sorted_keys = sorted(hashtags_occ,key=hashtags_occ.get,reverse=True)
res = []
for key in sorted_keys:
    res.append([key,hashtags_occ[key]])
csv_file_writer.write_csv('hashtags_occurrence.csv', res)


