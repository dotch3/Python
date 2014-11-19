import unittest

from advanced import Span

class StaticAndClassMethods(unittest.TestCase):

	def test_static_methods_do_not_require_an_instance(self):
		self.assertEqual(0, Span.get_num_instances())


		span = Span()
		self.assertEqual(1, Span.get_num_instances())


		span = Span()
		self.assertEqual(2, Span.get_num_instances())
		self.assertEqual(2, Span.get_num_instances_cm())






if __name__ == '__main__':
	unittest.main()





