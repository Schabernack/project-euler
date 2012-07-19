
triplets = []

for c in reversed(range(999)):
    for b in range(1, c):
        a = 1000-b-c
        if 0<=a<b<c:
                triplets.append((a,b,c))

for triple in triplets:
    if triple[0]**2+triple[1]**2==triple[2]**2:
        print triple
        print "product: ", triple[0]*triple[1]*triple[2]
        break


    
            
