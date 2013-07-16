#!/usr/bin/env python

from urllib import urlopen
from pprint import pprint

#names = urlopen("http://projecteuler.net/project/names.txt").read()
names = ''
with open("names.txt") as f:
    names = f.read()

names = names.replace("\"","")
names = names.split(',')
names.sort()

sum_of_names = 0
for idx, val in enumerate(names):
    sum_of_names += (idx + 1)* sum([ord(letter)-64 for letter in val])

pprint(sum_of_names)
