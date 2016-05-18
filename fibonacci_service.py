#!/usr/bin/python
#  python -V
#	Python 2.7.5


def valid_input(i):
	try:
		float(i) # for int, long and float
	except ValueError:
		try:
			complex(i) # for complex
		except ValueError:
			return False
	if i == int(i):
		return True
	return False


def fib():
	x, y = 0, 1
	while 1:
		yield x
		x, y = y, x + y


def fibonacci(fib_length):
	if not valid_input(fib_length):
		raise ValueError("INVALID Entry:  not an integer")

	if fib_length < 1:
		raise ValueError("INVALID Input - Enter a value > 0 ") 	

	series = []
	x = fib()
	for i in range(fib_length):
		series.append(x.next())
	return series
