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
    dot_ind = -1
    for i in range(len(path)-1, -1, -1):
        if path[i] == '.':
            dot_ind = i
            break
    extension = path[dot_ind+1:]
    if extension == 'csv':
        return read_csv(path)
    elif extension == 'mat':
        return read_mat(path)
    else:
        raise Exception('Extension nut supported is')


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
    path of the mat file to read

output:
    numpy array
"""


def read_mat(path):
    dic = scipy.io.loadmat(path)
    return dic['array']




