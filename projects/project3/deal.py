"""
Project 3 for CS150 spring of 2022. This program represents a computer
game version of the game Deal of No Deal (UK version).  Notice, the monetary
values shown are British pounds which are denoted by the £ symbol. You can
type this by holding down the alt key (option key on Mac OS) and typing the
number 156.

@author: Andrew Scott
@author: Sasha Donaldson and Andy Bart
@date: March 2022

Functions:
    greeting(prize_list)
    show_prizes(prize_list)
    generate_closed_boxes(prize_list> -> List 'int'
    show_closed_boxes(closed_boxes)
    choose_box() -> int
    open_box(closed_boxes,open_boxes)
    count_not_closed(closed_boxes) -> int
    prizes_remaining(prize_list,open_boxes) list 'int'
    banker(remaining_prizes) -> int
    winner(deal, offer,player_box)
    display_documentation()
    main()
"""
import random


# -------------------------------------------------
#        PUT YOUR FUNCTIONS UNDER HERE
# -------------------------------------------------

def greeting(prize_list) -> None:
    """
    This function receives one parameter, the list containing the remaining
    prizes on offer and announces the introduction to the game depending on
    the number of prizes in the original prize_list list.

    :param prize_list: A sorted list of available prizes
    """
    print(f'Welcome to deal or no deal, there are {len(prize_list)} prizes'
          f'that have been placed in {len(prize_list)}\n'
          f'now closed boxes at random. The prizes are: ')
    show_prizes(prize_list)


def show_prizes(prize_list) -> None:
    """
    This function receives one parameter, a list containing the remaining
    prizes and displays then to the console as follows

    :param prize_list: A sorted list of available prizes
    :return:
    """
    display_prize_list = prize_list.copy()
    display_prize_list.sort()
    print("Remaining Prizes: ")
    for prize in display_prize_list:
        print(prize)


def generate_closed_boxes(prize_list) -> list:
    """
    This function receives as a parameter the list of prizes. The function
    starts by making a copy of the prize_list parameter and declaring an
    empty list of closed_boxes. Then for as many numbers as there are in the
    prize list copy, randomly pop a value from copied prize list and append
    it to the list of closed_boxes until the copied list of prizes is empty.
    This should make it so that the list of closed boxes is in a random
    order. Finally, the function returns the list of closed_boxes.

    :param prize_list: A sorted list of available prizes.
    :return closed_boxes: A list containing all the available prizes after
    being shuffled, with the opened prizes set to none.
    """
    closed_boxes = []
    prize_list_copy = prize_list.copy()

    for _ in range(len(prize_list_copy)):
        random_prize_index = random.randint(0, len(prize_list_copy) - 1)
        random_prize = prize_list_copy.pop(random_prize_index)
        closed_boxes.append(random_prize)

    return closed_boxes


def show_closed_boxes(closed_boxes) -> None:
    """
    This function displays the closed boxes and the index positions of each
    box. Although the boxes would in reality be indexed from 0 to n (n being
    the number of boxes in the game), to be user-friendly show them as 1 to
    n+1. In this example, assume boxes 3 and 5 were opened. Bear in mind an
    element in the list of closed boxes may contain None (indicating it has
    been opened); when this happens the box can be skipped.

    :param closed_boxes: A list containing all the available prizes after being
        shuffled, with the opened prizes set to none.
    :return:
    """
    for box_number, box in enumerate(closed_boxes):
        if box is None:
            continue
        else:
            print(f'{box_number+1}[?]', end=' ')
    print('')


def choose_box(closed_boxes) -> float:
    """
    This function is used at the start of the game, allowing the player to
    choose a box to open from the closed boxes. Note, although the boxes are
    shown with indexes 1 to n (n being the number of boxes in the game) they
    are in fact indexed 0 to n-1, but we do this to make the game
    user-friendly. Bear this in mind when handling user input, for example if
    the user chooses to open box 2, element 1 in the array is used.

    After a box is selected, the value of the box is stored in a variable to
    return at the end of the function, and the corresponding element in the
    list of closed boxes is set to none.

    :param closed_boxes: A list containing all the available prizes after being
    shuffled, with the opened prizes set to none.
    :return prize: The cash amount in the selected box
    """
    show_closed_boxes(closed_boxes)
    selected_box = None
    while True:
        try:
            selected_box = int(input('Select a box: '))
            if closed_boxes[selected_box - 1] is not None and selected_box > 0:
                break
        except ValueError:
            print('Error, select an integer')
            continue
        except IndexError:
            print('Error, select a box number shown')
            continue
        print('Error, select a box number shown')
    print(f'Player has chosen box {selected_box}')

    prize = closed_boxes[selected_box-1]
    closed_boxes[selected_box-1] = None
    return prize


def open_box(closed_boxes, open_boxes) -> None:
    """
    This function is used during the game, it allows the user to select a box
    to open from the closed boxes. When input is valid it announces what box
    number was chosen and reveals what is in that box. While input is invalid
    (not a number or out of bounds) an error is displayed and input is
    requested again. Note: although the boxes are shown with indexes 1 to n (n
    being the number of boxes in the game) they are in fact indexed 0 to  n-1,
    but we do this to make the game user-friendly. Bear this in mind when
    handling user input, for example if the user chooses to open box 2,
    element 1 in the array is used.

    When the box is selected the value at that index should be stored in a
    variable and then added to the list of open_boxes. The value at the
    chosen index `index` in the list of closed_boxes should be set to none.
    Note, this function is very similar to the previous function, consider
    how to maximize reuse of pre-exiting code rather than reinventing the
    wheel.

    :param closed_boxes: A list containing all the available prizes after being
    shuffled, with the opened prizes set to none.
    :param open_boxes: A list of the prizes which have been opened.
    """
    selected_box_prize = choose_box(closed_boxes)
    print(f'The box you opened had £{selected_box_prize}.')
    open_boxes.append(selected_box_prize)


def count_not_closed(closed_boxes) -> float:
    """
    Counts the number of closed boxes that have not been opened yet.

    :param closed_boxes: A list of closed boxes with shuffled prizes.
    :return count: The count of closed boxes that have not been opened yet.
    """
    count = 0
    for box in closed_boxes:
        if box is not None:
            count += 1
    return count


def prizes_remaining(prize_list, open_boxes) -> list:
    """
    Iterates through all prizes in the prize list and in the open boxes to
    find which prizes are remaining without looking at `closed_boxes`

    :param prize_list: A sorted list containing the available prizes.
    :param open_boxes: A chronologically ordered list of boxes which have been
    opened
    :return remaining_prizes: A list containing prizes that have not been
    opened
    """
    remaining_prizes = []
    for prize in prize_list:
        if prize not in open_boxes:
            remaining_prizes.append(prize)
    return remaining_prizes


def banker(prize_remaining) -> float:
    """
    Calculates the banker's offer based on the remaining prizes.

    :param prize_remaining: A list containing the remaining prizes.
    :return offer: The banker's offer.
    """
    total = 0
    for prize in prize_remaining:
        total += prize
    average_prize = total / len(prize_remaining)
    offer = int(average_prize * 0.7)  # 70% of the average prize
    return offer


def winner(deal, offer, players_box) -> None:
    """
    Determines the winner of the game and announces the result.

    :param deal: Indicates if a deal was made.
    :param offer: The last offer given by the banker.
    :param players_box: The value of the player's box.
    """
    print(f'Your box had £{players_box},'
          f'the bankers final offer was £{offer}.')
    if deal:
        if players_box <= offer:
            print(f"The player beat the banker.")
            print(f"The player gets £{offer}.")
        else:
            print(f"The banker beat the player.")
            print(f"The player gets £{offer}.")
    else:
        if players_box >= offer:
            print(f"The player beat the banker.")
            print(f"The player gets £{players_box}.")
        else:
            print(f"The banker beat the player.")
            print(f"The player gets £{players_box}.")


# End of area where your functions are defined ----------------

# --------------------------------------------------------------
# DO NOT EDIT THE CODE OF THIS FUNCTION: Read and make sure you understand it
# --------------------------------------------------------------
def display_documentation():
    """Displays the documentation for every function in the app"""
    print("========Module Deal.py documentation")
    print(__doc__)
    print("=========Function Documentation========")
    print("Function: Main:")
    print(main.__doc__)
    print("Function: Greeting:")
    print(greeting.__doc__)
    print("Function: Show Prizes:")
    print(show_prizes.__doc__)
    print("Function: generate_closed_boxes:")
    print(generate_closed_boxes.__doc__)
    print("Function: show_closed_boxes:")
    print(show_closed_boxes.__doc__)
    print("Function: show_prizes:")
    print(show_prizes.__doc__)
    print("Function: choose_box:")
    print(choose_box.__doc__)
    print("Function: open_box:")
    print(open_box.__doc__)
    print("Function: count_not closed:")
    print(count_not_closed.__doc__)
    print("Function: banker:")
    print(banker.__doc__)
    print("Function: winner:")
    print(winner.__doc__)
    print("Function: display_documentation:")
    print(display_documentation.__doc__)


# --------------------------------------------------------------
# DO NOT EDIT THE CODE OF THE MAIN FUNCTION: Read and ake sure you understand it
# --------------------------------------------------------------

def main():
    """Plays the game of deal or no deal."""
    # All the possible prizes, used to print out prizes left and to initialize
    # closed boxes, uncomment which one to use.

    if input("Enter 1 to see documentation, any other value to play:") == "1":
        display_documentation()
        exit()

    success = False
    while not success:  # Game choice big or small
        game_choice = input("\nBig or small game, 1) small, 2) big: ")
        if game_choice == "2":
            prize_list = [0.01, 0.10, 0.50, 1, 5, 10, 50, 100, 250, 500, 750,
                          1000, 3000, 5000, 10000, 15000, 20000, 35000, 50000,
                          75000, 100000, 250000]
            success = True
        elif game_choice == "1":
            prize_list = [1, 10, 100, 1000, 10000, 100000]
            success = True
        else:
            print("Error select 1 or 2")

    player_prize = 0
    deal = False  # No deal banker!!

    greeting(prize_list)

    open_boxes = []  # Open boxes start out empty
    closed_boxes = generate_closed_boxes(prize_list)

    print("\nPlayer please choose YOUR box.")
    players_box = choose_box(closed_boxes)
    count = 0

    # Player opens a box and then a bankers deal is offered until the player
    # accept the deal or sticks on to the bitter end
    while count_not_closed(closed_boxes) > 1 and deal == False:

        # Player chooses box to open
        chosen_box = open_box(closed_boxes, open_boxes)
        count += 1

        remaining = prizes_remaining(prize_list, open_boxes)
        show_prizes(remaining)

        # Every3rd go, or when3 or less boxes remaining or for small game banker
        # makes a deal
        if count % 3 == 0 or len(remaining) <= 3 or game_choice == "1":
            # calculate banker's deal
            bankers_offer = banker(remaining)

            print("\nBanker offers £", bankers_offer, sep="")

            choice = input("Deal or no deal?")
            deal = choice.upper() == "DEAL"  # Player made a deal

    if not deal:  # Banker offers final deal if no deal.
        print("\nThere are only two boxes remaining, yours and the other one")
        bankers_offer = banker(remaining)

        print("\nBanker's final' offers £", bankers_offer, sep="")
        choice = input("Deal or no deal?")
        deal = choice.upper() == "DEAL"  # Player made a deal

    # Once loop over anounce winner
    print("")  # blank line
    winner(deal, bankers_offer, players_box)


# Comment out the below line if you are testing your solution by calling methods
# directly. Uncomment it and remove the tests before submission.
if __name__ == "__main__":
    main()
