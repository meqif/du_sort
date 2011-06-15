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

class UnitMultiplierError(Exception):
   pass

def get_unit_multiplier(unit):
    units = ["B", "K", "M", "G", "T", "P"]
    exponent = dict(zip(units, range(0, len(units))))

    if unit in exponent:
        return 1024 ** exponent[unit]
    else:
        raise UnitMultiplierError

def sort_criterion(line):
    """ Returns the size in bytes or adimensional units of a 'du' output line.

    Defines the sort criterion for 'du' lines in the form 'size filename', where
    size may be adimensional.

    """
    size = line.split()[0]
    # some locales use commas as decimal separators
    size = size.replace(",", ".")

    if size[-1].isalpha():
        size, unit = size[:-1], size[-1]
        return float(size) * get_unit_multiplier(unit)
    else: # size given in blocks, don't mess with it
        return float(size)

def sort(input):
    """ Returns a copy of the input list, sorted in ascending order by the first
    column (file size in 'du' output).

    """
    return sorted(input, key=sort_criterion)

def main():
    if len(sys.argv) == 1 or sys.argv[1] == '-':
        input_file = sys.stdin
    else:
        input_file = open(sys.argv[1])

    input = input_file.readlines()

    for line in sort(input):
        print line.rstrip()

if __name__ == "__main__":
    main()

#                .-"""-.
#              _/-=-.   \
#             (_|a a/   |_
#              / "  \   ,_)
#         _    \`=' /__/
#        / \_  .;--'  `-.
#        \___)//      ,  \
#         \ \/;        \  \
#          \_.|         | |
#           .-\ '     _/_/
#         .'  _;.    (_  \
#        /  .'   `\   \\_/
#       |_ /       |  |\\
#      /  _)       /  / ||
#     /  /       _/  /  //
#     \_/       ( `-/  ||
#               /  /   \\ .-.
#               \_/     \'-'/
#                        `"`
