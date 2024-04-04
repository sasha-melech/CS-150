# CS-150 Worksheet 14
# Sasha Donaldson
# Created 4/3/2024

# Preparation A: Fibonacci
# Write a function to safely write the fibonacci sequence.
def fibonacci(length):
    if type(length) is not int or length <= 0:
        print('error, sequence length is invalid')
        return []

    if length == 1:
        return [0]

    sequence = [0, 1]
    for _ in range(length - 2):
        sequence.append(sequence[-1] + sequence[-2])

    return sequence


# Preparation B: Index List
# Recreate an index list function to find the index of the first occurrence of a
# value. The function returns -1 if the value is not present.
def my_index(target_item, list):
    for value, item in enumerate(list):
        if target_item == item:
            return value
    return -1


# Task 1: Slice This
def slice_this():
    hex1 = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
            'A', 'B', 'C', 'D', 'E', 'F']
    # Slice 0-9 in two different ways
    print(hex1[:10])
    print(hex1[-16:-6])
    # Slice A-F in two different ways
    print(hex1[10:16])
    print(hex1[-6:])
    # Slice 7-9
    print(hex1[7:10])
    print(hex1[-9:-6])
    # Fill an array with 1-3 and A-C
    hex2 = hex1[1:4]
    hex2.extend(hex1[10:13])
    print(hex2)


slice_this()
