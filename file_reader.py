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


"""
input:
    path of the mat file containing vectors and labels
output:
    4 lists
    train and test vectors
    train and test labels
"""


def read_data_vectors(path):
    vectors = scipy.io.loadmat(path)
    test_vectors = vectors['test_vectors']
    train_vectors = vectors['train_vectors']
    train_labels = vectors['train_labels']
    test_labels = vectors['test_labels']
    return train_vectors, test_vectors, train_labels, test_labels


"""
input:
    path of kernels
output:
    return two kernels train-train and test-train
"""


def load_kernel(path):
    tmp = scipy.io.loadmat(path)
    return tmp['train_train'], tmp['test_train']
