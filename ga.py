'''Basic Genetic Algorithm Implementation'''
'''Chromosome represented as binary'''

import random

def PopGen(pop_size, chromo_len):
	'''Initialize two lists for population and chromosome generation'''
	pop = range(0,pop_size)
	for i in range(0,pop_size):
		k = ''
		for j in range(0,chromo_len):
			'''Generate chromosome by appending string output of random.randint'''
			k +=  str(random.randint(0,1))
		pop[i] = k
	return pop

def CrossSPoint(m, f, pc=0.6):
	'''Crossover operator with probability pc'''
	if random.random() <= pc:
		point = random.randint(1, len(m)-1)
		temp = m[:point]
		m = f[:point]+m[point:]
		f = temp+f[point:]
	return [m, f]

def Mutation(c, pm=0.1):
	if random.random() <= pm:
		point = random.randint(1, len(c)-1)
		temp = list(c)
		temp[point] = str(abs(int(temp[point])-1))
		c = "".join(temp)
	return c

def Roulette():
	return 0