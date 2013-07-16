#!/usr/bin/env python
from pprint import pprint
import time
import math
from sets import Set

def main():
    t0 = time.clock()
    #pprint(abundant_numbers()[20:])
    pprint(no_sum_of_abundants())
    #pprint(get_divisors(12))
    print time.clock()-t0

def get_divisors(number):
    dset = Set()
    div = []
    lim = int(math.sqrt(number))+1
    for i in range(1,lim):
        if number % i == 0:
            dset.add(number/i)
            dset.add(i)
    if number>0:
        dset.remove(number)
    return dset

def abundant_numbers(limit=28123):
    an = []
    for i in range(28123):
        if sum(get_divisors(i))>i:
            an.append(i)
    return an

def no_sum_of_abundants():
    sum_of_ab = [0 for i in range(28123)]
    sset = Set()
    abundants = abundant_numbers()
    t0 = time.clock()
    alen = len(abundants)
    for i in range(alen):
        for x in range(i, alen):
            su = abundants[i]+abundants[x]
            if su > 28122:
                break
            sum_of_ab[su]=1
    soa = 0
    for x in range(len(sum_of_ab)):
        if sum_of_ab[x]==0:
            soa+=x
    return soa

if __name__ == '__main__':
    main()

