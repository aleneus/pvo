"""Factory method and factory."""
from random import randint


class Vehicle:
    """Any vehicle."""
    @staticmethod
    def create():
        """Create instance of class."""
        raise NotImplementedError

    def beep(self):
        """Beep signal."""
        raise NotImplementedError


class Car(Vehicle):
    """Car."""
    @staticmethod
    def create():
        return Car()

    def beep(self):
        print('Car beeps')


class Truck(Vehicle):
    """Truck."""

    @staticmethod
    def create():
        return Truck()

    def beep(self):
        print('Truck beeps')


class Bus(Vehicle):
    """Bus."""

    @staticmethod
    def create():
        return Bus()

    def beep(self):
        print('Bus beeps')


class Bike(Vehicle):
    """Bike."""

    @staticmethod
    def create():
        return Bike()

    def beep(self):
        print('Bike beeps')


def get_vehicle(name):
    """Creates vehicle by name."""
    name_to_vehicle = {
        'Bus': Bus,
        'Bike': Bike,
        'Truck': Truck,
        'Car': Car,
    }

    cls = name_to_vehicle[name]
    return cls.create()


def __get_rand_name():
    names = ['Car', 'Bus', 'Truck', 'Bike']
    return names[randint(0, len(names)-1)]


def main():
    """Example."""
    get_vehicle(__get_rand_name()).beep()
    get_vehicle(__get_rand_name()).beep()
    get_vehicle(__get_rand_name()).beep()
    get_vehicle(__get_rand_name()).beep()
    get_vehicle(__get_rand_name()).beep()


if __name__ == "__main__":
    main()
