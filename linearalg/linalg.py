import numpy as np
import math


def _implicit_plane_eq(plane):
    '''
    Takes a list of the plane's coefficients and returns its implicit equation.

    ### Inputs ###
    plane = [a, b, c, d]

    ### Outputs ###
    ax + bx + cx + d = 0
    '''
    equation = ''
    sign = ''

    if plane[0] < 0:
        sign = '-'
    equation += f' {sign} {abs(plane[0])}x '

    if plane[1] < 0:
        sign = '-'
    else:
        sign = '+'

    equation += f'{sign} {abs(plane[1])}y '

    if plane[2] < 0:
        sign = '-'
    else:
        sign = '+'

    equation += f'{sign} {abs(plane[2])}z '

    if plane[-1] < 0:
        sign = '-'
    else:
        sign = '+'

    equation += f'{sign} {abs(plane[-1])} = 0'

    return equation


def normal_point_plane(n, p):
    '''
    ### Inputs ###
    n:      normal vector [1D array]
    p:      plane's point [1D array]

    ### Returns ###
    plane:  [a, b, c, d] ---> ax + by + cz + d = 0
    '''
    if np.all((n == 0)):
        # If normal vector is zero vector no plane is generated
        return 'No plane is generated'

    d = -n[0] * p[0] - n[1] * p[1] - n[2] * p[2]
    return _implicit_plane_eq(np.array([*[n[i] for i in range(3)], d]))


def vectors_and_point_plane(v1, v2, p):
    '''
    ### Inputs ###
    v1:     plane's vector  [1D array]
    v2:     plane's vector  [1D array] 
    p:      plane's point   [1D array]

    ### Return ###
    Implicit plane equation
    '''
    return normal_point_plane(np.cross(v1, v2), p)


def vectors_angles(v1, v2):
    '''
    ### Inputs ###
    v1:     [1D array]
    v2:     [1D array]

    ### Return ###
    Angle between inputted vectors [degrees]

    ### Warnings ###
    Both vectors must have the same dimension
    '''
    if np.all((v1 == 0)) or np.all((v2 == 0)):
        # Zero vectors are considered to have an angle of 90° with any other vector
        return 90

    return math.degrees(math.acos(np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))))


def is_square(matrix):
    '''
    Checks if matrix is square
    '''
    try:
        if matrix.shape[0] == matrix.shape[1]:
            return True
        return False
    except IndexError:
        return False


def eigen_values(matrix):
    return '\n'.join([str(v) for v in np.linalg.eig(matrix)[0]])


def matrix_addition(matrices):
    '''
    ### Input ###
    List of matrices [Numpy format]

    ### Return ###
    Sum of all matrices
    '''
    result = matrices[0]
    for matrix in matrices[1::]:
        result += matrix
    return result
