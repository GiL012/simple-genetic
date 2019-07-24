import random
from FitnessF import ffunction

FILLVALUE = 5
SEPARATOR = ','
NEWLINE = '\n'
PPLFILE = 'population.in'

class gPopulation:
	def __init__(self,sizeC):
		self.sizeC = sizeC
		self.units = []
	def addUnits(self,unit):
		self.units.append(unit)
	def unitsFitness(self):
		return [ffunction(x) for x in self.units]

def checkFile(gen):
	try:
		f = open(PPLFILE,'r')
	except FileNotFoundError:
		f = open(PPLFILE,'w')
		fv = range(FILLVALUE)
		for line in fv:
			d = random.randint(10**(gen-1),(10**gen)-1)
			if(FILLVALUE-1 > line):
				sd = str(d) + SEPARATOR
			else:
				sd = str(d)
			f.write(sd)
		f.close()
		f = checkFile(gen)
	return f

def newPopulation(pop):
	f = open(PPLFILE, 'w')
	i = 0
	for u in pop.units:
		if(i < len(pop.units)-1):
			t = str(u) + SEPARATOR
		else:
			t = str(u)
		i = i+1
		f.write(t)
	f.close()

def fillPopulation(size,gen):
	f = checkFile(gen)
	pop = gPopulation(size)
	crom = list(f.read().split(SEPARATOR))
	for line in range(size):
		c = crom[line]
		pop.addUnits(c.zfill(gen))
	f.close()
	return pop

if __name__ == "__main__":
	ppl = fillPopulation(5,14)
	print(ppl.units)
	print(ppl.unitsFitness())
