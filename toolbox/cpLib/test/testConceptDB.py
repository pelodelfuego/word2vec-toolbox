#!/usr/bin/env python
# encoding: utf-8

import unittest

import cpLib.concept as cp
import cpLib.conceptDB as db

class ConceptDBTest(unittest.TestCase):

    # MANIPULATION
    def test_buildFromTxtFile(self):
        d = db.DB('../data/voc/txt/googleNews_mini.txt')
        self.assertEquals(d.get('</s>').vect[0], d.vect[0][0])

    def test_buildFromNpyFile(self):
        d = db.DB('../data/voc/npy/googleNews_mini.npy')
        self.assertEquals(d.get('</s>').vect[0], d.vect[0][0])
