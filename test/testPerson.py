import unittest

import sys

sys.path.insert(1, '../code/')
from Drink import Drink
from Person import Person


class TestPerson(unittest.TestCase):
    test_drink = Drink("Tea", "Hot")
    test_person = Person("John", "Smoth", test_drink)
    expected_full_name = "John Smoth"
    expected_order = [expected_full_name, test_drink]

    def test_get_name(self):
        self.assertEqual(self.expected_full_name, self.test_person.get_name())

    def test_get_favourite(self):
        # self.assertIs(self.test_drink, self.test_person.get_favourite())
        self.assertEqual(self.test_drink, self.test_person.get_favourite())

    def test_get_order_as_list(self):
        self.assertEqual(self.expected_order, self.test_person.get_order_as_list())


if __name__ == '__main__':
    unittest.main()
