nbrs = []

for i in range (100,1000):
    for k in range(100,1000):
        nbrs.append(i*k)

x = (filter(lambda x: str(x) == str(x)[::-1],nbrs))
       
print(max(x))
