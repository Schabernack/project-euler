#!/usr/bin/env python
import time

def get_triangle_lengths(perimeter):
  results = []
  for x in xrange(perimeter-2,0,-1):
    for y in xrange(perimeter-2):
      z = perimeter - x - y
      if x>=y>=z>0:
        if (x**2 + y**2 == z**2) or (x**2 + z**2 == y**2) or (y**2 + z**2 == x**2):
          results.append([x,y,z])
  return results


t0 = time.clock()
print get_triangle_lengths(120)
print time.clock()-t0

maxp = 0
maxsolutions = 0



for p in xrange(1,1000):
  sides = get_triangle_lengths(p)
  if len(sides) > maxsolutions:
    maxp = p
    maxsolutions = len(sides)
    print maxp,maxsolutions
