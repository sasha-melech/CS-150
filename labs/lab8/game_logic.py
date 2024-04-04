# Sasha Donaldson and


import random
WINNER = 0


def generate_ticket():
    """
    The purpose of this function is to create an empty list and then populate
    it with 6 unique random numbers between 1 and 50 (inclusive). This
    represents a lottery ticket and therefore each number must be unique. Once
    a ticket is generated it should be returned. For guidance on generating
    random numbers, see the handout for lab 6. Make sure the numbers chosen are
    unique, that is, there are no repeated numbers.
    """
    ticket = []
    while len(ticket) < 6:
        entry = random.randint(1, 50)
        if entry not in ticket:
            ticket.append(entry)
    return ticket


def contains(list, value):
    """
    This function has two parameters. The first parameter contains a list and
    the second contains a value. The aim of this function is discover if the
    list contains the value. If it does the function should return true. If not
    then the function should return false.
    """
    return value in list


def display_ticket(ticket):
    """
    This function takes one parameter that contains a list. It should simply
    display the lottery ticket. For example:
    ========Ticket========
    [15, 23, 35, 16, 4, 28]
    """
    print(f'========Ticket========\n'
          f'{ticket}')


def smallest(list):
    """
    This function takes one parameter a list representing the lottery ticket.
    The function should deduce and return the lowest value in the list. This is
    used in the game function of super_loto.py with the value being passed by
    it to the powerball function.
    """
    list.sort()
    return list[0]


def check_off(ticket, winning_number):
    """
    This function receives two parameters a list representing a lottery ticket
    and a value representing a number called during the lottery game. The job
    of this function is to search the list for a number matching the contents
    of the value parameter. Any matching value within the list should be set to
    zero.
    """
    for index in range(len(ticket)):
        if ticket[index] == winning_number:
            ticket[index] = 0


def wins(ticket):
    """
    This function receives one parameter a list representing a ticket. The job
    of this function is to scan the list deduce what prize to issue if any. If
    two or more values have been checked off the function should return an
    integer prize value as an int. Use table 1 as a guide for what prizes are
    issued. If less than two numbers have been checked of the function should
    return a zero value.
    """
    winning_numbers = 0
    for number in ticket:
        if number == WINNER:
            winning_numbers += 1

    match winning_numbers:
        case 2:  # Two numbers $5 (Five)
            return 5
        case 3:  # Three Numbers $100 (One hundred)
            return 100
        case 4:  # Four Numbers $1000 (One thousand)
            return 1000
        case 5:  # Five Numbers $10,000 (Ten thousand)
            return 10000
        case 6:  # Six Numbers $1,000,000 (One million)
            return 1000000
        case _:
            return 0


def powerball(ticket, smallest_value):
    """
    The powerball function is optional (do it only if you have the time)
    represents a bonus game feature. The function receives two parameter,
    a list representing a lottery ticket and a second representing the lowest
    value in the original lottery ticket. The function should generate a random
    number between 1 and 50 inclusive. This number represents the Powerball. If
    the smallest value on the ticket is larger than the powerball the player is
    awarded a $1000 bonus, the value 1000 is returned. If no bonus was won zero
    will be returned.

    In addition to returning a value the function should display the following
    when no bonus is won
      Power Ball: 26 Smallest: 2
      No Powerball Bonus!!

    And the following when a bonus is won
      Power Ball: 9 Smallest: 12
      POWERBALL BONUS WON!!
    """
    powerball_value = random.randint(1, 50)
    print(f'Power Ball: {powerball_value} Smallest: {smallest_value}\n')
    if smallest_value > powerball_value:
        print('POWERBALL BONUS WON!!')
        return 1000
    else:
        print(f'No Powerball Bonus!!')
        return 0
