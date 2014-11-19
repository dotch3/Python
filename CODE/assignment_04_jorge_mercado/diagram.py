import math
class Rectangle (object):

	def __init__(self, param_x, param_y ,param_weight , param_height):
		self.param_x = param_x
		self.param_y = param_y
		self.weight = param_weight
		self.param_height = param_height
		
	def contains_point(self,point):

		self.verify_has_point(point)


class Point (object):

	def __init__(self, param_x ,param_y):
		self.x = param_x
		self.y = param_y

	
	def distance_to(self,point):

		x = point.x
		y = point.y


		res = math.sqrt((y - self.y)**2 + (x - self.x)**2)


		return res