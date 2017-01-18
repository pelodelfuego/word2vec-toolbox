#!/usr/bin/env python
# encoding: utf-8

import unittest

import cpLib.conceptDB as db
import cpLib.conceptExtraction as cpe

class ConceptExtractionTest(unittest.TestCase):

    def setUp(self):
        self.d = db.DB('../data/voc/npy/googleNews_mini.npy')

    def test_buildConceptList(self):
        self.assertEquals(len(cpe.buildConceptList(self.d, ['king', 'king queen'], True)), 1)
        self.assertEquals(len(cpe.buildConceptList(self.d, ['king', 'queen'], False)), 2)

    def test_buildConceptPairList(self):
        self.assertEquals(len(cpe.buildConceptPairList(self.d, [('king', 'op', 'car'), ('king', 'op', 'king queen')], True)), 1)
        self.assertEquals(len(cpe.buildConceptPairList(self.d, [('king', 'op', 'car'), ('king', 'op', 'king queen')], False)), 2)

    def test_shuffleConceptPairList(self):
        posSample = cpe.buildConceptPairList(self.d, [('king', 'op', 'car'), ('man', 'op', 'woman'), ('king', 'op', 'queen')], False)
        negSample = cpe.shuffledConceptPairList(posSample)

        for p, n in zip(posSample, negSample):
            self.assertNotEquals(p[0].word, n[0].word)
