from unittest.case import TestCase
from unittest.mock import patch

from numbers import Number

from decimal import Decimal

from forcetype import forcetype, WrongParameterTypeException, WrongReturnTypeException


@forcetype
def add_number(op1: Number, op2: Number)-> Number:
	"""
	add
	:param op1:
	:param op2:
	:return:
	"""
	result = op1 + op2

	if result > 999:
		return str(result)

	return op1 + op2

@forcetype
def add_decimal(op1: Decimal, op2: Decimal)-> Decimal:
	"""
	add
	:param op1:
	:param op2:
	:return:
	"""

	result = op1 + op2

	if result > 999:
		return float(result)

	return result

@forcetype
def add_float(op1: float, op2: float)-> float:
	"""
	add
	:param op1:
	:param op2:
	:return:
	"""
	result = op1 + op2

	if result > 999:
		return int(result)

	return  result

@forcetype
def convert_to_decimal(value: int) -> Decimal:
	"""
	convert_to_decimal
	:param value:
	:return:
	"""

	if value == 9:
		return value

	return Decimal(value)


class TestNumericTypes(TestCase):

	def setUp(self):
		pass

	def tearDown(self):
		pass

	def test_numeric_success(self):

		self.assertEquals(add_number(1.1, 3), 4.1)

		self.assertEquals(add_number(4, 3.9), 7.9)

		self.assertEquals(add_decimal(Decimal(3), Decimal(9)), Decimal(12))

		self.assertEquals(add_decimal(Decimal(1), Decimal(5)), Decimal('6'))

		self.assertEquals(add_float(.5, .9), 1.4)

		self.assertEquals(add_float(1.0, 2.0), 3.0)

	def test_numeric_parametes(self):

		self.assertRaises(WrongParameterTypeException, lambda: add_number('1', 1))

		self.assertRaises(WrongParameterTypeException, lambda: add_decimal(Decimal(1), 1))

		self.assertRaises(WrongParameterTypeException, lambda: add_float(1000, 1.2))

		self.assertRaises(WrongParameterTypeException, lambda: convert_to_decimal(3.))


	def test_numeric_return(self):

		self.assertRaises(WrongReturnTypeException, lambda: add_number(1.2, 1000))

		self.assertRaises(WrongReturnTypeException, lambda: add_decimal(Decimal(10000), Decimal(1)))

		self.assertRaises(WrongReturnTypeException, lambda: add_float(10000.0, 1.0))

		self.assertRaises(WrongReturnTypeException, lambda: convert_to_decimal(9))

