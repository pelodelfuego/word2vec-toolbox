#!/usr/bin/env python
# encoding: utf-8

import utils.polarCoord as pc

import numpy as np

from scipy.weave import inline

operatorSet = set(['+', '-', 'n', '', 'p', 'a', 'm'])

# CONCEPT
class Concept(object):
    word = None
    vect = None

    def __init__(self, word, vect):
        self.word = word
        self.vect = vect

    def __repr__(self):
        return self.word

    def normalVect(self):
        return self.vect / np.linalg.norm(self.vect)

    def normalized(self):
        return Concept('__n__' + self.word, self.normalVect())

    def polarVect(self):
        return pc.carthToPolar(self.vect)

    def polarized(self):
        return Concept('__p__' + self.word, self.polarVect())

    def angularVect(self):
        return self.polarVect()[1:]

    def angularized(self):
        return Concept('__a__' + self.word, self.angularVect())


# OPERATIONS
def extractSubConcept(conceptStr):
    return set(conceptStr.split('__')) - operatorSet

def add(c1, c2):
    return Concept('__+__' + c1.word + '__' + c2.word, c1.vect + c2.vect)

def sub(c1, c2):
    return Concept('__-__' + c1.word + '__' + c2.word, c1.vect - c2.vect)

def addSub(addConceptList, subConceptList, normalized=True):
    addN = [c.normalized() for c in addConceptList] if normalized else addConceptList
    subN = [c.normalized() for c in subConceptList] if normalized else subConceptList

    sumC = addN[0]
    for c in addN[1:]:
        sumC = add(sumC, c)
    for c in subN:
        sumC = sub(sumC, c)
    return sumC

def mean(cpList):
    return Concept('__m__' + '__'.join([c.word for c in cpList]), addSub(cpList, [], normalized=False).vect)


# METRICS
def cosSim(c1, c2):
    v1 = c1.vect
    v2 = c2.vect
    dimCount = len(v1)

    code = """
            #include <math.h>

            float norm_v1 = 0.0;
            float norm_v2 = 0.0;
            float dot_pdt = 0.0;

            for(int i = 0; i < dimCount; i++) {
                dot_pdt += v1[i] * v2[i];
                norm_v1 += v1[i] * v1[i];
                norm_v2 += v2[i] * v2[i];
            }

            norm_v1 = sqrtf(norm_v1);
            norm_v2 = sqrtf(norm_v2);

            return_val = dot_pdt / norm_v1 / norm_v2;
    """
    return inline(code, ['v1', 'v2', 'dimCount'])

def euclDist(c1, c2):
    v1 = c1.vect
    v2 = c2.vect
    dimCount = len(v1)

    code = """
            #include <math.h>

            float dist = 0.0;

            for(int i = 0; i < dimCount; i++) {
                dist += pow(v1[i] - v2[i], 2);
            }

            return_val = sqrtf(dist);
    """
    return inline(code, ['v1', 'v2', 'dimCount'])

def manaDist(c1, c2):
    v1 = c1.vect
    v2 = c2.vect
    dimCount = len(v1)

    code = """
            #include <math.h>

            float dist = 0.0;

            for(int i = 0; i < dimCount; i++) {
                dist += fabs(v1[i] - v2[i]);
            }

            return_val = dist;
    """
    return inline(code, ['v1', 'v2', 'dimCount'])

if __name__ == '__main__':
    print 'weave function built'
