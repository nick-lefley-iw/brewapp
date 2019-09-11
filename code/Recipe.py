class Recipe:
    def __init__(self,location,steps):
        self.location = location
        self.steps = steps

    def get_steps(self):
        return self.steps

    def get_location(self):
        return self.location

