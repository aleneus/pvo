class Vehicle:
    def fabricate(name):
        if name == 'Car':
            return Car()
        if name == 'Truck':
            return Truck()
        if name == 'Bus':
            return Bus()
        if name == 'Bike':
            return Bike()
        raise AttributeError('Wrong vehicle type')
    fabricate = staticmethod(fabricate)

class Car(Vehicle):
    def beep(self):
        print('Car beeps')

class Truck(Vehicle):
    def beep(self):
        print('Truck beeps')

class Bus(Vehicle):
    def beep(self):
        print('Bus beeps')

class Bike(Vehicle):
    def beep(self):
        print('Bike beeps')

###################################

from random import randint

names = ['Car', 'Bus', 'Truck', 'Bike']

vehicles = [Vehicle.fabricate(names[randint(0,3)]) for i in range(20)]

for v in vehicles:
    v.beep()
