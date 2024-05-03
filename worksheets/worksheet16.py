# Task 3
# For the file, `data.txt` with the following contents:
#   10#5#A#50#2#15#100#@#1
# Read this file and total all the numeric values, ensuring the program
# does not crash.
def sum_file():
    total = 0
    with open('data.txt', 'r') as data:
        numbers = data.readline().strip('\n').split('#')
        for item in numbers:
            try:
                total += float(item)
            except ValueError:
                continue


# Task 4
# Write a range function which uses optional values to work like the original
# range function, except it returns a list instead of an immutable object.
def my_range(start, stop=None, step=None):
    if stop is None:
        stop = start
        start = 0
    if step is None:
        step = 1

    ranges = [start]
    while ranges[-1]+step < stop:
        ranges.append(ranges[-1]+step)

    return ranges
