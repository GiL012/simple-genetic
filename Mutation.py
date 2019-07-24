import random 

def flipMutation(cromosome, MUTRATE = 0.3):
	ncromosome = ''
	temp = ''
	zoo =  str.maketrans('0','1')
	ooz =  str.maketrans('1','0')
	for gen in cromosome:
		rndmut = random.random()
		temp =  gen
		if rndmut < MUTRATE:
			temp = gen.translate(zoo)
			temp = gen.translate(ooz)
		ncromosome = ncromosome + temp
	return ''.join(ncromosome)	

def perMutation(cromosome):
	pm = random.randint(2,len(cromosome)-1)
	pmm = random.randint(0,pm-1)
	crom = list(cromosome)
	gen = crom[pm]
	crom[pm] = crom[pmm]
	crom[pmm] = gen
	return ''.join(crom)

mutationType = { 0:flipMutation, 1:perMutation }

if __name__ == '__main__':
	print(flipMutation('1010101001',0.3))
	print(perMutation('1234567890'))
