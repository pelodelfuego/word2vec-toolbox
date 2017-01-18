#!/usr/bin/env python
# encoding: utf-8

import unittest

import utils.polarCoord as pc
import random

class PolarCoordTest(unittest.TestCase):

    def test_consistency(self):
        carth = random.sample(range(100), 10)
        polar = pc.carthToPolar(carth)
        tryCarth = pc.polarToCarth(polar)

        for a, b in zip(carth, tryCarth):
            self.assertAlmostEquals(a, b, places = 4)
