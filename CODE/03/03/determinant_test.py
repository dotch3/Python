import unittest

from functions import determinant


class DeterminantTest(unittest.TestCase):

    def test_determinant_is_zero_if_a_b_and_c_are_zero(self):
        self.assertEqual(0, determinant(0, 0, 0))

    def test_determinant_is_positive_if_b_x_b_is_greater_than_4_times_a_and_c(self):
        self.assertEqual(41, determinant(1, 5, -4))

    def test_determinant_is_negative_if_b_is_zero_and_both_a_and_c_are_positive(self):
        self.assertEqual(-8, determinant(1, 0, 2))


if __name__ == '__main__':
    unittest.main()