import random

population = range(0,100)
k = range(0,8)

for i in range(0,100):
	for j in range(0,8):
		k[j] = str("{0:b}".format(int(round(random.random()))))
	population[i] = "".join(k)

print population