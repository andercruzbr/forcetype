from unittest.case import TestCase

from forcetype import forcetype


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
def subtract(op1, op2):
	"""

	:param op1:
	:param op2:
	:return:
	"""
	return op1 - op2


class TestBasic(TestCase):

	def setUp(self):
		pass

	def tearDown(self):
		pass

	def test_01(self):

		self.assertEquals(add(1, 1), 2)

	def test_02(self):

		self.assertEquals(add(1, 1), 2)

	def test_03(self):
		self.assertEquals(subtract(1, 1), 0)