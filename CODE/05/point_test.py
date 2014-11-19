import unittest

from geometry import Point
class PointTest(unittest.TestCase):





	def test_a_point_should_be_created_with_x_and_y_coordinates(self):
		my_point = Point(5 , 7)


		self.assertTrue(isinstance(my_point, Point))

	# def test_a_point_without_coordinates(self):
	# 	my_point = Point ()
		
	# 	self.assertFalse(isinstance(my_point, Point))


	def test_a_point_should_return_its_x_and_y_coordinates(self):
		my_point = Point(5 , 7)


		self.assertTrue(5, my_point.x)
		self.assertTrue(7, my_point.y)

	def test_distance_to_same_should_be_zero(self):
		my_point = Point(5 , 7)


		self.assertEqual(0 , my_point.distance_to(my_point))

	def test_distance_to_3_4_from_origin_should_be_5(self):

		my_point = Point (0 , 0)
		another_point = Point (3 , 4)

		self.assertEqual(5, my_point.distance_to(another_point))
		self.assertEqual(5, another_point.distance_to(my_point))

if __name__ == '__main__':

		unittest.main()