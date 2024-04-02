# CS-150 Homework 2: Count Letter
# Sasha Donaldson
# Created 4/2/2024
# Create a function which counts the number of occurrences of a character in
# each element in a list.
def count_letter(letter, list):
    if type(letter) is not str or len(letter) > 1:
        print('error, letter is invalid')
        return 0

    occurrences = 0
    letter.lower()

    for item in list:
        if type(item) is str:
            occurrences += item.lower().count(letter)

    return occurrences


def main():
    my_list = ['Homer', 'Marge', 'Bart', 'Lisa', 'Maggie']
    target_letter = 'bal'
    count = count_letter(target_letter, my_list)
    print(f'The number of {target_letter}\'s in {my_list} is {count}.')


if __name__ == '__main__':
    main()
