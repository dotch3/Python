import unittest

from capicua import calculate_capicua

class CapicuaTest (unittest.TestCase):

	def test_capicua_should_return_true_for_an_empty_string(self):
		self.assertTrue(calculate_capicua(""))

	def test_capicua_should_return_true_if_string_has_only_one_character(self):
		self.assertTrue(calculate_capicua("a"))

	def test_capicua_should_return_false_if_the_string_has_two_different_characters(self):
		self.assertFalse(calculate_capicua("AB"))
		self.assertFalse(calculate_capicua("BCD#$$#DCB"))

	def test_capicua_should_return_true_if_the_string_has_equal_characters(self):
			self.assertTrue(calculate_capicua("AAAA"))
			self.assertTrue(calculate_capicua("bbbbb"))

	def test_capicua_should_return_true_if_extreme_chars_are_the_same(self):
			self.assertTrue(calculate_capicua("abcba"))
			self.assertTrue(calculate_capicua("BCDDCB"))
			self.assertTrue(calculate_capicua("BCD#$8$#DCB"))
		
if __name__ == '__main__':
	unittest.main()