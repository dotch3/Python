class Span:


	num_instances = 0

	def __init__(self):
		Span.num_instances += 1

	@staticmethod
	def get_num_instances():
		return Span.num_instances


	@classmethod
	def get_num_instances_cm(cls):
		return cls.num_instances

	#get_num_instanes = staticmethod(get_num_instanes)#overriding its name to static


