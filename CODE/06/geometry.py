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
		

		# Receives a figure that is evaluated if this is a Point or a Rectangle
	def contains2(self,my_figure): 
		if(isinstance(my_figure, Rectangle)):
			return (self.x <= my_figure.x <= self.x + self.w) and (self.y <= my_figure.y <= self.y + self.h) and (self.x <= my_figure.x + my_figure.w <= self.x + self.w) and (self.y <= my_figure.y + my_figure.h <= self.y + self.h)
			

		elif (isinstance(my_figure,Point)):
			return  (self.x <= my_figure.x <= self.x + self.w) and (self.y <= my_figure.y <= self.y + self.h)
