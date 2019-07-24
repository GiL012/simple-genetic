import PopulationG, random, itertools, math

MAXPOSITIVE = 100000000000
MAXNEGATIVE = -100000000000

def ruletteWheel(population,type= False):
	pf = population.unitsFitness()
	pu = population.units
	ev = dict(zip(pf,pu))
	fm = sum(ev.keys()) / len(pu)
	r = random.uniform(0,fm)
	i = [ x/fm for x in ev.keys() ]
	i = itertools.accumulate(i)
	rs = dict(zip(ev.values(),i))
	rslt = [ x for x,y in rs.items() if y >= r]
	if not rslt or len(rslt) < 2:
		return list(ev.values())[-1],list(ev.values())[-2]
	return rslt[0],rslt[1]

def tournamentSelection(population,type):
	pf = population.unitsFitness()
	pu = population.units
	pplfit = dict(zip(pf,pu))
	result = sorted(pplfit.items(),key=lambda fitness: fitness[0])
	result = tournamentN(result,type)
	return result[0][1],result[1][1]

def  tournamentN(result,type):
	k = len(result)
	lo = [result[i] for i in range(k) if i%2 == 0]
	lt = [result[i] for i in range(k) if i%2 != 0]
	r = []
	lng = math.ceil(k/2)
	if len(lo) > len(lt):
		if type:
			lt.append((MAXNEGATIVE,'0'))
			r = [lt[i] if lt[i][0] > lo[i][0] else lo[i] for i in range(lng)]
		else:
			lt.append((MAXPOSITIVE,'0'))
			r = [lt[i] if lt[i][0] < lo[i][0] else lo[i] for i in range(lng)]
	if len(r) > 2:
		r = tournamentN(r,type)
	return r

seleccionTypes = { 0:ruletteWheel,1:tournamentSelection}

if __name__ == "__main__":
	ppl = PopulationG.fillPopulation(5,10)
	print(ppl.units)
	print("ruletteWheel")
	print(seleccionTypes[0](ppl))
	print("Tournament")
	print(seleccionTypes[1](ppl,False))
	print("Tournament True")
	print(seleccionTypes[1](ppl,True))
