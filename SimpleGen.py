import PopulationG, Selection, Mutation, Crossover, sys, random
# first arg size of population
# second arg size of cromosome
# third arg type selection
#   0. Ruletwheel
#   1. Tornament 
# forth arg type crossover
#   0. uniformCross 
#   1. onePointFunc 
#   2. crossPointFunc 
#   3. permutationFunc 
# fifth arg mutation rate default 0.3
# sixth arg max iterations

try:
	people = int(sys.argv[1])
	cromosomeS = int(sys.argv[2])
	selectionT = int(sys.argv[3])
	crossoverT = int(sys.argv[4])
	mutationT = float(sys.argv[5])
	iterations = int(sys.argv[6])
except ValueError:
	print("Input value error")
	return -1
except:
	print("Unexpected Error")

while(iterations > 0):
	ppl = PopulationG.fillPopulation(people,cromosomeS)
	pplfit =[]
	pplcrs =[]
	pplsel = Selection.seleccionTypes[selectionT](ppl,(selectionT < 2))
	pplcrs = Crossover.crossoverTypes[crossoverT](pplsel[0],pplsel[1])
	pplmt = []	
	if(random.random() < mutationT):
		if(selectionT < 2):
			pplmt.append(Mutation.mutationType[0](pplcrs[0],mutationT))
			pplmt.append(Mutation.mutationType[0](pplcrs[1],mutationT))
		else:
			pplmt.append(Mutation.mutationType[1](pplcrs[0]))
			pplmt.append(Mutation.mutationType[1](pplcrs[1]))
	if(pplmt):
		pplfit.extend(pplmt)
	else:
		pplfit.extend(pplcrs)
	pplsel = Selection.seleccionTypes[selectionT](ppl,(selectionT >= 2))
	pplfit.extend([x for x in ppl.units if x not in pplsel])
	print(pplfit)
	ppl.units = pplfit
	PopulationG.newPopulation(ppl)
	iterations = iterations - 1