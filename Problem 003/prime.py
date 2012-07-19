import itertools
import math

primes = []

nbr = 600851475143 

i = 0

while i<math.sqrt(nbr):
    prime = True
    for k in xrange(2,int(math.sqrt(i)+1)):
        if(i%k == 0):
            prime = False
            break
    if prime:
        primes.append(i)
    i+=1




factors = []


for i in reversed(primes):
    if i!=0 and nbr%i==0:
        factors.append(i)

print(factors)
