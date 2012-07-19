import math
import time

t0 = time.clock()

last_nbr = 2000000

is_prime = [True] * (last_nbr+1)


for i in range(2,len(is_prime)):
    for k in range(2,(last_nbr/i)+1):
        #print i, "   ", k
        is_prime[i*k]=False

is_prime[0]=False
is_prime[1]=False
is_prime[2]=True

#print(filter(lambda x: x[1]==True, enumerate(is_prime)))


print(sum([i[0] for i in enumerate(is_prime) if i[1]==True]))

print time.clock()-t0
