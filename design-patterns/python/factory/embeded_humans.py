import random


class Human:
    def repr(self):
        pass


class Woman(Human):
    class Factory:
        @staticmethod
        def create():
            return Woman()


class Man(Human):
    class Factory:
        @staticmethod
        def create():
            return Man()


class Girl(Human):
    class Factory:
        @staticmethod
        def create():
            return Girl()


class Boy(Human):
    class Factory:
        @staticmethod
        def create():
            return Boy()


class HumanFactory:
    fabrics = {
        'Man': Man.Factory,
        'Woman': Woman.Factory,
        'Girl': Girl.Factory,
        'Boy': Boy.Factory,
    }

    @staticmethod
    def create(name):
        if name not in HumanFactory.fabrics.keys():
            raise AttributeError('Wrong name of human')
        return HumanFactory.fabrics[name].create()


class Shop:
    def __init__(self):
        self.humans = []

    def generate_humans(self, number):
        pass

    def show(self):
        print(self.humans)


class ToolsShop(Shop):
    def generate_humans(self, number):
        names = ['Man', 'Woman', 'Boy', 'Girl']
        ps = [70, 25, 4, 1]
        f = HumanFactory()
        self.humans = []
        for i in range(number):
            r = random.randint(0, 100)
            s = 0
            for p, n in zip(ps, names):
                s += p
                if r <= s:
                    self.humans.append(f.create(n))
                    break


if __name__ == "__main__":
    ts = ToolsShop()
    ts.generate_humans(50)
    ts.show()
