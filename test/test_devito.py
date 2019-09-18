import unittest
import helpers.devito

class TestDevito(unittest.TestCase):
    def test_devito_time(self):
        self.assertEqual(helpers.devito.danny, helpers.devito.devito_time())


if __name__ == '__main__':
    unittest.main()
