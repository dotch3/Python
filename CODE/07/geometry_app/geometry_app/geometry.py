import math

class Point(object):

    z = 5
    
    def __init__(self, x, y):
        self.x = x
        self.y = y        

    def distance_to(self, point):
        return math.sqrt((point.y - self.y) ** 2 + (point.x - self.x) ** 2)

    def __eq__(self, other_point):
        return self.x == other_point.x and self.y == other_point.y



class Rectangle(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

        self.top_left = Point(x, y + height)

        self.bottom_right = Point(x + width, y)
        

    def contains(self, shape):
        return (self.x <= shape.x <= self.x + self.width) and (self.y <= shape.y <= self.y + self.height)

    def perimeter(self):
        return 2 * self.width + 2 * self.height

    def __eq__(self, other_rectangle):
        return self.x == other_rectangle.x and self.y == other_rectangle.y and self.width == other_rectangle.width and self.height == other_rectangle.height

    def intersect(self, other_rectangle):
        top_left_x = max(self.top_left.x, other_rectangle.top_left.x)
        top_left_y = min(self.top_left.y, other_rectangle.top_left.y)

        bottom_right_x = min(self.bottom_right.x, other_rectangle.bottom_right.x)
        bottom_right_y = max(self.bottom_right.y, other_rectangle.bottom_right.y)

        width = bottom_right_x - top_left_x
        height = top_left_y - bottom_right_y

        #print ("[%s, %s, %s, %s]" % (top_left_x, bottom_right_y, width, height))

        if (width < 0 or height < 0):
            return None
        return Rectangle(top_left_x, bottom_right_y, width, height)


    def join(self, other_rectangle):
        top_left_x = min(self.top_left.x, other_rectangle.top_left.x)
        top_left_y = max(self.top_left.y, other_rectangle.top_left.y)

        bottom_right_x = max(self.bottom_right.x, other_rectangle.bottom_right.x)
        bottom_right_y = min(self.bottom_right.y, other_rectangle.bottom_right.y)

        width = bottom_right_x - top_left_x
        height = top_left_y - bottom_right_y

        print ("[%s, %s, %s, %s]" % (top_left_x, bottom_right_y, width, height))

        if (width < 0 or height < 0):
            return None
        return Rectangle(top_left_x, bottom_right_y, width, height)

# class Square(Rectangle):
#     def __init__(self, x, y, side):
#         Rectangle.__init__(self, x, y, side, side)

class Square:
    def __init__(self, x, y, side):
        self._rect = Rectangle(x, y, side, side)

    def perimeter(self):
        return self._rect.perimeter()