#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 30 15:37:57 2025

@author: ummusalmahumarrani
"""

import unittest
import math

from calculator_app import sqrt, square, sin, cos, log  # If logic is separated

class TestCalculatorFunctions(unittest.TestCase):

    def test_square(self):
        self.assertEqual(square(3), 9)

    def test_sqrt(self):
        self.assertAlmostEqual(sqrt(16), 4.0)

    def test_sin(self):
        self.assertAlmostEqual(sin(90), 1.0, places=5)

    def test_log(self):
        self.assertAlmostEqual(log(100), 2.0)

    def test_arcsin_out_of_range(self):
        self.assertTrue(math.isnan(math.asin(2)))  # should produce domain error

if __name__ == '__main__':
    unittest.main()
