import time

t0 = time.clock()

for c in reversed(range(999)):
    for b in range(1, 1000-c):
        a = 1000-b-c
        if 0<=a<b<c and a**2+b**2==c**2:
                print a*b*c



    
print time.clock() - t0
