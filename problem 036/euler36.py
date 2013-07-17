#!/usr/bin/env python


palindromic_nbrs = []

for i in range(1000000):
    if (str(i)==str(i)[::-1]) and bin(i)[2:]==bin(i)[:1:-1]:
        palindromic_nbrs.append(i)

print sum(palindromic_nbrs)
