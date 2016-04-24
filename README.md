# forcetype

This project born from some of my needs in validate types of functions/methods parameters. Usually, developers do that inside of the function using if statements.

In this project I aim another way to do that using decorators and function annotations, as can seen below.

```
@forcetype
def add(op1: int, op2: int) -> int:
	"""
	Add
	:param op1:
	:param op2:
	:return:
	"""
	return op1 + op2
```

The forcetype decorator require that all parameters be of the same type as defined in the function, including the return of function.
