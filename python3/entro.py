'''
entro.py
'''
import hashlib

COUNTER_MAX = 1000000
CONCAT = 12

data = '0'
ctr = 0
gen = hashlib.md5(b'')
start = hashlib.md5(data.encode())
test = start

print(start.hexdigest()[0:CONCAT]) 

while gen.hexdigest()[0:CONCAT] != start.hexdigest()[0:CONCAT]:
    test = hashlib.md5(test.digest())
    gen = test
    ctr += 1 
    if not ctr % COUNTER_MAX:
        print(str(ctr // COUNTER_MAX) + 'M ' + gen.hexdigest()[0:CONCAT]) 

print(str(ctr) + ' ' + gen.hexdigest()[0:CONCAT] + ' ' + start.hexdigest()[0:CONCAT])
