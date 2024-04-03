##
# Authors: Erik Berger and Sasha Donaldson 
# CS150
# Project 2: Vroom Vroom
# PURPOSE: This is the driver file for CarSim.py that runs the car simulator.
##

from carSim import travel, valid_input  # Import the travel and valid_input method from carSim


def main():
    # Take input of Tank Size in Gallons, Then miles per gallon, Then cost per gallon
    tank_size = valid_input("Please enter your Car's Tank size (in gallons): ")
    miles_per_gallon = valid_input("Please enter your Car's Miles Per Gallon: ")
    cost_per_gallon = valid_input("Please enter your Car's Cost Per Gallon: ")

    # Pass input to the travel function in carSimStart
    print("\n=======CAR SIMULATOR=======\n")
    travel(tank_size, miles_per_gallon, cost_per_gallon)  # The method from carSim imported


main()
