#!/usr/bin/env python

import itertools

x = itertools.permutations([x for x in range(10)])

n = 1000000 - 1

foo = itertools.islice(x, n,n+1).next()

res = ''

for bla in foo:
  res += str(bla)


print res
