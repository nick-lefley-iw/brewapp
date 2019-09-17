import unittest

import sys

sys.path.insert(1, '../code/')
from Drink import Drink
from Person import Person


class TestPerson(unittest.TestCase):
    def setUp(self):
        self.test_drink = Drink("Tea", "Hot")
        self.test_person = Person("John", "Smoth", self.test_drink)
        self.expected_full_name = "John Smoth"
        self.expected_order = [self.expected_full_name, self.test_drink]

    def test_get_name(self):
        self.assertEqual(self.expected_full_name, self.test_person.get_name())

    def test_get_favourite(self):
        # self.assertIs(self.test_drink, self.test_person.get_favourite())
        self.assertEqual(self.test_drink, self.test_person.get_favourite())

    def test_get_order_as_list(self):
        self.assertEqual(self.expected_order, self.test_person.get_order_as_list())


if __name__ == '__main__':
    unittest.main()
