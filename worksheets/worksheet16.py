# Task 3
# For the file, `data.txt` with the following contents:
#   10#5#A#50#2#15#100#@#1
# Read this file and total all the numeric values, ensuring the program
# does not crash.

total = 0
with open('data.txt', 'r') as data:
    numbers = data.readline().strip('\n').split('#')
    for item in numbers:
        try:
            total += float(item)
        except ValueError:
            continue

print(total)
