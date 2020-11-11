# TODO: add descroption
# TODO: add short docstrings for classes

import random

class Human:
    def repr(self):
        pass

class Woman(Human):
    class Factory:
        def fabricate():
            return Woman()
        fabricate = staticmethod(fabricate)

class Man(Human):
    class Factory:
        def fabricate():
            return Man()
        fabricate = staticmethod(fabricate)

class Girl(Human):
    class Factory:
        def fabricate():
            return Girl()
        fabricate = staticmethod(fabricate)

class Boy(Human):
    class Factory:
        def fabricate():
            return Boy()
        fabricate = staticmethod(fabricate)

class HumanFactory:
    fabrics = {
        'Man' : Man.Factory,
        'Woman' : Woman.Factory,
        'Girl' : Girl.Factory,
        'Boy' : Boy.Factory,
    }
    def fabricate(name):
        if name not in HumanFactory.fabrics.keys():
            raise AttributeError('Wrong name of human')
        return HumanFactory.fabrics[name].fabricate()
    fabricate = staticmethod(fabricate)

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
            for p, n in zip(ps,names): 
                s += p
                if r <= s:
                    self.humans.append(f.fabricate(n))
                    break
    
ts = ToolsShop()
ts.generate_humans(50)
ts.show()
