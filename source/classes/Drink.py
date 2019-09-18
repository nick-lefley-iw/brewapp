class Drink:
    def __init__(self, name, temperature):
        self._name = name
        self._temperature = temperature.upper()

    def __repr__(self):
        return self.get_name()

    def __eq__(self, other):
        if not isinstance(other, Drink):
            # don't attempt to compare against unrelated types
            return NotImplemented

        return self._name == other._name and self._temperature == other._temperature

    def get_name(self):
        return self._name

    def get_temperature(self):
        return self._temperature

    def is_hot(self):
        return self.get_temperature() == "HOT"