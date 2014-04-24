def xor(x, y):
	"""Returns a Boolean resulting in using the XOR method on x and y.\n
	XOR is equivalent to an OR statement that returns False if both conditions are True.\n
	Examples:
	xor(0, 0) --> False
	xor(1, 0) --> True
	xor(1, 1) --> False
	"""
	return bool(x) != bool(y)

def xnor(x, y):
	"""Returns a Boolean resulting in using the XNOR method on x and y.\n
	XNOR is the negated form of the XOR statement.\n
	Examples:
	xnor(0, 0) --> True
	xnor(1, 0) --> False
	xnor(1, 1) --> True
	"""
	return bool(x) == bool(y)

def nand(x, y):
	"""Returns a Boolean resulting in using the NAND method on x and y.\n
	NAND is the negated form of the AND statement.\n
	Examples:
	nand(0, 0) --> True
	nand(1, 0) --> True
	nand(1, 1) --> False
	"""
	return not (x and y)

def nor(x, y):
	"""Returns a Boolean resulting in using the NOR method on x and y.\n
	NOR is the negated form of the OR statement.\n
	Examples:
	nor(0, 0) --> True
	nor(1, 0) --> False
	nor(1, 1) --> False
	"""
	return not (x or y)