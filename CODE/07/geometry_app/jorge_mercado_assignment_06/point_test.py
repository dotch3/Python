import unittest

from geometry import Point

class PointTest(unittest.TestCase):

    def test_a_point_should_be_created_with_x_and_y_coordinates(self):
        my_point = Point(5, 7)

        self.assertTrue(isinstance(my_point, Point))

    def test_a_point_should_return_its_x_and_y_coordinates(self):
        my_point = Point(5, 7)

        self.assertEqual(5, my_point.x)
        self.assertEqual(7, my_point.y)

    def test_distance_to_same_point_should_be_zero(self):
        my_point = Point(5, 7)

        self.assertEqual(0, my_point.distance_to(my_point))

    def test_distance_to_3_4_from_origin_should_be_5(self):
        origin = Point(0, 0)
        other_point = Point(3, 4)
        

        self.assertEqual(5, origin.distance_to(other_point))
        self.assertEqual(5, other_point.distance_to(origin))

    def test_point_can_be_compared_with_equals_operator(self):
        point= Point(0, 0)

        self.assertTrue(point == Point(0, 0))

    def test_point_should_be_different_to_other_point_if_coordinates_are_not_the_same(self):
        point= Point(0, 0)

        self.assertFalse(point == Point(0, 1))
        self.assertFalse(point == Point(1, 0))
        

if __name__ == '__main__':
    unittest.main()