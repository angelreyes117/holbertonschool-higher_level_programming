import unittest
from 6-max_integer import max_integer

class TestMaxInteger(unittest.TestCase):
    def test_max(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

if __name__ == "__main__":
    unittest.main()
