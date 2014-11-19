import unittest

from geometry import Rectangle
from geometry import Square
from geometry import Point
from geometry import Circle

class RectangleTest(unittest.TestCase):

	def test_rectangle_can_be_created_with_four_params_x_y_w_h(self):
		rect = Rectangle(0 , 0 , 10 , 5)

		self.assertTrue(isinstance(rect, Rectangle))


	def test_rectangle_contains_a_point_with_same_coordinates_as_its_x_y_attributes(self):
		point  = Point(0 , 0)
		rect = Rectangle (0 , 0 , 4 , 5)

		self.assertTrue(rect.contains(point))

		
	def test_contains_should_return_false_if_point_in_x_coordinates_is_outside_of_the_rectangle(self):
		point = Point (-1, 0)
		rect = Rectangle (0 , 0 , 4 , 5)

		self.assertFalse(rect.contains(point))



	def test_contains_should_return_false_if_point_in_y_coordinates_is_outside_of_the_rectangle(self):
		point = Point (0, -1)
		rect = Rectangle (0 , 0 , 4 , 5)

		self.assertFalse(rect.contains(point))



	def test_point_can_be_compared_with_equals_operator(self):
		point = Point(0 , 0)
		

		self.assertTrue(point == Point(0 , 0))

	def test_point_should_be_different_to_other_point_if_coordinates_are_not_the_same(self):
		point = Point(0 , 0)

		self.assertFalse(point == Point(1 , 2))
		self.assertFalse(point == Point(0 , 2))


	def test_permiter_should_return_a_positive_value(self):
		rect = Rectangle(0 , 0 , 4 , 5)

		self.assertEquals(18, rect.perimeter())


	def test_rectangle_contains_a_circle_totally(self):
		rect = Rectangle(0 , 0 , 10 , 15)
		circ = Circle ( 2, 3 , 4)
		new_rectangle = Rectangle(circ.x, circ.y, 2 * circ.r, 2 * circ.r)

		self.assertTrue(rect.contains2(new_rectangle))


	def test_return_false_because_the_rectangle_doesnot_contains_a_circle(self):
		rect = Rectangle(0 , 0 , 10 , 15)
		circ = Circle ( 2, 8 , 4)
		new_rectangle = Rectangle(circ.x, circ.y, 2 * circ.r, 2 * circ.r)

		self.assertFalse(rect.contains2(new_rectangle))




if __name__ == '__main__':
	unittest.main()








