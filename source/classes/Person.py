class Person:
    def __init__(self, first_name, surname, favourite_drink):
        self._first_name = first_name
        self._surname = surname
        self._favourite = favourite_drink

    def __repr__(self):
        return self.get_name()

    def get_name(self):
        return f"{self._first_name} {self._surname}"

    def get_favourite(self):
        return self._favourite

    def get_order_as_list(self):
        return [self.get_name(), self.get_favourite()]
