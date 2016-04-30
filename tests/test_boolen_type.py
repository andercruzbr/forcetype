from unittest.case import TestCase

from forcetype import forcetype, WrongParameterTypeException, WrongReturnTypeException


@forcetype
def func_and(op1: bool, op2: bool) -> bool:
	"""
	func_and
	:param op1:
	:param op2:
	:return:
	"""
	return op1 and op2


@forcetype
def func_or(op1: bool, op2: bool) -> bool:
	"""
	func_or
	:param op1:
	:param op2:
	:return:
	"""

	return int(op1 or op2)


class TestBooleanType(TestCase):

	def setUp(self):
		pass

	def tearDown(self):
		pass

	def test_boolean_success(self):

		self.assertEquals(func_and(True, False), False)

		self.assertEquals(func_and(True, True), True)

		self.assertEquals(func_and(False, True), False)

		self.assertEquals(func_and(False, False), False)

		self.assertNotEqual(func_and(True, False), True)

		self.assertNotEqual(func_and(True, True), False)

		self.assertNotEqual(func_and(False, True), True)

		self.assertNotEqual(func_and(False, False), True)

	def test_boolean_parametes(self):

		self.assertRaises(WrongParameterTypeException, lambda: func_and(True, 1))

		self.assertRaises(WrongParameterTypeException, lambda: func_and(0, 1))

		self.assertRaises(WrongParameterTypeException, lambda: func_and(0, False))

	def test_boolean_return(self):

		self.assertRaises(WrongReturnTypeException, lambda: func_or(True, False))

		self.assertRaises(WrongReturnTypeException, lambda: func_or(True, True))

		self.assertRaises(WrongReturnTypeException, lambda: func_or(False, False))


