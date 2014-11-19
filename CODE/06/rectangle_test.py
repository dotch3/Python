import unittest

from geometry import Rectangle
from geometry import Point

class RectangleTest(unittest.TestCase):

	# def test_rectangle_can_be_created_with_four_params_x_y_w_h(self):
	# 	rect = Rectangle(0 , 0 , 10 , 5)

	# 	self.assertTrue(isinstance(rect, Rectangle))


	# def test_rectangle_contains_a_point_with_same_coordinates_as_its_x_y_attributes(self):
	# 	point  = Point(0 , 0)
	# 	rect = Rectangle (0 , 0 , 4 , 5)

	# 	self.assertTrue(rect.contains(point))

		
	# def test_contains_should_return_false_if_point_in_x_coordinates_is_outside_of_the_rectangle(self):
	# 	point = Point (-1, 0)
	# 	rect = Rectangle (0 , 0 , 4 , 5)

	# 	self.assertFalse(rect.contains(point))



	# def test_contains_should_return_false_if_point_in_y_coordinates_is_outside_of_the_rectangle(self):
	# 	point = Point (0, -1)
	# 	rect = Rectangle (0 , 0 , 4 , 5)

	# 	self.assertFalse(rect.contains(point))



	# def test_point_can_be_compared_with_equals_operator(self):
	# 	point = Point(0 , 0)
		

	# 	self.assertTrue(point == Point(0 , 0))

	# def test_point_should_be_different_to_other_point_if_coordinates_are_not_the_same(self):
	# 	point = Point(0 , 0)

	# 	self.assertFalse(point == Point(1 , 2))
	# 	self.assertFalse(point == Point(0 , 2))


	def test_contains2_should_return_true_if_the_figure_to_evaluate_is_a_rectangle_inside_the_first_rectangle(self):
		main_rect = Rectangle (0, 0 , 6 , 8)
		other_rect = Rectangle (1 , 3 , 2 , 3)


		self.assertTrue(main_rect.contains2(other_rect))



	def test_contains2_should_return_False_if_point_entered_is_outside_of_the_rectangle(self):
		point = Point (0, -1)
		main_rect = Rectangle (0 , 0 , 4 , 5)

		self.assertFalse(main_rect.contains2(point))

	def test_contains2_should_return_True_if_point_entered_is_inside_of_the_rectangle(self):
		point = Point (0, 4)
		main_rect = Rectangle (0 , 0 , 5 , 12)

		self.assertTrue(main_rect.contains2(point))


	def test_contains2_should_return_True_if_the_figure_to_evaluate_is_a_rectangle_inside_of_the_first_rectangle(self):
		main_rect = Rectangle (0, 0 , 6 , 8)
		other_rect = Rectangle (1 , 3 , 2 , 3)


		self.assertTrue(main_rect.contains2(other_rect))


	def test_contains2_should_return_false_if_the_figure_to_evaluate_is_a_rectangle_outside_of_the_first_rectangle(self):
		main_rect = Rectangle (0, 0 , 6 , 8)
		other_rect = Rectangle (1 , 3 , 8 , 3)


		self.assertFalse(main_rect.contains2(other_rect))



		



if __name__ == '__main__':
	unittest.main()








