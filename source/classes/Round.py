from prettytable import PrettyTable


class Round:
    def __init__(self, maker, people_list, active=True):
        self._maker = maker
        self._people = people_list
        self._status = active

    def get_people(self):
        return self._people

    def get_maker(self):
        return self._maker

    def get_drinks(self):
        drinks = []
        for person in self._people:
            drinks.append(person.get_favourite())
        return drinks

    def print_round(self):
        print(f"The round's maker is: {self._maker}")
        x = PrettyTable()

        x.field_names = ['Person', 'Drink']
        for person in self._people:
            x.add_row(person.get_order_as_list())

        print(x)

    def is_active(self):
        return self._status
