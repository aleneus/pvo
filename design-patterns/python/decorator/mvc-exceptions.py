class Component:
    def select_data(self):
        pass

class Model(Component):
    def __init__(self):
        self.opened = False
    
    def open_storage(self):
        # Open storage or return
        self.opened = True

    def select_data(self):
        if not self.opened:
            return "Wrong data"
        return "Selected data"

class Decorator(Component):
    def __init__(self, model):
        self.model = model

    def open_storage(self):
        pass

    def select_data(self):
        pass

class ModelWithExceptions(Decorator):
    def open_storage(self):
        self.model.open_storage()
    
    def select_data(self):
        if not self.model.opened:
            raise AttributeError("Storage not opened")
        return self.model.select_data()
        
class Controller:
    def set_model(self, model):
        self.model = model

    def open_storage(self):
        self.model.open_storage()
        
    def select_data(self):
        try:
            print(self.model.select_data())
        except Exception:
             print("Something wrong")
            
m = ModelWithExceptions(Model())
c = Controller()
c.set_model(m)
c.open_storage()
c.select_data()
