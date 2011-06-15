#!/usr/bin/env python
#
# Copyright (c) 2011 Ricardo Martins
#
# Licensed under the MIT License.
# http://www.opensource.org/licenses/mit-license.php

from nose.tools import *
from du_sort import *

def test_prefix_multiplier_known_prefixes():
    """ Check if all known units are associated with the correct multiplier. """
    for index, unit in enumerate(["B", "K", "M", "G", "T", "P"]):
        eq_(get_prefix_multiplier(unit), 1024 ** index)

def test_prefix_multiplier_invalid_prefixes():
    """ Check if invalid units are rejected. """
    assert_raises(PrefixMultiplierError, get_prefix_multiplier, "D")

def test_convert_dimensional_sizes():
    """ Check if sizes with units are converted to their value in bytes. """
    assert size_to_bytes("0B") == 0
    assert size_to_bytes("4.0K") == 4096
    assert size_to_bytes("113.5M") == 119013376

def test_convert_dimensional_sizes_with_comma():
    """ Check if sizes with commas as decimal separator are treated correctly. """
    assert size_to_bytes("4,0K") == 4096

def test_parse_du_output():
    """ Check if du output is correctly parsed. """
    assert sort_criterion("4,0K\tLICENSE") == 4096
    assert sort_criterion("0\tREADME") == 0
    assert sort_criterion("123.0M             LONGSPACE") == 128974848

def test_parse_adimensional_sizes():
    """ Check if filesizes without units are not mangled. """
    assert sort_criterion("5072\ttestfile") == 5072

def test_sort():
    """ Check if sort order is correct. """
    original = ["12.0K\tREADME", "2.0G\tfoo", "0\ttestfile", "5.3M\tblob"]
    expected = ["0\ttestfile", "12.0K\tREADME", "5.3M\tblob", "2.0G\tfoo"]
    assert sort(original) == expected
