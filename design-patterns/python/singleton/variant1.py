# additional 1, not Singleton yet
class Test1:
    field = 'Hello'

t1 = Test1()
print(getattr(t1, 'field'))

# additional 2, not Singleton yet
class Test2:
    field1 = 'Value of field1'
    def __getattr__(self, name):
        if name == 'field2':
            return 'Value of field2'

t2 = Test2()
print(t2.field1)
print(t2.field2)

# additional 3, not Singleton yet
class Test3:
    def __str__(self):
        return 'I am Test3'

t3 = Test3()
print(t3)


#Singleton (from Eckel and freinds)
class OnlyOne:
    class __OnlyOne:
        def __init__(self, arg):
            self.val = arg
        def __str__(self):
            return repr(self) + " val = "+ self.val
    instance = None
    def __init__(self, arg):
        if not OnlyOne.instance:
            OnlyOne.instance = OnlyOne.__OnlyOne(arg)
        else:
            OnlyOne.instance.val = arg

    def __getattr__(self, name):
        return getattr(self.instance, name)

x = OnlyOne('value 1')
print(x)
print(x.instance)
print(x.val)

y = OnlyOne('value 2')
print(y)
print(y.instance)
print(y.val)
