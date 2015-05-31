import ga
import math

def Fitness(c):
	bin_x1 = c[:len(c)/2]
	bin_x2 = c[len(c)/2:]
	sign = {0:'', 1:'-'}
	x1_sign = sign[int(bin_x1[:1])]
	x2_sign = sign[int(bin_x2[:1])]
	x1 = int(x1_sign+str(int(bin_x1[1:], 2)))
	x2 = int(x2_sign+str(int(bin_x2[1:], 2)))
	f = 3*x1-7*x2
	return f

popsize = 4
population = ga.PopGen(popsize, 10)

print population
for i in range(0, popsize):
	population[i] = ga.Mutation(population[i], 1/(len(population[i])))
print population

roulette

for i in range(0, int(math.floor(popsize/2))):
	i = i*2
	pop_cross =  ga.CrossSPoint(population[i], population[i+1], 1.0)
	print Fitness(pop_cross[0]), Fitness(population[i])
	print Fitness(pop_cross[1]), Fitness(population[i+1])
	if Fitness(pop_cross[0]) > Fitness(population[i]) and Fitness(pop_cross[1]) > Fitness(population[i+1]):
		population[i] = pop_cross[0]
		population[i+1] = pop_cross[1]
print population