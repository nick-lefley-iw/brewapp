class Recipe:
    def __init__(self,location,steps):
        self._location = location
        self._steps = steps

    def get_steps(self):
        return self._steps

    def get_location(self):
        return self._location

    def is_simple(self):
        return self.get_steps() <= 1
