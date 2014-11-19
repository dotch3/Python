import unittest

from recursion import factorial

from recursion import factorialWhile

class RecursionTest(unittest.TestCase):

	def test_factorial_of_0_is_1(self):
		self.assertEqual(1, factorial(0))

	def test_factorial_of_2_is_2(self):
		self.assertEqual(2, factorial(2))

	def test_factorial_of_3_is_6(self):
		self.assertEqual(6, factorial(3))

	def test_factorial_of_12_is_6(self):
		self.assertEqual(479001600, factorial(12))

	def test_factorialWhile_of_0_is_1(self):
		self.assertEqual(1, factorialWhile(0))

	def test_factorialWhile_of_2_is_2(self):
		self.assertEqual(2, factorialWhile(2))

	def test_factorialWhile_of_3_is_6(self):
		self.assertEqual(6, factorialWhile(3))

	def test_factorialWhile_of_12_is_6(self):
		self.assertEqual(479001600, factorialWhile(12))
	def test_factorialWhile_Is_Big_Name(self):
		self.assertTrue(factorialWhile(120000)>100000000)


if __name__ == '__main__':
	unittest.main()



