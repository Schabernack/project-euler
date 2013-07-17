#!/usr/bin/env python

def fib_gen(limit=100):
    f1 = 1
    f2 = 1
    
    while limit<=100:
        if f1 == 1:
            yield 1
        elif f2 == 1:
            tmp = f1
            f1 = f2
            f2 = tmp + f1

            yield 1
        else:
            tmp = f1
            f1 = f2
            f2 = tmp + f1

            yield f2


if __name__ == '__main__':
    for i in fib_gen():
        print i
