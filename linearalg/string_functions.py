import numpy as np
import re


def is_int(number):
    '''
    Retruns True if string inputted is an int number
    '''
    try:
        int(number)
        return True
    except ValueError:
        return False


def list_to_array(list_):
    '''
    Converts list of numbers [str] to an array [Numpy format]
    '''
    arr = []
    for n in list_:
        if '/' in n:
            frac = n.split('/')
            arr.append(int(frac[0])/int(frac[1]))
        else:
            if is_int(n):
                arr.append(int(n))
            else:
                arr.append(float(n))

    return np.array(arr)


def vector_to_array(vec):
    '''
    Get array of n-dimensional vector

    Input:  vec(a b c d)
    Output: array [float]
    '''
    return list_to_array(vec[4:len(vec)-1].split(' '))


def matrix_to_array(matrix):
    '''
    Converts a nxn Matrix [PyMath format] to array [Numpy format]
    '''
    elements = matrix[7:len(matrix)-1].split(',')
    arr = []
    for nums in elements:
        nums_list = nums.strip().split(' ')
        arr.append(list_to_array(nums_list))

    return np.array(arr)


def array_to_vector(arr):
    '''
    Converts 1xn array to an n-dimensional vector 
    '''
    vector = 'vec('
    for i, n in enumerate(arr):
        vector += str(n)
        if i < len(arr) - 1:
            vector += ' '
        else:
            vector += ')'
    return vector


def array_to_matrix(arr):
    np.set_printoptions(precision=4)
    rows = str(arr).split('\n')

    for row in rows:
        if 'array' in row:
            raise ValueError('Could not convert array to matrix')

    matrix = rows[0][1::]
    for i, row in enumerate(rows[1::]):
        if i < len(rows) - 2:
            matrix += f'\n{row[1::]}'
        else:
            matrix += f'\n{row[1:len(row)-1]}'
    return matrix
