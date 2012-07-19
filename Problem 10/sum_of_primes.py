import math
import time

t0 = time.clock()

sum = 2
for i in xrange(3,2000000,2):
    if i%11111==0:
        print i
    isPrime=True
    for k in xrange(3,int(math.sqrt(i)+1)):
        if i%k==0:
            isPrime=False
            break
    if isPrime:
        sum +=i

print time.clock()-t0
print sum
