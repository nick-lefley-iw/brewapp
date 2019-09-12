class Round:
    def __init__(self, maker, people_list, active=True):
        self._maker = maker
        self._people = people_list
        self._status = active

    def get_people(self):
        return self._people


    def get_drinks(self):
        drinks = []
        for person in self._people:
            drinks.append(person.get_favourite())

    def is_active(self):
        return self._status
