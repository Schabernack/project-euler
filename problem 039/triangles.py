#!/usr/bin/env python


def get_triangle_lengths(perimeter):
  results = []
  for a in xrange(1,perimeter+1):
    for b in xrange(1,perimeter+1):
      for c in xrange(1,perimeter+1):
        if a+b+c==perimeter  and  (a**2 + b**2 == c**2):
          res = sorted([a,b,c])
          if not res in results:
            results.append(res)
  return results




maxp = 0
maxsolutions = 0

for p in xrange(492,1000):
  print p
  sides = get_triangle_lengths(p)
  if len(sides) > maxsolutions:
    maxp = p
    maxsolutions = len(sides)
    print maxp,maxsolutions
