#!/usr/bin/env python

import time
import itertools

t0 = time.clock()
pandigital = {int(''.join(map(str, x))) for x in list(itertools.permutations([x for x in range(10)]))}

print time.clock()-t0

big_pandigitals = filter(lambda x: len(str(x))==10, pandigital)

print time.clock()-t0

pandigital = big_pandigitals

#print pandigital
divisors = [2,3,5,7,11,13,17]
indexes = []
shifter = [x for x in range(0,10)]
for idx in range(1,8):
  indexes.append(shifter[idx:idx+3])

good_pandigitals = []

for nbr in pandigital:
  nbrstring = str(nbr)
  rest = []
  for x in range(len(indexes)):
    dividend = int(nbrstring[indexes[x][0]] + nbrstring[indexes[x][1]] + nbrstring[indexes[x][2]])
    divisor = divisors[x]
    rest.append(dividend%divisor)

  if all(item == 0 for item in rest):
    good_pandigitals.append(nbr)


print(sum(good_pandigitals))
