class Wife:
    """ Director 
    """
    def __init__(self):
        self._builder = None

    def construct(self, builder):
        self._builder = builder
        self._builder.build_table()
        self._builder.build_shelf()
        self._builder.build_cooker()

class Builder:
    """ Abstract builder
    """
    def __init__(self):
        self.product = Kitcnen()

    def build_table(self):
        pass

    def build_shelf(self):
        pass

    def build_cooker(self):
        pass

class Husband(Builder):
    """ Concrete builder
    """
    def build_table(self):
        print("Husband build table")
        self.product.table = "Made by husband"

    def build_shelf(self):
        print("Husband build shelf")
        self.product.shelf = "Made by husband"

    def build_cooker(self):
        pass

class Worker(Builder):
    """ Concrete builder
    """
    def build_table(self):
        print("Worker build table")
        self.product.table = "Made by worker"

    def build_shelf(self):
        print("Worker build shelf")
        self.product.shelf = "Made by worker"
        
    def build_cooker(self):
        print("Worker installed cooker")
        self.product.cooker = "Made by worker"

class Kitcnen:
    """ Product
    """
    def __init__(self):
        self.table = ""
        self.shelf = ""
        self.cooker = ""

    def show(self):
        print("Table: ", self.table)
        print("Shelf: ", self.shelf)
        print("Cooker: ", self.cooker)

wife = Wife()
husband = Husband()
worker = Worker()
wife.construct(worker)
kitchen = worker.product
kitchen.show()
