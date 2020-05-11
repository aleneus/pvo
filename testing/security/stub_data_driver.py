"""Stub data driver."""
from passwd import DataDriver


class StubDataDriver(DataDriver):
    def __init__(self):
        self.file_exists = False
        self.text = ""

    def read(self, name):
        return self.text

    def write(self, text):
        self.text = text

    def set_text(self, text):
        self.set_file_exists(True)
        self.text = text

    def set_file_exists(self, value):
        self.file_exists = value

    def get_text(self):
        return self.text
