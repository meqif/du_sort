#!/usr/bin/env python
#
# Copyright (c) 2011 Ricardo Martins
#
# Licensed under the MIT License.
# http://www.opensource.org/licenses/mit-license.php

import unittest

from du_sort import *

class Sort_Criterion(unittest.TestCase):
    """ Check the function sort_criterion() works correctly. """

    def test_converts_unit(self):
        """ Check if the size is correctly retrieved and converted. """
        self.assertEqual(sort_criterion("4,0K\tLICENSE"), 4096)
        self.assertEqual(sort_criterion("0\tREADME"), 0)
        self.assertEqual(sort_criterion("5072\ttestfile"), 5072)
