#!/usr/bin/env python3
#-*- coding: iso-8859-1 -*-


import inspect
from functools import wraps
# import functools
# import re


def forcetype(method):
	"""

	:param method:
	:return:
	"""

	argspec = inspect.getfullargspec(method)

	if not argspec.annotations:
		# raise Exception("All parameters need be typed")
		return method

	# default_arg_count = len(argspec.defaults or [])
	# non_default_arg_count = len(argspec.args) - default_arg_count
	# method_name = method.__name__
	# kwarg_defaults = argspec.kwonlydefaults or {}

	type_list = []
	param_list = []

	for n, v in argspec.annotations.items():

		type_list.append(v)
		param_list.append(n)

	def inner(*args, **kwargs):
		"""

		:param args:
		:param kwargs:
		:return:
		"""

		for i, v in enumerate(args):

			if not isinstance(v, type_list[i]):
				raise Exception("Param %s need be a %s type" % (param_list[i], type_list[i]))

		result = method(*args, **kwargs)

		if not isinstance(result, type_list[-1]):
			raise Exception('Type Error')

		return result

		return method(*args, **kwargs)

	return inner
