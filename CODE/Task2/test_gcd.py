import unittest

from gcd import calculate_gcd


class DeterminantTest(unittest.TestCase):

    def test_gcd_should_be_8(self):
        self.assertEqual(8, calculate_gcd(56,8))
        
    def test_gcd_should_be_0(self):
        self.assertEqual(0, calculate_gcd(0,8))

if __name__ == '__main__':
    unittest.main()