from unittest.case import TestCase

from forcetype import forcetype, WrongParameterTypeException, WrongReturnTypeException


@forcetype
def concat_str(str1: str, str2: str) -> str:
	"""
	concat_str
	:param str1:
	:param str2:
	:return:
	"""
	return str1 + str2

@forcetype
def foo_str(str1: str, str2: str) -> str:
	"""
	concat_str
	:param str1:
	:param str2:
	:return:
	"""
	return int(str1 + str2)


class TestStringTypes(TestCase):

	def setUp(self):
		pass

	def tearDown(self):
		pass

	def test_str_success(self):

		self.assertEquals(concat_str('2', '1'), '21')

		self.assertEquals(concat_str('a', 'b'), 'ab')

		self.assertEquals(concat_str('y', 'z'), 'yz')

		self.assertNotEqual(concat_str('2', '1'), '12')

		self.assertNotEqual(concat_str('a', 'b'), 'ba')

		self.assertNotEqual(concat_str('y', 'z'), 'zy')

	def test_str_parametes(self):

		self.assertRaises(WrongParameterTypeException, lambda: concat_str('a', 1))

		self.assertRaises(WrongParameterTypeException, lambda: concat_str('b', False))

		self.assertRaises(WrongParameterTypeException, lambda: concat_str(0, 'False'))

	def test_boolean_return(self):

		self.assertRaises(WrongReturnTypeException, lambda: foo_str('1', '2'))

		self.assertRaises(WrongReturnTypeException, lambda: foo_str('10', '92'))

		self.assertRaises(WrongReturnTypeException, lambda: foo_str('23', '65'))

