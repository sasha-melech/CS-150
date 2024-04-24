##
# Andy Bart and Sasha Donaldson
# Lab 9: Practice with Class Definitions
# 04/24/2024
##


class Dog:
    """
    Andy Bart and Sasha Donaldson
    Class creates a model for a dog which includes methods for monitoring,
    changing, playing with, comparing, editing, and printing modeled
    dogs with a name, breed, weight, and color.
    """

    def __init__(self, name, breed, weight, color="brown"):
        self.name = name
        self.breed = breed
        self.weight = weight
        self.color = color

    def get_name(self):
        """
        Gets the dog's name and returns it as a string
        :return: the dog's name
        """
        return self.name

    def get_breed(self):
        """
        Gets the dog's breed and returns it as a string
        :return: the dog's breed
        """
        return self.breed

    def set_breed(self, new_breed):
        """
        Sets the dog's breed to any value based on the `new_breed` parameter
        :param new_breed: the new breed that the dog will be set to
        :return:
        """
        if type(new_breed) is str:
            self.breed = new_breed
        else:
            raise TypeError("new_breed must be a string")

    def get_weight(self):
        """
        Gets the dog's breed and returns it as an int
        :return: the dog's weight
        """
        return self.weight

    def get_color(self):
        """
        Gets the dog's color and returns it as an int
        :return: the dog's color
        """
        return self.color

    def set_color(self, new_color):
        """
        Set a new color for the dog.
        """
        if type(new_color) is str:
            self.breed = new_color
        else:
            raise ValueError("new_color must be a string")

    def bark(self):
        """
        Make the dog start barking.
        """
        print(f"{self.name} says 'Bowowowowo!'")

    def growl(self):
        """
        Make the dog growl
        """
        print(f"{self.name} says 'Grrrrrr'")

    def play_outside(self):
        """
        PLay outside will make the dog bark, growl, 
        and then his fur will turn yellow from getting dirty.
        """
        self.bark()
        self.growl()
        self.set_color('yellow')

    def heaviest(self, other_dog):
        """
        This method will take two different dogs and 
        compare their weight, determining who is heavier.
        """
        if type(other_dog) is not Dog:
            raise TypeError("dog must be a dog")

        if self.weight == other_dog.get_weight():
            print(self.name, "and", other_dog.get_name(), "are the same")
        elif self.weight > other_dog.get_weight():
            print(self.name, "is heaviest")
        else:
            print(other_dog.get_name(), "is heaviest")

    def __str__(self):
        """
        This string method will return each value of 
        this dog object as one long string.
        """
        return (f'(name = {self.name}; breed = {self.breed};'
                f'weight = {self.weight}; color = {self.color})')


def test_dog():
    # Create an object for dog 1
    dog1 = Dog('spot', 'hound', 45)
    print(dog1)

    # Create an object for dog 2
    dog2 = Dog('fido', 'poodle', 10)
    print(dog2)

    # Get the name, breed, weight and color for dog 1
    print(dog1.get_name())
    print(dog1.get_breed())
    print(dog1.get_weight())
    print(dog1.get_color())

    # Set a new breed and color for dog 2
    dog2.set_breed("daschund")
    dog2.set_color("black")
    print(dog2)

    # Dog 1 barks and growls, and dog 2 will play outside
    dog1.bark()
    dog1.growl()
    dog2.play_outside()

    # Get the new color for dog 2
    print(dog2.get_color())

    # Compare weights of the different dogs
    dog1.heaviest(dog2)
    dog2.heaviest(dog1)
    dog2.heaviest(dog2)

    # Create an empty list for dogs in a kennel
    kennel = []

    # Add dogs to the kennel list
    kennel.append(Dog("nannette", "mountain feist", 25))
    kennel.append(Dog("honey", "yellow lab mix", 40, "yellow"))
    kennel.append(Dog("joy", "australian sheep dog", 43))
    kennel.append(Dog("bryson", "labrador", 80, "black"))

    # Print each dog in the kennel list
    for dog in kennel:
        print(dog)


def main():
    test_dog()


if __name__ == "__main__":
    main()
