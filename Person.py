class Person:

    def __init__(self, first, last):
        self.first_name = first
        self.last_name = last

    def description(self):
        return self.first_name + " " + self.last_name
