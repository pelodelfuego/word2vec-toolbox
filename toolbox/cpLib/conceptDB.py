#!/usr/bin/env python
# encoding: utf-8

import numpy as np

import time
import json
import random

from utils.utils import sizeof_fmt

import cpLib.concept as cp


# CONCEPT DB
class DB(object):
    def __init__(self, fname, verbose=True):
        if fname.endswith('.txt'):
            self.voc, self.vect, self.corpus = _verboseLoading(_buildFromTxtFile, fname, verbose)

        if fname.endswith('.npy'):
            self.voc, self.vect, self.corpus = _verboseLoading(_buildFromNpyFile, fname, verbose)

# CONCEPT FINDER
    def _find(self, concept, mesurement, n=10, inv=False):
        srcConceptSet = cp.extractSubConcept(concept.word)

        matchList =  [(mesurement(concept, self.get(otherConcept)), str(otherConcept)) for otherConcept in set(self.voc.keys()) - srcConceptSet]

        return sorted(matchList, key=lambda x: x[0], reverse=not inv)[:n]

    def find_cosSim(self, concept):
        return self._find(concept, cp.cosSim)

    def find_euclDist(self, concept):
        return self._find(concept, cp.euclDist, inv=True)

    def find_manaDist(self, concept):
        return self._find(concept, cp.manaDist, inv=True)

# DB MANIPULATION
    def has(self, conceptName):
        return self.voc.has_key(conceptName)

    def get(self, conceptName, tryCompose=True):
        return cp.Concept(conceptName, self.voc[conceptName]) if self.has(conceptName) else None

    def getSample(self, size):
        return [self.get(w) for w in random.sample(self.voc.keys(), size)]


# DB LOADING
def _verboseLoading(loadFunction, fname, verbose):
    t1 = time.time()

    loadVoc, loadVect, corpus = loadFunction(fname, verbose)

    if verbose:
        print len(loadVect), "loaded from", corpus
        print "mem usage", sizeof_fmt(loadVect.nbytes)
        print "loaded time", time.time() - t1, "s"

    return (loadVoc, loadVect, corpus)

def _buildFromTxtFile(fname, verbose=True):
    loadVoc = {}
    loadVect = None
    corpus = fname.split('/')[-1].split('.')[0]

    nbVect = None
    vectSize = None

    with open(fname) as vectFile:
        for i, line in enumerate(vectFile):
            splitLine = line.split()
            if i == 0:
                nbVect = int(splitLine[0])
                vectSize = int(splitLine[1])
                loadVect = np.zeros((nbVect, vectSize), dtype='f')
            else:
                k = i - 1
                for j, dimVal in enumerate(splitLine[1:]):
                    loadVect[k][j] = dimVal
                loadVoc[splitLine[0]] = loadVect[k]

                if verbose:
                    if k % 5000 == 0:
                        print k ," / " , nbVect, line.split()[0]
    return (loadVoc, loadVect, corpus)

def _buildFromNpyFile(fname, verbose=True):
    vectFilePath = fname
    vocFilePath = fname + 'dict'

    loadVoc = {}
    loadVect = None
    corpus = fname.split('/')[-1].split('.')[0]

    vocIndexDict = {}

    with open(vocFilePath) as vocFile:
        vocIndexDict = json.load(vocFile)

    loadVect = np.load(vectFilePath)

    for k, v in vocIndexDict.iteritems():
        loadVoc[k] = loadVect[v]
    return (loadVoc, loadVect, corpus)
