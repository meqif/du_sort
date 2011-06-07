#!/usr/bin/env python

import sys

def sort_criterion(line):
    size = line.split()[0]

    if size[-1] == "K":
        return float(size[:-1])
    elif size[-1] == "M":
        return float(size[:-1]) * 1024
    elif size[-1] == "G":
        return float(size[:-1]) * 1024**2
    else: # size given in blocks, don't mess with it
        return float(size[:-1])

INPUT_FILE = sys.stdin

input = INPUT_FILE.readlines()
ordered_data = sorted(input, key=sort_criterion)

for line in ordered_data:
    print line.rstrip()
