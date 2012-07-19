#http://projecteuler.net/problem=8

from urllib import urlopen
import re

website = urlopen("http://projecteuler.net/problem=8").read()

rx_blanks=re.compile(r"\W+") # to remove blanks and newlines

problem = rx_blanks.sub("",website)

find_nbr = re.compile("(7316)(.*)(63450)")

nbr = find_nbr.search(problem).group()
nbr = nbr.replace("b","").replace("r","")
i=0
max=-1

while i<len(nbr)-5:
    product=1
    for k in range(5):
        product = product*int(nbr[i+k])
    if max<product:
        max = product
    i=i+1

print max




