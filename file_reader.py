"""
Written by Benyamin Bashari
"""

import csv
import scipy.io

"""
input:
    path of the file to read

output:
    a string contains everything in file
"""


def read(path):
    file = open(path, 'r')
    ret = file.read()
    file.close()
    return ret

"""
input:
    path of the file to read
based on extention of the path read the file in specific format
output:
    if extension is .mat -> numpy array
    if extnesion is .csv -> 2D list
"""


def read_format_file(path):
    extension = path[len(path)-3:]
    if extension == 'csv':
        return read_csv(path)
    elif extension == 'mat':
        return read_mat(path)
    else:
        raise ("Extension nut supported is" + extension)


"""
input:
    path of the csv file to read

output:
    2D list
"""


def read_csv(path):
    file = open(path, newline='')
    data = csv.reader(file)
    ret = []
    for row in data:
        ret.append(row)
    file.close()
    return ret


"""
input:
    path of the file to read
output:
    numpy array
"""


def read_mat(path):
    dic = scipy.io.loadmat(path)
    return dic['data']




