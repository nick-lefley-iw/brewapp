import unittest

import sys

sys.path.insert(1, '../code/')
from Drink import Drink
from Person import Person
from Round import Round


class TestRound(unittest.TestCase):
    test_drink = Drink("Tea", "Hot")
    test_person = Person("John", "Smoth", test_drink)
    second_test_person = Person("Jane", "Smath", test_drink)
    test_people_list = [test_person, second_test_person]


    expected_people_list = test_people_list
    expected_drinks_list = [test_drink,test_drink]


    test_round = Round(test_person, test_people_list)

    def test_get_people(self):
        self.assertEqual(self.test_people_list, self.test_round.get_people())

    def test_get_drinks(self):
        self.assertEqual(self.expected_drinks_list,self.test_round.get_drinks())

    def test_is_active(self):
        self.assertTrue(self.test_round.is_active())

if __name__ == '__main__':
    unittest.main()
