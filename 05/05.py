#!/usr/bin/env python3

import sys
import re
import functools
import itertools
import copy

def destroy(x, y):
  return abs(ord(x) - ord(y)) == abs(ord('a') - ord('A'))

def reduced_length(s):
  st = []
  for ch in s:
    if st and destroy(st[-1], ch):
      st.pop()
    else:
      st.append(ch)
  return len(st)

def remove_units(s, ch):
  return ''.join([c for c in s if c != ch and not destroy(c, ch)])

def main():
  s = sys.stdin.read().strip()
  print(reduced_length(s))
  print(min([reduced_length(remove_units(s, chr(ord('a') + ch))) for ch in range(26)]))

if __name__ == "__main__":
  main()
