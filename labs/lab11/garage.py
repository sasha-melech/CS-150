from car import Car


class Garage:
    def __init__(self, car1=None, car2=None):
        """
        Constructs a Garage with optional cars.
        :param car1: the Car in the Garage's first spot
        :param car2: the Car in the Garage's second spot
        """
        self.car1 = car1
        self.car2 = car2

    def __str__(self):
        """
        Allows for stringify implementations of the Garage class
        :return: Garage object displayed in string format
        """
        space1 = f'{self.car1}' if self.car1 is not None else 'Space 1: Empty'
        space2 = f'{self.car2}' if self.car2 is not None else 'Space 2: Empty'
        return (f'Garage:=============\n'
                f'{space1}\n'
                f'{space2}\n'
                f'====================')

    def get_car1(self):
        """
        Returns value of first car
        :return: value of first car
        """
        return self.car1

    def get_car2(self):
        """
        Returns value of second car
        :return: value of second car
        """
        return self.car2

    def set_car1(self, value):
        """
        Sets value of first car
        :return:
        """
        if type(value) is not Car:
            raise TypeError('set car must be a car')
        self.car1 = value

    def set_car2(self, value):
        """
        Sets value of second car
        :return:
        """
        if type(value) is not Car:
            raise TypeError('set car must be a car')
        self.car2 = value
