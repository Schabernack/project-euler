import sys
import time

def foo():

    t0 = time.clock()

    how_many=500
    triangle = 0
    i = 0
    divisors = 0
    
    while divisors<how_many:
        triangle += i
        divisors = 0
        k = 1
        while k<triangle/k:
            if triangle%k==0:
                divisors+=2
            k+=1
        
            if divisors>how_many:   
                break
        i+=1
    
    print triangle
    print time.clock()-t0

if __name__ == "__main__":
    foo()
