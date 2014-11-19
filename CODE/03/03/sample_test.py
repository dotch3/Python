import unittest


class TestSample(unittest.TestCase):

    def test_compare_values(self):
        my_value = 10

        self.assertEqual(10, my_value, "values must be equal")

if __name__ == '__main__':
    unittest.main()