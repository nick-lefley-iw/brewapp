class Round:
    def __init__(self,maker,people_list):
        self.maker = maker
        self.people = people_list

    def get_people(self):
        return self.people
    

    def get_drinks(self):
        drinks = []
        for person in self.people:
            drinks.append(person.get_favourite())