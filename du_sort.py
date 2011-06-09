#!/usr/bin/env python
#
# Copyright (c) 2011 Ricardo Martins
#
# Licensed under the MIT License.
# http://www.opensource.org/licenses/mit-license.php

""" du_sort: a short script for sorting 'du' output correctly

Don't you hate when you want to quickly check what's using the most space in
your laptop's disk or server's RAID but 'du -hsc *' gives you unsorted output?

Using 'du -hsc * | sort --numeric-sort' doesn't help because the units after the
size mess everything up and using 'du -k' to display the size in blocks would
allow easy sorting but defeat the purpose of having human-readable units.

So I did what any respectable programmer would do: create a script that would
sort the results exactly as I want them. That's how this script was born.

I hope it's as useful to you as it has been to me. :)
"""

import sys

def sort_criterion(line):
    """ Returns the size in bytes or adimensional units of a 'du' output line.

    Defines the sort criterion for 'du' lines in the form 'size filename', where
    size may be adimensional.

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
    exponent = dict(zip(units, range(0, len(units))))

    if size[-1] in exponent:
        return float(size[:-1]) * 1024 ** exponent[size[-1]]
    else: # size given in blocks, don't mess with it
        return float(size)

def main():
    if len(sys.argv) == 1 or sys.argv[1] == '-':
        input_file = sys.stdin
    else:
        input_file = open(sys.argv[1])

    input = input_file.readlines()
    ordered_data = sorted(input, key=sort_criterion)

    for line in ordered_data:
        print line.rstrip()

if __name__ == "__main__":
    main()
