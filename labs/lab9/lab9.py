# Sasha Donaldson and Greyson Calhoun
# Lab 9
# Created 4/10/2024
# Functions:
#     make_list2D(int, int) -> list
#     make_random2D(int, int) -> list
#     print2D(list)
#     sum_array(list) -> int
#     row_sum(list, int) -> int
#     col_sum(list, int) -> int
#     corner_sum(list) -> int


from random import randint


def make_list2D(rows, columns) -> list:
    """
    This method makes a 2D nxn matrix filled with zeros with `rows` rows and
    `columns` columns.

    :param rows: The number of rows in the matrix
    :param columns: The number of columns in the matrix
    :return:
    """
    matrix = []
    for _ in range(rows):
        row = [0] * columns  # Create a row with zeroes for each column
        matrix.append(row)  # Append the row to the matrix
    return matrix


def make_random2D(rows, columns) -> list:
    """
    This method makes a 2D nxn matrix filled with random integers from 0 to 9
    with `rows` rows and `columns` columns.

    :param rows: The number of rows in the matrix
    :param columns: The number of columns in the matrix
    :return:
    """
    matrix = []
    for _ in range(rows):
        row = []
        for _ in range(columns):
            # Append a random integer between 0 and 9 to the row for each column
            row.append(randint(0, 9))
        matrix.append(row)

    return matrix


def print2D(matrix) -> None:
    """
    This method prints out a matrix separating rows with a newline.

    :param matrix: The matrix being printed
    :return:
    """
    for row in matrix:
        for item in row:
            # Print each item in the row without newlines
            print(f'[{item}]', end='')
        print('')  # Print a newline to separate rows
    print('')


def matrix_sum(matrix) -> int:
    """
    This method calculates the total of all items in a 2-dimensional matrix.

    :param matrix: The matrix which we are summing the items of.
    :return:
    """
    total = 0
    for row in matrix:  # Perform a loop for each row in the matrix
        for item in row:
            total += item  # Add the extracted item to the total
    return total


def row_sum(matrix, row_index) -> int:
    """
    This function calculates the total of items in a specific row at `row_index`
    for a 2D matrix.

    :param matrix: The matrix which we are summing the items of.
    :param row_index: The index of the row where we are summing items.
    :return:
    """
    total = 0
    for item in matrix[row_index]:  # Loop over each item at a row index
        total += item
    return total


def column_sum(matrix, column_index) -> int:
    """
    This function calculates the total of items in a specific column at
    `column_index` for a 2D matrix.

    :param matrix: The matrix which we are summing the items of.
    :param column_index: The index of the column where we are summing items.
    :return:
    """
    total = 0
    for row in matrix:
        # Add the cosponsoring item in the column index from each row to
        # the total
        total += row[column_index]
    return total


def corner_sum(matrix) -> int:
    """
    This function calculates the sum of each of the items in the corners of the
    matrix (right/leftmost and top/bottommost)

    :param matrix: The matrix which we are summing the items of.
    :return:
    """
    return matrix[0][0] + matrix[0][-1] + matrix[-1][0] + matrix[-1][-1]


def main():
    zero_list = make_list2D(5, 5)
    random_list1 = make_random2D(5, 4)
    random_list2 = make_random2D(3, 4)
    print2D(zero_list)
    print2D(random_list1)
    print2D(random_list2)
    print("Total of col1: ", column_sum(random_list2, 1))
    print("Total of row0: ", row_sum(random_list2, 0))
    print("Total of corners ", corner_sum(random_list2))


if __name__ == '__main__':
    main()
