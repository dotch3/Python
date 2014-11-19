import unittest



from geometry import Rectangle
from geometry import Square

class SquareTest(unittest.TestCase):

	def test_square_is_a_derivative_of_rectangle(self):

		square =Square(0 , 0 , 5)

		self.assertTrue(isinstance(square, Rectangle))
		self.assertTrue(isinstance(square, Square))


	def test_perimeter_returns_four_times_its_side(self):
		square = Square(0 , 0 , 5)

		self.assertEqual(20, square.perimeter())

		square.width =3

		self.assertEqual(20, square.perimeter())





if __name__ == '__main__':
	unittest.main()

