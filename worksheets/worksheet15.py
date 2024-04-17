# CS-150 Worksheet 15
# Sasha Donaldson
# Created 4/10/2024
from pprint import pprint


# Task 1: 2D Data Structure of Zeros
# Create a 5x5 array of just zeros
def zeros():
    matrix = []
    for _ in range(5):
        row = [0] * 5
        matrix.append(row)
    return matrix


# Task 2: Data Structure of Numbers
# Build a 2D matrix which contains numbers 1-25 in row-column order
def numbers():
    matrix = []
    index = 1

    for _ in range(5):
        row = []
        for _ in range(5):
            row.append(index)
            index += 1
        matrix.append(row)

    return matrix


# Task 3: Dynamic 2D Data Structure
# Change Task 2's function to output any range of indexes based on a parameter
def range_matrix(start=1, end=25):
    matrix = []
    index = start
    row_length = int((end-start+1)**(1/2))

    while index <= end:
        row = []
        for _ in range(row_length):
            row.append(index)
            index += 1
        matrix.append(row)

    return matrix


pprint(range_matrix(1, 100))
