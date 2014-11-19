import unittest

from diagram import Rectangle
class RectangleTest(unittest.TestCase):


	def test_a_point_should_be_created_with_x_and_y_coordinates(self):
		my_point = Point(5,7)
		my_rectangle = Rectangle(my_point,7,4)


		self.assertTrue(isinstance(my_rectangle, Rectangle))



if __name__ == '__main__':

		unittest.main()