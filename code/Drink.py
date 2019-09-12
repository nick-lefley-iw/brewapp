class Drink:
    def __init__(self, name, temperature):
        self._name = name
        self._temperature = temperature

    def __repr__(self):
        return self.get_name()

    def get_name(self):
        return self._name

    def get_temperature(self):
        return self._temperature

    def is_hot(self):
        return self._temperature == "hot"
