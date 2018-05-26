def foo(*args):
	print(type(args))
	for i in args:
		print("Hello, {}!".format(i))


input = ["Alex", "Ivan", "Lion"]
foo(*input)


def f(**kwargs):
	print(type(kwargs)) # dict
	for key, val in kwargs.items():
		print("{}: {}".format(key, val))

