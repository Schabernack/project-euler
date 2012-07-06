
nbr = 20
s = []
do_search = True
divisible = True

while True:
    divisible = True
    for i in range(1,20):
        if(nbr % i !=0):
            divisible=False
    if(divisible):
        break
    nbr = nbr + 20

print(nbr)
