import unittest

def generate_matrix(size):
    return  [[1]]


class MatricesTest(unittest.TestCase):

    def test_generate_matrix_of_size_1(self):
        self.assertEqual([[1]], generate_matrix(1))

    def test_generate_matrix_of_size_2(self):
        self.assertEqual([[1, 3], [2, 4]], generate_matrix(2))


if __name__ == '__main__':
    unittest.main()