import math as m

number = input("Number to be checked: ")

for mod in range(2,int(m.ceil(m.sqrt(number+1)))):
	s = number % mod
	if s == 0:
		print str(number)+" is NOT a prime number"
		exit()
print str(number)+" is a prime number!!!"