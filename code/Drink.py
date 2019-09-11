class Drink:
    def __init__(self, name, temperature, recipe):
        self.name = name
        self.temperature = temperature
        self.recipe = recipe

    def get_name(self):
        return self.name

    def is_hot(self):
        return self.temperature == "hot"

    def is_simple(self):
        return self.recipe.get_steps() <= 1
