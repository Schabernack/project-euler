#!/usr/bin/env python
import time
import math

def fibseq():
    f1 = 1
    f2 = 1
    while True:
        tmp = f1
        f1 = f2
        f2 = tmp + f1
        yield tmp

def len_log(nbr):
    return math.floor(math.log10(nbr))+1

def len_str(nbr):
    return len(str(nbr))

if __name__ == '__main__':
    t0 = time.clock()
    for idx, val in enumerate(fibseq()):
        if len_log(val)>=1000:
            print idx+1
            break
    print time.clock()-t0
