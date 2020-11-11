class OnlyOne:
    
    class __OnlyOne:
        def __init__(self):
            self.val = None
        def __str__(self):
            return repr(self) + self.val
        
    instance = None
    
    def __new__(cls):
        if not OnlyOne.instance:
            OnlyOne.instance = OnlyOne.__OnlyOne()
        return OnlyOne.instance
    
    def __getattr__(self, name):
        return getattr(self.instance, name)

x = OnlyOne()
x.val = 'value 1'
print(x)

y = OnlyOne()
y.val = 'value 2'
print(y)
