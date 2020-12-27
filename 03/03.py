#!/usr/bin/env python3

import sys
import re
import functools
import itertools
import copy

class Rectangle:
  def __init__(self, rect_id, x0, y0, dx, dy):
    self.rect_id = rect_id
    self.x0 = x0
    self.y0 = y0
    self.x1 = x0 + dx
    self.y1 = y0 + dy

def parse_rect(line):
  m = re.match(r'^#(\d+) @ (\d+),(\d+): (\d+)x(\d+)$', line)
  return Rectangle(*map(int, [m.group(i + 1) for i in range(5)]))

def main():
  rects = list(map(parse_rect, sys.stdin.read().strip().split('\n')))

  counts = dict()
  for rect in rects:
    for x in range(rect.x0, rect.x1):
      for y in range(rect.y0, rect.y1):
        counts[(x, y)] = counts.get((x, y), 0) + 1
  print(sum([1 for k, v in counts.items() if v > 1]))
     
  for rect in rects:
    if all([counts[(x, y)] == 1 for y in range(rect.y0, rect.y1) for x in range(rect.x0, rect.x1)]):
      print(rect.rect_id)


if __name__ == "__main__":
  main()
