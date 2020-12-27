#!/usr/bin/env python3

import sys
import re
import functools
import itertools
import copy

def get_check_sum(s):
  counts = dict()
  for c in s:
    counts[c] = counts.get(c, 0) + 1
  counts = set(counts.values())
  return 2 in counts, 3 in counts


def similarity(s1, s2):
  diffs = {i for i in range(len(s1)) if s1[i] != s2[i]}
  if len(diffs) == 1:
    index = list(diffs)[0]
    return s1[:index] + s1[index+1:]

def main():
  ids = list(sys.stdin.read().strip().split('\n'))
  
  x2, x3 = functools.reduce(lambda x, y: (x[0] + y[0], x[1] + y[1]), map(get_check_sum, ids))
  print(x2 * x3)

  for i in range(len(ids)):
    for j in range(i):
      x = similarity(ids[i], ids[j])
      if x is not None:
        print(x)


if __name__ == "__main__":
  main()
