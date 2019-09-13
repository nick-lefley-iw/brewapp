class Order:
    def __init__(self, person, drink):
        self._person = person
        self._drink = drink

    def __repr__(self):
        return (self._person, self._drink)
