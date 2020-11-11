def singleton(cls):
    print('Call decorator')
    instances = {}
    print(instances)
    def getinstance():
        print('Run getinstance')
        print(instances)
        if cls not in instances:
            instances[cls] = cls()
        return instances[cls]
    return getinstance

@singleton
class MyClass:
    def __init__(self):
        print('Run self-made init')
    def test(self):
        print('test')

m1 = MyClass()
print(m1)
m1.test()
m2 = MyClass()
print(m2)
