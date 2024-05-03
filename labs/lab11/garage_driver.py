from car import Car
from garage import Garage


def main():
    """
    This function tests the Garage and Car classes. The function creates
    two Car objects and a Garage object and uses this to test the
    functionality of these two classes
    """

    # Create an empty garage and print it
    a_garage = Garage()
    print(a_garage, "\n")

    # Build new cars
    my_car = Car("Pointy-Yack", "Trash-AM", 1975, 20100)

    partners_car = Car("Cadililac", "Coupe Devil", 1982, 43210)

    # make garage but put only one car in
    our_garage = Garage(my_car)

    our_garage.set_car1(my_car)

    # print out the status of our garage now.
    print(our_garage, "\n")

    # Put second car in garage
    our_garage.set_car2(partners_car)

    # print out the status of our garage now.
    print(our_garage, "\n")

    # Take cars for a spin
    partners_car.travel(100)
    my_car.travel(5)

    # Print out status of our garage now.
    print(our_garage, "\n")


# Call pythons main method if this file is called directly by the interpreter.
if __name__ == "__main__":
    main()
