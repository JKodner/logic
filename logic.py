def xor(x, y, bi=False):
	"""Returns a Boolean resulting in using the XOR method on x and y.

	XOR is equivalent to an OR statement that returns False if both conditions are True.
	
	Note: If x and y are integers, and the 'bi' parameter is True, this function will
	return a binary representation of both numbers being acted upon by the XOR method.

	Note: The 'bi' parameter defaults to False.
	
	Examples:
	xor(0, 0) --> False
	xor(1, 0) --> True
	xor(1, 1) --> False
	"""
	if bi in [True, False]:
		if bi == False:
			return bool(x) != bool(y)
		else:
			if isinstance(x, int) and isinstance(y, int):
				return x ^ y
			else:
				raise ValueError("Invalid value for binary calculation.")
	else:
		raise ValueError("Invalid value for 'bi' parameter.")

def xnor(x, y, bi=False):
	"""Returns a Boolean resulting in using the XNOR method on x and y.

	XNOR is the negated form of the XOR statement.

	Note: If x and y are integers, and the 'bi' parameter is True, this function will
	return a binary representation of both numbers being acted upon by the XNOR method.

	Note: The 'bi' parameter defaults to False.
	
	Examples:
	xnor(0, 0) --> True
	xnor(1, 0) --> False
	xnor(1, 1) --> True
	"""
	if bi in [True, False]:
		if bi == False:
			return bool(x) == bool(y)
		else:
			if isinstance(x, int) and isinstance(y, int):
				x, y = bin(x), bin(y)
				if len(x) > len(y):
					x = "0b" + x[-(len(y) - 2):]
				elif len(y) > len(x):
					y = "0b" + y[-(len(x) - 2):]
				new = ['0', 'b']
				keys = zip(x, y)[2:]
				for i in keys:
					i = map(int, i)
					a, b = i
					if bool(a) == bool(b):
						new.append("1")
					else:
						new.append("0")
				return int("".join(new), 2)
			else:
				raise ValueError("Invalid value for binary calculation.")
	else:
		raise ValueError("Invalid value for 'bi' parameter.")

def nand(x, y, bi=False):
	"""Returns a Boolean resulting in using the NAND method on x and y.
	
	NAND is the negated form of the AND statement.

	Note: If x and y are integers, and the 'bi' parameter is True, this function will
	return a binary representation of both numbers being acted upon by the NAND method.

	Note: The 'bi' parameter defaults to False.
	
	Examples:
	nand(0, 0) --> True
	nand(1, 0) --> True
	nand(1, 1) --> False
	"""
	if bi in [True, False]:
		if bi == False:
			return not (x and y)
		else:
			if isinstance(x, int) and isinstance(y, int):
				x, y = bin(x), bin(y)
				if len(x) > len(y):
					x = "0b" + x[-(len(y) - 2):]
				elif len(y) > len(x):
					y = "0b" + y[-(len(x) - 2):]
				new = ['0', 'b']
				keys = zip(x, y)[2:]
				for i in keys:
					i = map(int, i)
					a, b = i
					if not (a and b):
						new.append("1")
					else:
						new.append("0")
				return int("".join(new), 2)
			else:
				raise ValueError("Invalid value for binary calculation.")
	else:
		raise ValueError("Invalid value for 'bi' parameter.")

def nor(x, y, bi=False):
	"""Returns a Boolean resulting in using the NOR method on x and y.

	NOR is the negated form of the OR statement.

	Note: If x and y are integers, and the 'bi' parameter is True, this function will
	return a binary representation of both numbers being acted upon by the NOR method.

	Note: The 'bi' parameter defaults to False.
	
	Examples:
	nor(0, 0) --> True
	nor(1, 0) --> False
	nor(1, 1) --> False
	"""
	if bi in [True, False]:
		if bi == False:
			return not (x or y)
		else:
			if isinstance(x, int) and isinstance(y, int):
				x, y = bin(x), bin(y)
				if len(x) > len(y):
					x = "0b" + x[-(len(y) - 2):]
				elif len(y) > len(x):
					y = "0b" + y[-(len(x) - 2):]
				new = ['0', 'b']
				keys = zip(x, y)[2:]
				for i in keys:
					i = map(int, i)
					a, b = i
					if not (a or b):
						new.append("1")
					else:
						new.append("0")
				return int("".join(new), 2)
			else:
				raise ValueError("Invalid value for binary calculation.")
	else:
		raise ValueError("Invalid value for 'bi' parameter.")