import math

which_prime = 10001
prime_no = 1
i = 3

while prime_no < which_prime:
    is_prime = True
    for div in xrange (2,int(math.sqrt(i)+1)):
        if (i % div == 0):            
            is_prime = False
            break
    if is_prime:
        prime_no = prime_no+1
    if prime_no==which_prime:
        break
    i = i+2


print i
