#!/usr/bin/env python



import itertools



x = itertools.permutations([x for x in range 10])



n = 1000000



print(itertools.islice(x, n,n+1))

