#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for row in matrix:
        new_row = []
        for cell in row:
            new_number = cell ** 2
            new_row.append(new_number)
        new_matrix.append(new_row)
    return new_matrix
