from car import Car


def main():
    """
    This function tests the Car class. The function creates two Car
    objects and ses this to test the functionality of the Car class
    """

    # Make two cars
    a_car = Car("Bord", "Drongo", 2006)
    another_car = Car("Puik", "LeSober", 2009)

    # Display details of a_car.
    print(a_car)

    # print details of another_car
    print(another_car)

    # Change some details in a_car
    a_car.set_year(2007)
    a_car.set_model("Bronco")
    a_car.set_make("Ford")
    a_car.travel(100)

    another_car.travel(55)

    # Display details of a_car.
    print(a_car)

    # print details of another_car
    print(another_car)


# Call pythons main method if this file is called directly by the interpreter.
if __name__ == "__main__":
    main()
