#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 30 15:37:57 2025

@author: ummusalmahumarrani
"""

import unittest
import math

class TestCalculatorFunctions(unittest.TestCase):

    def test_square(self):
        self.assertEqual(3 ** 2, 9)

    def test_sqrt(self):
        self.assertAlmostEqual(math.sqrt(16), 4.0)

    def test_sin(self):
        self.assertAlmostEqual(math.sin(math.radians(90)), 1.0, places=5)

    def test_log(self):
        self.assertAlmostEqual(math.log10(100), 2.0)

    def test_arcsin_out_of_range(self):
        with self.assertRaises(ValueError):
            math.asin(2)  # Will raise ValueError due to domain error

if __name__ == '__main__':
    unittest.main()

