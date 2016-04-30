from unittest.case import TestCase

from numbers import Number

from decimal import Decimal

from forcetype import forcetype


@forcetype
def add(op1: Number, op2: Number)-> Number:
	"""
	add
	:param op1:
	:param op2:
	:return:
	"""
	return op1 + op2

@forcetype
def add_decimal(op1: Decimal, op2: Decimal)-> Decimal:
	"""
	add
	:param op1:
	:param op2:
	:return:
	"""
	return op1 + op2

@forcetype
def add_float(op1: float, op2: float)-> float:
	"""
	add
	:param op1:
	:param op2:
	:return:
	"""
	return op1 + op2


def convert_to_decimal(value: 1) -> Decimal:
	"""
	convert_to_decimal
	:param value:
	:return:
	"""
	return Decimal(value)


class TestNumericTypes(TestCase):

	def setUp(self):
		pass

	def tearDown(self):
		pass

	def test_01(self):
		pass