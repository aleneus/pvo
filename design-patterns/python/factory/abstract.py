""" Abstract factory example."""


class Person:
    def __init__(self, name):
        self.name = name

    def interact_with(self, utensil): pass


class Dishwasher(Person):
    def interact_with(self, utensil):
        print("{} washes {}".format(self.name, utensil.name()))


class Cook(Person):
    def interact_with(self, utensil):
        print("{} cooks in {}".format(self.name, utensil.name()))


class Utensil:
    def name(self): pass


class Pan(Utensil):
    def name(self):
        return "pan"


class Wok(Utensil):
    def name(self):
        return "wok"


class KitchenActivityFactory:
    def __init__(self, name, cls):
        self.name = name
        self.cls = cls

    def fabric_person(self):
        pass

    def fabric_utensil(self):
        pass


class WashingFactory(KitchenActivityFactory):
    def fabric_person(self):
        return Dishwasher(self.name)

    def fabric_utensil(self):
        return self.cls()


class CookingFactory(KitchenActivityFactory):
    def fabric_person(self):
        return Cook(self.name)

    def fabric_utensil(self):
        return self.cls()


class KitchenEnvironment:
    def __init__(self, factory):
        self.factory = factory
        self.p = factory.fabric_person()
        self.u = factory.fabric_utensil()

    def work(self):
        self.p.interact_with(self.u)


if __name__ == "__main__":
    k1 = KitchenEnvironment(WashingFactory("Aleksandr", Wok))
    k1.work()
    k2 = KitchenEnvironment(CookingFactory("Ann", Wok))
    k2.work()
