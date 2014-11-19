
import unittest

from gravity import calculate_y_position

class GravityTest (unittest.TestCase):

	def test_y_position_should_be_initials_y_if_time_is_zero(self):
		y = calculate_y_position(initial_y=2, initial_speed =4, time=0)
		self.assertEqual(2, y)

	def test_y_position_should_be_1_dot_1_if_time_is_one(self):
		y = calculate_y_position(initial_y=2, initial_speed =4, time=1)
		epsylon = 1.1 - y
		self.assertTrue(epsylon < 0.00000001)



if __name__ == '__main__':
	unittest.main()