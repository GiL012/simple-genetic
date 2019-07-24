
def decode(coded):
	# Implement this section 
	# ----------------------
	return int(coded)

def binRepDecode(coded,a,b):
	k = len(coded)
	c = (2**k)-1
	d = (b - a) / c
	de = dec(coded)
	print(d)
	return a + (de * d)

def dec(coded):
	k = len(coded)
	x = [int(y)*(2**(k-x)) for x,y in enumerate(coded) if x > 0]
	print(x)
	return sum(x)

if __name__ == "__main__":
	coded = "111111111111111"
	print(coded)
	print(binRepDecode(coded,0.0,20.0))