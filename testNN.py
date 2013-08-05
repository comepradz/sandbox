import random

def WGen():
	return random.random()

input_layer = {0:WGen(), 1:WGen()}
hidden_layer = {0:WGen(), 1:WGen(), 2:WGen()}
output_layer = {0:WGen()}

truth_table = {0:{0:0, 1:1}, 1:{0:1, 1:0}}

print input_layer
print hidden_layer
print output_layer