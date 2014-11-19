import unittest

from geometry import Rectangle
from geometry import Point


class RectangleTest(unittest.TestCase):

    # def test_rectangle_can_be_created_with_four_params_x_y_width_and_height(self):
    #     rect = Rectangle(0, 0, 10, 5)

    #     self.assertTrue(isinstance(rect, Rectangle))

    # def test_rectangle_contains_a_point_with_same_coordinates_as_its_x_y_attributes(self):
    #     point = Point(0, 0)
    #     rect = Rectangle(0, 0, 4, 5)

    #     self.assertTrue(rect.contains(point))

    # def test_contains_should_return_false_if_point_is_outside_of_the_rectangle(self):
    #     point = Point(-1, 0)
    #     rect = Rectangle(0, 0, 4, 5)

    #     self.assertFalse(rect.contains(point))
    #     self.assertFalse(rect.contains(Point(0, -1)))

    # def test_perimeter_should_return_a_positive_value(self):
    #     rect = Rectangle(0, 0, 4, 5)

    #     self.assertEquals(18, rect.perimeter())

    # def test_rectangle_can_compare_using_equals_operator(self):
    #     rect = Rectangle(0, 0, 1, 1)

    #     self.assertEquals(Rectangle(0 ,0, 1, 1), rect)

    #     self.assertFalse(Rectangle(0, 1, 1, 1) == rect)

    # def test_intersect_returns_none_if_there_is_no_intersection(self):
    #     rect = Rectangle(0, 0, 5, 6)

    #     self.assertEquals(None, rect.intersect(Rectangle(-3, -4, 1, 2)))


    # def test_intersect_should_return_the_inner_rectangle_if_it_is_completely_inside_the_bigger_rectangle(self):
    #     small = Rectangle(2, 2, 1, 3)
    #     big = Rectangle(-1, -1, 6, 8)

    #     self.assertEquals(small, small.intersect(big))
    #     self.assertEquals(small, big.intersect(small))

    # def test_intersect_returns_smaller_rectangle_if_there_is_overlap(self):
    #     intersection = Rectangle(3, 2, 4, 3)

    #     first_rect = Rectangle(2, 2, 5, 4)
    #     second_rect = Rectangle(3, 1, 5, 4)

    #     self.assertEquals(intersection, first_rect.intersect(second_rect))


    def test_join_two_rectangles_overlapped(self):
        joined = Rectangle(2 , 1 , 6 , 5)
        joined2 = Rectangle(1 , 2 , 8, 15)

        first_rect = Rectangle (2, 2, 5, 4)
        second_rect = Rectangle (3, 1, 5, 4)
        third_rect = Rectangle (1, 5 , 8 , 12)

        self.assertEquals(joined,  first_rect.join(second_rect))
        self.assertEquals(joined2,  first_rect.join(third_rect))


if __name__ == '__main__':
    unittest.main()