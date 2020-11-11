# TODO: add description
# TODO: add short docstrings for classes

class Vehicle:
    def beep(self):
        pass

class Bus(Vehicle):
    class Factory:
        def fabricate():
            return Bus()
        fabricate = staticmethod(fabricate)
    def beep(self):
        print('Bus beeps')

class Car(Vehicle):
    class Factory:
        def fabricate():
            return Car()
        fabricate = staticmethod(fabricate)
    def beep(self):
        print('Car beeps')

class VehicleFactory:
    fabrics = {
        'Bus' : Bus.Factory,
        'Car' : Car.Factory,
    }
    def fabricate(name):
        if name not in VehicleFactory.fabrics.keys():
            raise AttributeError('Wrong name of vehicle')
        return VehicleFactory.fabrics[name].fabricate()
    fabricate = staticmethod(fabricate)

##################

import random

names = ['Bus', 'Car']

vehicle_fabric = VehicleFactory()

vehicles = [vehicle_fabric.fabricate(random.choice(names)) for i in range(20)]

for v in vehicles:
    v.beep()
