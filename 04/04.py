#!/usr/bin/env python3

import sys
import re
import functools
import itertools
import copy

GUARD = 0
SLEEP = 1
WAKE_UP = 2

def parse_log_line(s):
  if s.endswith('begins shift'):
    return GUARD, int(s.split('#')[1].split(' ')[0])
  time = int(s[15:17])
  if s.endswith('falls asleep'):
    return SLEEP, time
  elif s.endswith('wakes up'):
    return WAKE_UP, time
  else:
    raise ValueError()

def main():
  lines = list(map(parse_log_line, sorted(sys.stdin.read().strip().split('\n'))))
  sleep_tables = dict()
  cur_guard_id = -1
  sleep_since = -1
  for event_type, arg in lines:
    if event_type == GUARD:
      cur_guard_id = arg
    elif event_type == SLEEP:
      sleep_since = arg
    elif event_type == WAKE_UP:
      sleep_table = sleep_tables.setdefault(cur_guard_id, [0] * 60)
      for minute in range(sleep_since, arg):
        sleep_table[minute] += 1
    else:
      raise ValueError()

  best_guard_id = max(sleep_tables.keys(), key=lambda x: sum(sleep_tables[x]))
  best_minute = max(range(60), key=lambda x: sleep_tables[best_guard_id][x])
  print(best_guard_id * best_minute)

  best_guard_id, best_minute = max(itertools.product(sleep_tables.keys(), range(60)), key=lambda x: sleep_tables[x[0]][x[1]])
  print(best_guard_id * best_minute)

if __name__ == "__main__":
  main()
