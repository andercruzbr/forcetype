from unittest.case import TestCase

from forcetype import forcetype


class Point:
	"""
	Point class
	"""
	def __init__(self, x=None, y=None):
		"""
		Constructor
		:param x:
		:param y:
		"""
		self.x = x
		self.y = y

	def __add__(self, other):
		"""
		Operator+
		:param other:
		:return:
		"""
		point = Point()
		point.x = self.x + other.x
		point.y = self.y + other.y
		return point

	def __eq__(self, other):
		"""
		Operator==
		:param other:
		:return:
		"""
		return self.x == other.x and self.y == other.y


@forcetype
def add(op1: Point, op2: Point) -> Point:
	"""
	Add
	:param op1:
	:param op2:
	:return:
	"""
	return op1 + op2


class TestComplexType(TestCase):
	"""
	TestComplexType
	"""

	def setUp(self):
		self.point1 = Point(1, 2)

		self.point2 = Point(2, 4)

		self.point3 = Point(3, 6)

	def tearDown(self):
		pass

	def test_01(self):

		self.assertEquals(add(self.point1, self.point2), self.point3)

	def test_02(self):
		pass
		# self.assertEquals(add(1, '1'), 2)
