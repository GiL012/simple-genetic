import random

def randomPair(besto):
	k = len(besto)
	r = random.sample(range(0,k), 2)
	r.sort()
	return r

def uniformCross(besto,bestt):
	c1,c2 = [],[]
	k = len(besto)
	for x in range(k):
		r = random.uniform(0,1)
		if(r > SWAPPROB):
			c1.append(bestt[x])
			c2.append(besto[x])
		else:
			c1.append(besto[x])
			c2.append(bestt[x])
	return ''.join(c1),''.join(c2)

def onePointFunc(besto,bestt):
	r = randomPair(besto)
	r1 = random.shuffle(r)
	c1 = besto[:r[0]] + bestt[r[0]:]
	c2 = bestt[:r[0]] + besto[r[0]:]
	return c1,c2

def crossPointFunc(besto,bestt):
	r = randomPair(besto)
	c1 = besto[:r[0]] + bestt[r[0]:r[1]] + besto[r[1]:]
	c2 = bestt[:r[0]] + besto[r[0]:r[1]] + bestt[r[1]:]
	return c1,c2

def permutationFunc(besto,bestt):
	r = randomPair(besto)
	c_1,c_2 = besto[r[0]:r[1]],bestt[r[0]:r[1]]
	ct = ''.join([x for x in bestt if x not in c_1])
	ct2 = ''.join([x for x in besto if x not in c_2])
	c1 = ct[:r[0]] + c_1 + ct[r[0]:]
	c2 = ct2[:r[0]] + c_2 + ct2[r[0]:]
	return c1,c2

crossoverTypes = { 0:uniformCross,1:onePointFunc,2:crossPointFunc,3:permutationFunc }
SWAPPROB = 0.35

if __name__ == "__main__":
	print("Input: '1234567890','0987654321'")
	print(crossoverTypes[0]('1234567890','0987654321'))
	print(crossoverTypes[1]('1234567890','0987654321'))
	print(crossoverTypes[2]('1234567890','0987654321'))
	print(crossoverTypes[3]('1234567890','0987654321'))











