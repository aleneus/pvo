class BuildingTextView:
    def purpose(self, p):
        print(p)

    def numbers(self, ns, purpose):
        print('Rooms for {0}:'.format(purpose))
        for n in ns:
            print(n)
