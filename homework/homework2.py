# CS-150 Homework 2: Count Letter
# Sasha Donaldson
# Created 4/2/2024
# Create a function which counts the number of occurrences of a character in
# each element in a list.
def count_letter(letter, list, case_sensitive=True):
    if type(letter) is not str or len(letter) > 1:
        print('error, letter is invalid')
        return 0

    occurrences = 0
    if not case_sensitive:
        letter = letter.lower()

    for item in list:
        if type(item) is not str:
            continue
        if not case_sensitive:
            item = item.lower()
        for character in item:
            occurrences += 1 if letter == character else 0

    return occurrences


def main():
    my_list = ['Homer', 'Marge', 'Bart', 'Lisa', 5, 'Maggie']
    target_letter = 'b'
    letter_count = count_letter(target_letter, my_list)
    print(f'The number of {target_letter}\'s in {my_list} is {letter_count}.')


if __name__ == '__main__':
    main()
