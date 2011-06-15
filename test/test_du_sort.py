#!/usr/bin/env python
#
# Copyright (c) 2011 Ricardo Martins
#
# Licensed under the MIT License.
# http://www.opensource.org/licenses/mit-license.php

import unittest

from du_sort import *

class TestUnitMultiplier(unittest.TestCase):
    """ Check the function get_unit_multiplier() works correctly. """

    def test_known_units(self):
        """ Check if all known units are associated with the correct multiplier. """
        for index, unit in enumerate(["B", "K", "M", "G", "T", "P"]):
            self.assertEqual(1024**index, get_unit_multiplier(unit))

    def test_invalid_units(self):
        """ Check if invalid units are rejected. """
        self.assertRaises(UnitMultiplierError, get_unit_multiplier, "D")
        self.assertRaises(UnitMultiplierError, get_unit_multiplier, "KB")

class TestSortCriterion(unittest.TestCase):
    """ Check the function sort_criterion() works correctly. """

    def test_converts_unit(self):
        """ Check if the size is correctly retrieved and converted. """
        self.assertEqual(sort_criterion("4,0K\tLICENSE"), 4096)
        self.assertEqual(sort_criterion("0\tREADME"), 0)
        self.assertEqual(sort_criterion("5072\ttestfile"), 5072)

    def test_raises_value_error(self):
        """ Check that input with a non-numeric first column raises an error.

        """
        for input in ["REVERSED 12345", "INVALID INPUT", "INVALIDINPUT"]:
            self.assertRaises(ValueError, sort_criterion, input)
