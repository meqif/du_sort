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

    units = ["B", "K", "M", "G", "T", "P"]
    EXPONENT = dict(zip(units, range(0, len(units))))

    if size[-1] in EXPONENT:
        return float(size[:-1]) * 1024 ** EXPONENT[size[-1]]
    else: # size given in blocks, don't mess with it
        return float(size)

def main():
    if len(sys.argv) == 1 or sys.argv[1] == '-':
        INPUT_FILE = sys.stdin
    else:
        INPUT_FILE = open(sys.argv[1])

    input = INPUT_FILE.readlines()
    ordered_data = sorted(input, key=sort_criterion)

    for line in ordered_data:
        print line.rstrip()

if __name__ == "__main__":
    main()
