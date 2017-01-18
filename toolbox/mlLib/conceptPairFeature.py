#!/usr/bin/env python
# -*- coding: utf-8 -*-

import __init__

import numpy as np
from scipy.weave import inline

from sklearn.ensemble import RandomForestClassifier

import cpLib.concept as cp
import utils.skUtils as sku


# PROJECTION
def projCosSim(c1, c2):
    v1 = c1.vect
    v2 = c2.vect
    dimCount = len(v1)

    arr = np.zeros(dimCount, 'f')

    code = """
            for(int i = 0; i < dimCount; i++) {
                float norm_v1 = 0.0;
                float norm_v2 = 0.0;
                float dot_pdt = 0.0;

                for(int j = 0; j < dimCount; j++) {
                    if(i != j) {
                        dot_pdt += v1[j] * v2[j];
                        norm_v1 += v1[j] * v1[j];
                        norm_v2 += v2[j] * v2[j];
                    }
                }

                norm_v1 = sqrtf(norm_v1);
                norm_v2 = sqrtf(norm_v2);

                arr[i] = dot_pdt / norm_v1 / norm_v2;
            }

            return_val = 1;
    """
    inline(code, ['v1', 'v2', 'dimCount', 'arr'], headers = ['<math.h>'], compiler = 'gcc')
    return arr

def projEuclDist(c1, c2):
    v1 = c1.vect
    v2 = c2.vect
    dimCount = len(v1)

    arr = np.zeros(dimCount, 'f')

    code = """
            for(int i = 0; i < dimCount; i++) {
                float dist = 0.0;

                for(int j = 0; j < dimCount; j++) {
                    if(i != j) {
                        dist += pow(v1[j] - v2[j], 2);
                    }
                }

                arr[i] = sqrt(dist);
            }

            return_val = 1;
    """
    inline(code, ['v1', 'v2', 'dimCount', 'arr'], headers = ['<math.h>'], compiler = 'gcc')
    return arr

def projManaDist(c1, c2):
    v1 = c1.vect
    v2 = c2.vect
    dimCount = len(v1)

    arr = np.zeros(dimCount, 'f')

    code = """
            for(int i = 0; i < dimCount; i++) {
                float dist = 0.0;

                for(int j = 0; j < dimCount; j++) {
                    if(i != j) {
                        dist += fabs(v1[i] - v2[i]);
                    }
                }

                arr[i] = dist;
            }

            return_val = 1;
    """
    inline(code, ['v1', 'v2', 'dimCount', 'arr'], headers = ['<math.h>'], compiler = 'gcc')
    return arr


# COMMUTATIVE FEATURE
def subCarth(conceptPair):
    return conceptPair[2].vect - conceptPair[0].vect

def subPolar(conceptPair):
    return conceptPair[2].polarVect() - conceptPair[0].polarVect()

def subAngular(conceptPair):
    return conceptPair[2].angularVect() - conceptPair[0].angularVect()

def concatCarth(conceptPair):
    return np.concatenate((conceptPair[0].vect, conceptPair[2].vect))

def concatPolar(conceptPair):
    return np.concatenate((conceptPair[0].polarVect(), conceptPair[2].polarVect()))

def concatAngular(conceptPair):
    return np.concatenate((conceptPair[0].angularVect(), conceptPair[2].angularVect()))


# NON COMMUATIVE FEATURE
# PROJECTION SIMILARITY
def pCosSim(conceptPair):
    return projCosSim(conceptPair[0], conceptPair[2])

def pEuclDist(conceptPair):
    return projEuclDist(conceptPair[0], conceptPair[2])

def pManaDist(conceptPair):
    return projManaDist(conceptPair[0], conceptPair[2])

# PROJECTION DISSIMILARITY
def _projectionDissimarilty(projectionMetric, globalMetric, conceptPair):
    projectedFeature = projectionMetric(conceptPair[0], conceptPair[2])
    globalFeature = globalMetric(conceptPair[0], conceptPair[2])
    return np.array([(globalFeature - v) for v in projectedFeature])

def pdCosSim(conceptPair):
    return _projectionDissimarilty(projCosSim, cp.cosSim, conceptPair)

def pdEuclDist(conceptPair):
    return _projectionDissimarilty(projEuclDist, cp.euclDist, conceptPair)

def pdManaDist(conceptPair):
    return _projectionDissimarilty(projManaDist, cp.manaDist, conceptPair)


# CLF
class ConceptPairClf(object):
    def __init__(self, clf, featureExtractionFct):
        self.clf = clf
        self.featureExtractionFct = featureExtractionFct

    def fit(self, X, y):
        self.clf.fit([self.featureExtractionFct(x) for x in X], y)
        self.classes_ = self.clf.classes_

    def predict(self, X):
        return self.clf.predict([self.featureExtractionFct(x) for x in X])

    def predict_proba(self, X):
        return self.clf.predict_proba([self.featureExtractionFct(x) for x in X])
