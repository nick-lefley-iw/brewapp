import unittest

from source.classes.Drink import Drink
from source.classes.Person import Person
from source.classes.Round import Round


class TestRound(unittest.TestCase):
    def setUp(self):
        self.test_drink = Drink("Tea", "Hot")
        self.test_person = Person("John", "Smoth", self.test_drink)
        self.second_test_person = Person("Jane", "Smath", self.test_drink)
        self.test_people_list = [self.test_person, self.second_test_person]

        self.expected_people_list = self.test_people_list
        self.test_round = Round(self.test_person, self.test_people_list)
        self.expected_drinks_list = [self.test_drink, self.test_drink]

    def test_get_people(self):
        self.assertEqual(self.test_people_list, self.test_round.get_people())

    def test_get_drinks(self):
        self.assertEqual(self.expected_drinks_list, self.test_round.get_drinks())

    def test_is_active(self):
        self.assertTrue(self.test_round.is_active())


if __name__ == '__main__':
    unittest.main()
