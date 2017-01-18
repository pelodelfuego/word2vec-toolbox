#!/usr/bin/env python
# encoding: utf-8

import unittest

import cpLib.concept as cp
import cpLib.conceptDB as db

import numpy as np

class ConceptTest(unittest.TestCase):

    def setUp(self):
        self.d = db.DB('../data/voc/npy/googleNews_mini.npy')

    def test_transform(self):
        k = self.d.get('king')

        norm = np.linalg.norm(k.vect)
        k_p = k.polarVect()
        k_a = k.angularVect()

        for a, b in zip(np.concatenate(([norm], k_a)), k_p):
            self.assertAlmostEquals(a, b, places=5)


    # DISTANCE
    def test_cosSim(self):
        k = self.d.get('king')
        q = self.d.get('queen')

        self.assertAlmostEquals(cp.cosSim(k, q), cp.cosSim(q, k), places=5)
        self.assertAlmostEquals(cp.cosSim(k, k), 1.0, places=5)

    def test_euclDist(self):
        k = self.d.get('king')
        q = self.d.get('queen')

        self.assertEqual(cp.euclDist(k, q), cp.euclDist(q, k))
        self.assertAlmostEquals(cp.euclDist(k, k), 0.0, places=5)

    def test_manaDist(self):
        k = self.d.get('king')
        q = self.d.get('queen')

        self.assertEqual(cp.manaDist(k, q), cp.manaDist(q, k))
        self.assertAlmostEquals(cp.manaDist(k, k), 0.0, places=5)

    # OPERATION
    def test_arith(self):
        # k - m = q - w

        k = self.d.get('king')
        q = self.d.get('queen')
        m = self.d.get('man')
        w = self.d.get('woman')

        v1 = cp.add(k, w)
        v1 = cp.sub(v1, m)

        v2 = cp.sub(k, m)
        v2 = cp.add(v2, w)

        v3 = cp.addSub([k, w], [m])

        v4 = cp.sub(k.normalized(), m.normalized())
        v4 = cp.add(v4, w.normalized())

        self.assertAlmostEquals(cp.cosSim(v1, v2), 1.0, places=5)
        self.assertAlmostEquals(cp.cosSim(v3, v4), 1.0, places=5)

        self.assertEquals(self.d.find_cosSim(v1)[0][1], 'queen')
        self.assertEquals(self.d.find_cosSim(v2)[0][1], 'queen')
        self.assertEquals(self.d.find_cosSim(v3)[0][1], 'queen')
        self.assertEquals(self.d.find_cosSim(v4)[0][1], 'queen')
