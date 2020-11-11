class Log:
    class __Log:
        def log(self, string):
            print('Log: ' + string)

    instance = None

    def __init__(self):
        if not Log.instance:
            Log.instance = Log.__Log()

    def __getattr__(self, name):
        return getattr(self.instance, name)

    def log(self, string):
        self.instance.log(string)


if __name__ == "__main__":
    l1 = Log()
    print(l1.instance)
    l2 = Log()
    print(l2.instance)

    l1.log('debug string from l1')
    l2.log('debug string from l2')
