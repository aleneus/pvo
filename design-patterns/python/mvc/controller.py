from model import *
from view import *

class BuildingController:
    def __init__(self, model=None, view=None):
        self.model = model
        self.view = view

    def open_or_create_db(self, file_name):
        self.model.open_db(file_name)

    def set_view(self, view):
        self.view = view

    def info(self):
        data = self.model.get_info()
        self.view.table(data)

    def purpose(self, number):
        data = self.model.get_purpose(number)
        self.view.table(data)

    def numbers_by_purpose(self, purpose):
        numbers_data = self.model.get_numbers_by_purpose(purpose)
        self.view.table(numbers_data)
