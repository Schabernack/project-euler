#!/usr/bin/env python

alb = 2
aub = 100

blb = 2
bub = 100

rset = set()

for a in range(alb, aub+1):
  for b in range(blb, bub+1):
    rset.add(a**b)

print(len(rset))
