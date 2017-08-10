"""
Written by Benyamin Bashari
"""
import csv
import scipy.io

"""
input:
    path of the file to write
    data to write

data must be string

output:
    write data in path
"""


def write(path, data):
    file = open(path, 'w')
    file.write(data)
    file.close()


"""
input:
    path of the file to write
    data to write

write data in specific format based on path extension
if extension is .csv -> 2D list
if extension is .mat -> numpy array

output:
    write data in path
"""


def write_format_file(path, data):
    dot_ind = -1
    for i in range(len(path) - 1, -1, -1):
        if path[i] == '.':
            dot_ind = i
            break
    extension = path[dot_ind + 1:]
    if extension == 'csv':
        write_csv(path, data)
    elif extension == 'mat':
        write_mat(path, data)
    else:
        raise Exception('Extension is not supported is')


"""
input:
    path of the file to write
    data to write

data must be 2D list

output:
    write data in csv format
"""


def write_csv(path, data):
    file = open(path, 'w', newline='')
    csv_file = csv.writer(file)
    for row in data:
        csv_file.writerow(row)
    file.close()

"""
input:
    path of the file to write
    data to write

data must be numpy array

output:
    writes data in mat format
"""


def write_mat(path, data):
    scipy.io.savemat(path, {'array': data})



