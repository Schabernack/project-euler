#!/usr/bin/env python

import os


def triangle_gen(maxval):
  n = 1
  while True:
    res = int((0.5*n) * (n+1))
    if res > maxval:
      break
    yield res
    n+=1



scores = []

with open('p042_words.txt', 'r') as f:
  for line in f:
    words = line.split(',')



for word in words:
  score = 0
  word = word.strip('"')
  for letter in word:
    score += ord(letter.upper())-64
  scores.append(score)


triangle_numbers = []
for x in triangle_gen(max(scores)):
  triangle_numbers.append(x)

tria_in_list = 0
for score in scores:
  if score in triangle_numbers:
    tria_in_list += 1

print tria_in_list
