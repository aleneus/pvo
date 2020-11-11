import random


class Vehicle:
    def beep(self):
        pass


class Bus(Vehicle):
    class Factory:
        @staticmethod
        def create():
            return Bus()

    def beep(self):
        print('Bus beeps')


class Car(Vehicle):
    class Factory:
        @staticmethod
        def create():
            return Car()

    def beep(self):
        print('Car beeps')


class VehicleFactory:
    fabrics = {
        'Bus': Bus.Factory,
        'Car': Car.Factory,
    }

    @staticmethod
    def create(name):
        if name not in VehicleFactory.fabrics.keys():
            raise AttributeError('Wrong name of vehicle')
        return VehicleFactory.fabrics[name].create()


if __name__ == "__main__":
    names = ['Bus', 'Car']
    vehicle_fabric = VehicleFactory()
    vehicles = [vehicle_fabric.create(random.choice(names))
                for i in range(20)]
    for v in vehicles:
        v.beep()
