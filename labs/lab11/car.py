class Car:
    def __init__(self, make: str, model: str, year: int, miles: int = 0):
        """
        Constructs a simulated car which has make, model, year, and miles
        self parameters.

        :param make: the make of the vehicle
        :param model: the model of the vehicle
        :param year: the year of the vehicle
        :param miles: the total number of miles the vehicle has traveled
        """
        self.make = make
        self.model = model
        self.year = year
        self.miles = miles

    def __str__(self):
        return (f'Car:****************\n'
                f'Make: {self.make}\n'
                f'Model: {self.model}\n'
                f'Year: {self.year}\n'
                f'Miles: {self.miles}\n'
                f'********************')

    def get_make(self) -> str:
        """
        Returns the make of the vehicle.

        :return: the make of the vehicle
        """
        return self.make

    def get_model(self) -> str:
        """
        Returns the model of the vehicle.

        :return: the model of the vehicle
        """
        return self.model

    def get_year(self) -> int:
        """
        Returns the year of the vehicle.

        :return: the year of the vehicle
        """
        return self.year

    def get_miles(self) -> int:
        """
        Returns the total number of miles the vehicle has traveled.

        :return: the total number of miles the vehicle has traveled
        """
        return self.miles

    def set_make(self, value) -> None:
        """
        Sets the make of the vehicle.
        :param value: the new make of the vehicle
        :return:
        """
        if type(value) is not str:
            raise TypeError('make must be a string')
        self.make = value

    def set_model(self, value) -> None:
        """
        Sets the model of the vehicle.
        :param value: the new model of the vehicle
        :return:
        """
        if type(value) is not str:
            raise TypeError('model must be a string')
        self.model = value

    def set_year(self, value) -> None:
        """
        Sets the year of the vehicle.
        :param value: the year make of the vehicle
        :return:
        """
        if type(value) is not int:
            raise TypeError('year must be an integer')
        self.year = value

    def set_miles(self, value) -> None:
        """
        Sets the total number of miles the vehicle has traveled.
        :param value: the new total number of miles the vehicle has traveled
        :return:
        """
        if type(value) is not int:
            raise TypeError('miles must be an integer')
        self.miles = value

    def travel(self, miles_traveled) -> None:
        """
        The car class should have a method called travel that receives as a
        parameter the miles to travel. If the miles to travel is not an
        integer a raise an appropriate exception. Likewise, if the miles to
        travel is negative also raise an appropriate exception. If the miles
        to travel is an appropriate value, then increment the odometer (
        miles) by that amount.

        :param miles_traveled: The number of miles travelled
        :return:
        """
        if type(miles_traveled) is not int:
            raise TypeError('miles traveled must be an integer')
        if miles_traveled <= 0:
            raise ValueError('miles traveled must be positive')
        self.miles += miles_traveled


def main():
    my_car = Car("Bord", "Drongo", 2006)
    print(my_car)
    my_car.travel(100)
    print(my_car)


if __name__ == '__main__':
    main()
