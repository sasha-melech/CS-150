# Authors: Erik Berger and Sasha Donaldson CS150
# Project 2: Vroom Vroom
# PURPOSE: This is a module for the CarSimStart.py file that stores functions
# enabling the driver file to run a car simulation program.

def travel(tank_size, miles_per_gallon, cost_per_gallon):
    """
    This is the primary function of the program that takes three parameters:
    tank-size, miles_per_gallon, and cost_per_gallon. It initializes the
    total_distance, net_miles, and trip_active variables. The function contains
    a while loop that allows the user to perform 3 commands:
        0) end the program and calc stats
        1) travel forward
        2) travel backward
    Any other input results in re-prompting until valid.
    """
    # Initialize variables
    total_distance = 0
    net_miles = 0
    # Find the maximum distance the car can travel with a full tank
    maximum_distance = find_maximum_distance(tank_size, miles_per_gallon)

    # Begin the car trip with a while loop
    while True:
        # Prompt user for option 0, 1, or 2
        option = input('Enter 0-End Trip(stats screen), 1-Travel Forward, '
                       '2-Travel Backward: ')

        # The reason case 1 and 2 are split up like this, despite being
        # basically the same, is because the project requirements stated
        # that the go_forward() and go_backward() functions had to only take
        # miles and net_miles as variables, so I thought it would be easier
        # to just restate case 1 and 2 rather than make a 'prepare_to_move()'
        # function.
        match option:
            case '0':
                break
            case '1':
                miles = valid_input('Distance Forward: ')
                if miles_exceeded(miles, total_distance, maximum_distance):
                    continue  # Restart the loop
                total_distance += miles
                net_miles = go_forward(miles, net_miles)
            case '2':
                miles = valid_input('Distance Backward: ')
                if miles_exceeded(miles, total_distance, maximum_distance):
                    continue
                total_distance += miles
                net_miles = go_backward(miles, net_miles)
            case _:
                continue

    gallons_used = find_gallons(total_distance, miles_per_gallon)
    total_fuel_cost = find_total_cost(gallons_used, cost_per_gallon)
    print_stats(total_distance, miles_per_gallon, net_miles, total_fuel_cost,
                gallons_used)


def go_forward(miles, net_miles):
    """
    This function takes miles_forward and net_miles as parameters to increment
    the net miles with a while loop. It returns the current net miles travelled.
    """
    while miles >= 1:
        net_miles += 1
        miles -= 1

    return net_miles


def miles_exceeded(miles, total_distance, maximum_distance):
    if miles + total_distance > maximum_distance:
        print(f'Not Enough Fuel!\n'
              f'{miles - (maximum_distance - total_distance)} miles'
              f'is too far!\n'
              f'Try Again!')


def go_backward(miles, net_miles):
    """
    This function takes miles_backward and net_miles as parameters to decrement
    the net miles with a while loop. It returns the current net miles travelled.
    """
    while miles >= 1:
        net_miles -= 1
        miles -= 1

    return net_miles


def find_maximum_distance(tank_size, miles_per_gallon):
    """
    This function takes tank_size and miles_per_gallon as parameters to
    calculate the maximum possible distance of travel (rounded to 2 decimal
    places) and then returns it to the user.
    """
    maximum_distance = round(tank_size * miles_per_gallon, 2)

    return maximum_distance


def find_gallons(total_dist_travelled, miles_per_gallon):
    """
    This function accepts total_dist_travelled and miles_per_gallon as
    parameters. It initializes and stores the gallons_used variable. It returns
    the gallons_used variable and rounds it to two places after the decimal.
    """
    # Use a try-except block to catch a ZeroDivisionError when calculating
    # gallons used
    try:
        gallons_used = total_dist_travelled / miles_per_gallon
    except ZeroDivisionError:
        gallons_used = 0
        print('MPG is Zero!')

    return round(gallons_used, 2)


def find_total_cost(gallons_used, cost_per_gallon):
    """
    This function takes gallons_used and cost_per_gallon as parameters then
    returns the total_fuel_cost variable rounded to two decimal places.
    """
    # calculate the total fuel cost and round it
    total_fuel_cost = round(gallons_used * cost_per_gallon, 2)

    return total_fuel_cost


def print_stats(total_dist_travelled, miles_per_gallon, net_miles,
                total_fuel_cost, gallons_used):
    """
    This function takes the total_dist_travelled, miles_per_gallon, net_miles,
    total_fuel_cost, and gallons_used variables then prints a report based on a
    trip.
    """
    # Generate a message based on the total fuel cost for the trip
    if total_fuel_cost >= 100:
        cost_comment = 'Ouuucccchhhh!'
    elif total_fuel_cost >= 25:
        cost_comment = 'Wallet getting nervous!'
    else:
        cost_comment = 'Cha Chiiiiiiiinnnnggg!'

    # Display the trip report
    print('====REPORT====\n'
          f'Total Miles traveled: {total_dist_travelled}\n'
          f'Net Miles: {net_miles}\n'
          f'Gallons Used: {gallons_used}\n'
          f'Miles Per Gallon: {miles_per_gallon}\n'
          f'Total Cost: ${total_fuel_cost}\n'
          f'{cost_comment}')


def valid_input(prompt):
    """
    This function ensures that the user enters a valid response to a prompt.
    it takes the prompt parameter and returns a valid value.
    """
    # Create a while loop to reprompt user for input if invalid
    while True:
        # Prompt user with input parameter and check if valid 
        try:
            value = float(input(prompt))
        except ValueError:
            print('Error. Please enter an integer.')
            continue
        if value < 0:
            print('Error. Please enter a positive integer.')
            continue
        return value
