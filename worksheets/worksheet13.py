# CS-150 Worksheet 13
# Sasha Donaldson
# Created 4/1/2024

# Task 1: Safe List
# Create function which allows a user to input n values which are exception
# handled.
def input_safe_list(intended_length):
    inputted_list = []
    while len(inputted_list) < intended_length:
        new_element = input(f'Enter value {len(inputted_list) + 1}: ')
        try:
            if '.' in new_element:
                inputted_list.append(float(new_element))
            else:
                inputted_list.append(int(new_element))
        except ValueError as error:
            print(error)
    return inputted_list


# Task 2: Print List
# Create a function which prints out a list
def print_list(printed_list):
    print(printed_list)


# Task 3: Biggest Value
# Create a function which returns the largest value in the list
def biggest(values_list):
    values_list.sort()
    return values_list[-1]


def main():
    length = 10
    user_list = input_safe_list(length)
    print_list(user_list)
    for i in range(5):
        print(biggest(user_list))


if __name__ == '__main__':
    main()
