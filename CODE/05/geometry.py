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