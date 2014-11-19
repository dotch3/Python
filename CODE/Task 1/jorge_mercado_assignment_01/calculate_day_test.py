import unittest

from functions import calculate_day


class DeterminantTest(unittest.TestCase):

    def test_day_of_burn(self):
        self.assertEqual(2, calculate_day(5,14,1985))

    def test_day_of_birthday_2014(self):
        self.assertEqual(3, calculate_day(5,14,2014))

    def test_day_today(self):
        self.assertEqual(1, calculate_day(10,27,2014))

    def test_day_near_to_today(self):
        self.assertEqual(5, calculate_day(10,31,2014))


if __name__ == '__main__':
    unittest.main()