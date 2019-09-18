import unittest
import source.helpers.devito as devito

class TestDevito(unittest.TestCase):
    def test_devito_time(self):
        self.assertEqual(devito.danny, devito.devito_time())


if __name__ == '__main__':
    unittest.main()
