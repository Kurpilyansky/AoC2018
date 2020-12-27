#!/usr/bin/env python3

import sys
import re
import functools
import itertools
import copy

def main():
  v = list(map(int, sys.stdin.read().strip().split('\n')))
  print(sum(v))

  used = set()
  s = 0
  i = 0
  while True:
    if s in used:
      print(s)
      break
    used.add(s)
    s += v[i]
    i = (i + 1) % len(v)


if __name__ == "__main__":
  main()
