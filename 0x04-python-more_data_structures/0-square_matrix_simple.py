#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    newList = []
    for i in matrix:
        tmpl = list(map(lambda x: x**2, i))
        newList.append(tmpl)
    return newList
