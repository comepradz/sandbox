'''Card Shuffle using Sattolo's Algorithm'''

from random import randrange
 
def SattoloShuffle(items):
    i = len(items)
    while i > 1:
        i = i - 1
        j = randrange(i)  # 0 <= j <= i-1
        items[j], items[i] = items[i], items[j]
    return items

counter = {'123':0, '132':0, '213':0, '231':0, '312':0, '321':0}
cards = ['1', '2', '3']

print "".join(cards)
for i in xrange(0,10000):
	cards = SattoloShuffle(cards)
	counter["".join(cards)] += 1

for r in counter.keys():
	print r, "=", counter[r]