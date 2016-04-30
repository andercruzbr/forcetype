from unittest.case import TestCase

from forcetype import forcetype, WrongParameterTypeException, TypesNotDefinedException, WrongReturnTypeException


@forcetype
def add(op1: int, op2: int) -> int:
	"""
	Add
	:param op1:
	:param op2:
	:return:
	"""
	return op1 + op2


@forcetype
def subtract(op1: int, op2: int) -> int:
	"""

	:param op1:
	:param op2:
	:return:
	"""
	return op1 - op2


@forcetype
def multiple(op1: int, op2: int) -> int:
	"""

	:param op1:
	:param op2:
	:return:
	"""
	return float(op1 * op2)


class TestBasic(TestCase):

	def setUp(self):
		pass

	def tearDown(self):
		pass

	def test_01(self):

		self.assertEquals(add(1, 1), 2)

	def test_02(self):

		self.assertEquals(subtract(3, 1), 2)

	def test_exceptions(self):

		self.assertRaises(WrongParameterTypeException, lambda: subtract(1, '1'))

		self.assertRaises(WrongParameterTypeException, lambda: subtract(1, '1'))

		self.assertRaises(WrongParameterTypeException, lambda: subtract(1.0, 1))

		self.assertRaises(WrongReturnTypeException, lambda: multiple(2, 4))






