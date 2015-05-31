limit = 100

'''Search parameters for max and min value of function F'''
def F(x,y):
	'''f(x) = x^2-4x+57'''
	func = x**2+65*x*y+y**2
	return func
b = limit/2
varmax = [0,0,0]
varmin = [0,0,0]
if __name__ == '__main__':
	for i in xrange(-b,b+1):
		for j in xrange(-b,b+1):
			var = F(i,j)
			#print var
			if var > varmax[2]:
				varmax = [i,j,var]
			elif var < varmin[2]:
				varmin = [i,j,var]
	print varmax, varmin

