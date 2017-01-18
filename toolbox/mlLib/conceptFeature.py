#!/usr/bin/env python
# -*- coding: utf-8 -*-

import __init__

from sklearn.ensemble import RandomForestClassifier

import cpLib.concept as cp
import utils.skUtils as sku

# FEATURE
def identity(concept):
    return concept.vect

def polar(concept):
    return concept.polarVect()

def angular(concept):
    return concept.angularVect()

# CLF
class ConceptClf(object):
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
