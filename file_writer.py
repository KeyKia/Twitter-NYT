"""
Written by Benyamin Bashari
"""
import csv
import scipy.io
import numpy as np

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
    extension = path[len(path)-3:]
    if extension == 'csv':
        write_csv(path, data)
    elif extension == 'mat':
        write_mat(path, data)
    else:
        raise('Extension is not supported is ' + extension)


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
write data in mat format
data must be numpy array
output:
    write data in path
"""


def write_mat(path, data):
    scipy.io.savemat(path, {'data': data})



"""
input:
    4 lists
    train and test vectors
    train and test labels
output:
    write vectors in a single .mat file
"""


def write_data_vectors(train_vectors, test_vectors, train_labels, test_labels, dest_path):
    scipy.io.savemat(dest_path, {'test_vectors': test_vectors,
                                 'train_vectors': train_vectors,
                                 'train_labels': train_labels,
                                 'test_labels': test_labels})

"""
input:
    write path
    two table train-train and test-train(similarity of objects)
output:
    write these 2 kernel in path
"""


def save_kernel(path, train_train, test_train):
    scipy.io.savemat(path, {'train_train': train_train, 'test_train': test_train})