import unittest

from source.classes.Drink import Drink


class TestDrink(unittest.TestCase):
    def setUp(self):
        self.test_drink_cold = Drink("Water","Cold")
        self.test_drink_hot = Drink("Tea","Hot")
        self.test_second_drink_cold = Drink("Water","Cold")

    def test_is_hot(self):
        self.assertTrue(self.test_drink_hot.is_hot())
        self.assertFalse(self.test_drink_cold.is_hot())

    def test_equivalence(self):
        self.assertEqual(self.test_drink_cold, self.test_second_drink_cold)
        self.assertEqual(self.test_drink_hot, self.test_drink_hot)


if __name__ == '__main__':
    unittest.main()
