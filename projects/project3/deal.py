"""
Project 3 for CS150 spring of 2022. This program represents a computer game version
of the game Deal of No Deal (UK version).  Notice, the monitary values shown are
British pounds which are denoted by the £ smbol. You can type this by holding
down the alt key (option key on Mac OS) and typing the number 156.

@author: Andrew Scott
@author: YOUR NAME
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
import math
import copy


#-------------------------------------------------
#        PUT YOUR FUNCTIONS UNDER HERE
#-------------------------------------------------

def greeting(prize_list):
    number_of_prizes = len(prize_list)
    print(f"\nWelcome to deal or no deal, there are {number_of_prizes} prizes that have been placed in {number_of_prizes}"
          "\nnow closed boxes at random. The prizes are: ")
    show_prizes(prize_list)


def show_prizes(prize_list):
    new_prize_list = prize_list.copy()
    new_prize_list.sort()
    print("Remaining Prizes: ")
    for value in new_prize_list:
        print(value)



def generate_closed_boxes(prie_list):
    pass


def show_closed_boxes(closed_boxes):
    pass


def choose_box(closed_boxes):
    pass


def open_box(closed_boxes, open_boxes):
    pass


def count_not_closed(closed_boxes):
    pass


def prizes_remaining(prize_list, open_boxes):
    pass


def banker(prize_remaining):
    pass


def winner(deal, offer, players_box):
    pass    


#End of area where your functions are defined ----------------

#--------------------------------------------------------------
# DO NOT EDIT THE CODE OF THIS FUNCTION: But read and make sure you understand it
#--------------------------------------------------------------
def display_documentation():
    '''Displays the documentation for every function in the app'''
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



#--------------------------------------------------------------
# DO NOT EDIT THE CODE OF THE MAIN FUNCTION: but read and ake sure you understand it
#--------------------------------------------------------------

def main():
    '''Plays the game of deal or no deal.'''
    # All the possible prizes, used to print out prizes left and to initialize
    # closed boxes, uncomment which one to use.

    if  input("Enter 1 to see documentation, any other value to play:") == "1":
      display_documentation()
      exit()

    success = False
    while not success:  #Game choice big or small
        game_choice = input("\nBig or small game, 1) small, 2) big: ")
        if game_choice == "2":
            prize_list = [0.01,0.10,0.50, 1, 5, 10, 50, 100, 250, 500, 750, 1000,\
				3000,5000, 10000, 15000, 20000, 35000, 50000,75000,100000,250000]
            success = True
        elif game_choice == "1":
            prize_list = [1, 10, 100, 1000, 10000, 100000]
            success = True
        else:
            print("Error select 1 or 2")

    player_prize = 0
    deal = False#No deal banker!!

    greeting(prize_list)

    open_boxes = []#Open boxes start out empty
    closed_boxes = generate_closed_boxes(prize_list)

    print("\nPlayer please choose YOUR box.")
    players_box = choose_box(closed_boxes)
    count = 0

    #Player opens a box and then a bankers deal is offered until the player
    #accept the deal or sticks on to the bitter end
    while count_not_closed(closed_boxes) > 1 and deal == False:

        #Player chooses box to open
        chosen_box = open_box(closed_boxes,open_boxes)
        count+=1

        remaining = prizes_remaining(prize_list,open_boxes)
        show_prizes( remaining)

        #Every3rd go, or when3 or less boxes remaining or for small game banker
        #makes a deal
        if count % 3 == 0 or len(remaining) <= 3 or game_choice == "1":
            #calculate banker's deal
            bankers_offer = banker(remaining)

            print("\nBanker offers £",bankers_offer,sep="")

            choice = input("Deal or no deal?")
            deal =  choice.upper() == "DEAL"#Player made a deal

    if not deal:#Banker offers final deal if no deal.
        print("\nThere are only two boxes remaining, yours and the other one")
        bankers_offer = banker(remaining)

        print("\nBanker's final' offers £",bankers_offer,sep="")
        choice = input("Deal or no deal?")
        deal = choice.upper() == "DEAL"#Player made a deal

    #Once loop over anounce winner
    print("")#blank line
    winner(deal,bankers_offer,players_box)


#Comment out the below line if you are testing your solution by calling methods
#directly. Uncomment it and remove the tests before submission.
if __name__ == "__main__":
    main()
