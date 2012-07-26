import sys
import time

t0 = time.clock()

how_many=50
triangle = 0
i = 0
divisors = 0

while divisors<how_many:
    triangle += i
    divisors = 0
    for k in range(1,int(triangle)):
        if triangle%k==0:
            divisors += 1            
        if divisors>how_many:   
            break
    i+=1
    
print triangle
print time.clock()-t0
