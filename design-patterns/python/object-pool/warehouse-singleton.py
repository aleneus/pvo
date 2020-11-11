""" Object pool example

This example discussed here: https://sourcemaking.com/design_patterns/object_pool

The warehouse is singleton here.
"""

class Warehouse:
    class __Warehouse:
        def __init__(self, size):
            self._devices = [Device() for _ in range(size)]

    instance = None
    
    def __init__(self, size):
        if not Warehouse.instance:
            Warehouse.instance = Warehouse.__Warehouse(size)
        
    def acquire(self):
        return self.instance._devices.pop()

    def release(self, device):
        self.instance._devices.append(device)

class Device:
    pass

w1 = Warehouse(10)
d = w1.acquire()
print(d)
w1.release(d)

w2 = Warehouse(10)
d = w2.acquire()
print(d)
w1.release(d)
