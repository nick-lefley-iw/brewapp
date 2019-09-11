class Person:
    def __init__(self,first_name,surname, favourite_drink):
        self.first_name = first_name
        self.surname = surname
        self.favourite = favourite_drink

    def get_name(self):
        return f"{self.first_name} {self.surname}"

    def get_favourite(self):
        return self.favourite