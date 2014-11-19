import unittest

from geometry import Circle
from geometry import Point

class RectangleTest(unittest.TestCase):

	def test_circle_can_be_created_with_3_params_x_y_r(self):
		circ = Circle(0 , 0 , 5)

		self.assertTrue(isinstance(circ, Circle))

	def test_max_size_for_a_Circle(self):
		circ = Circle(0 , 0 ,4)

		self.assertEquals(8, circ.circle_size())

	def test_max_x_coordinates_for_a_Circle(self):
		circ = Circle(2, 3 ,8)
		
		self.assertEquals(18, circ.circle_max_x_position())

	def test_max_y_coordinates_for_a_Circle(self):
		circ = Circle(1, 5, 4)
		
		self.assertEquals(13, circ.circle_max_y_position())

	def test_new_rectangle_from_circle(self):
		circ = Circle(1 , 5, 3)
		circ_new_rectangle = circ.circle_new_circle_to_rectangle()

		self.assertTrue(circ_new_rectangle.x, circ.circle_max_x_position())
		self.assertTrue(circ_new_rectangle.y, circ.circle_max_y_position())



if __name__ == '__main__':
	unittest.main()


