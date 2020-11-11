""" Object pool example. This example discussed here:
https://sourcemaking.com/design_patterns/object_pool."""


class Warehouse:
    def __init__(self, size):
        self._devices = [Device() for _ in range(size)]

    def acquire(self):
        return self._devices.pop()

    def release(self, device):
        self._devices.append(device)


class Device:
    pass


if __name__ == "__main__":
    warehouse = Warehouse(10)
    device = warehouse.acquire()
    print(device)
    warehouse.release(device)

    device = warehouse.acquire()
    print(device)
    warehouse.release(device)

    device1 = warehouse.acquire()
    print(device1)
    device2 = warehouse.acquire()
    print(device2)
    warehouse.release(device1)
    warehouse.release(device2)
