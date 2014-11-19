import math
class Point (object):

	def __init__(self, param_x ,param_y):
		self.x = param_x
		self.y = param_y

	
	def distance_to(self,point):

		x = point.x
		y = point.y


		res = math.sqrt((y - self.y)**2 + (x - self.x)**2)


		return res

	def contains2(self,my_figure): 
		if(isinstance(my_figure, Rectangle)):
			return (self.x <= my_figure.x <= self.x + self.w) and (self.y <= my_figure.y <= self.y + self.h) and (self.x <= my_figure.x + my_figure.w <= self.x + self.w) and (self.y <= my_figure.y + my_figure.h <= self.y + self.h)
			

		elif (isinstance(my_figure,Point)):
			return  (self.x <= my_figure.x <= self.x + self.w) and (self.y <= my_figure.y <= self.y + self.h)



	def __eq__(self, other_point): # will overwrite the logic to use the "==" operator
		return self.x == other_point.x and self.y == other_point.y


class Rectangle (object):

	def __init__(self, x, y, w, h):
		self.x = x
		self.y = y
		self.w = w
		self.h = h


	def contains(self, point):
		return (self.x <= point.x <= self.x + self.w) and (self.y <= point.y <= self.y + self.h)


	def contains2(self,my_figure): 
		if(isinstance(my_figure, Rectangle)):
			return (self.x <= my_figure.x <= self.x + self.w) and (self.y <= my_figure.y <= self.y + self.h) and (self.x <= my_figure.x + my_figure.w <= self.x + self.w) and (self.y <= my_figure.y + my_figure.h <= self.y + self.h)
			

		elif (isinstance(my_figure,Point)):
			return  (self.x <= my_figure.x <= self.x + self.w) and (self.y <= my_figure.y <= self.y + self.h)



	def perimeter(self):
		return 2 * self.w + 2 *  self.h


class Square(Rectangle):# class square inheritance from rectangle

	# def __init__(self, x, y, side):
	# 	Rectangle.__init__(self,x ,y, side, side)# obtaining value from the inheritance of rectangle

	def __init__(self, x, y, side):
		self._rect = Rectangle(x, y, side, side)

	def perimeter(self):
		return self._rect.perimeter()


class Circle(object):

	def __init__(self,x, y, r):
		self.x = x
		self.y = y
		self.r = r

	def circle_size(self):
		return 2 * self.r

	def circle_max_x_position(self):

		return self.x + 2 * self.r

	def circle_max_y_position(self):
		return self.y + 2 * self.r

	def circle_new_circle_to_rectangle(self):
		self.x = self.circle_max_x_position()
		self.y = self.circle_max_y_position()
		return self


