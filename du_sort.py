#!/usr/bin/env python

import sys

def sort_criterion(line):
    """
    Return the size in bytes or adimensional units of a 'du' output line.

    Defines the sort criterion for 'du' lines in the form 'size filename',
    where size may be adimensional.

    >>> sort_criterion("4,0K\tLICENSE")
    4096.0
    >>> sort_criterion("0\tREADME")
    0.0
    >>> sort_criterion("5072\ttestfile")
    5072.0
    """
    size = line.split()[0]
    # some locales use commas as decimal separators
    size = size.replace(",", ".")

    if size[-1] == "B":
        return float(size[:-1])
    elif size[-1] == "K":
        return float(size[:-1]) * 1024
    elif size[-1] == "M":
        return float(size[:-1]) * 1024**2
    elif size[-1] == "G":
        return float(size[:-1]) * 1024**3
    else: # size given in blocks, don't mess with it
        return float(size)

INPUT_FILE = sys.stdin

input = INPUT_FILE.readlines()
ordered_data = sorted(input, key=sort_criterion)

for line in ordered_data:
    print line.rstrip()
