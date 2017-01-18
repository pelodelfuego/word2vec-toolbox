#!/usr/bin/env python
# -*- coding: utf-8 -*-

import __init__

import mlLib.conceptPairFeature as cppf
import cpLib.conceptDB as db
import cpLib.concept as cp
import utils.skUtils as sku
import cpLib.conceptExtraction as cpe
import mlLib.postFeature as pf

from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier

d = db.DB('../data/voc/npy/wikiEn-skipgram.npy')

X, y = [], []
X = cpe.buildConceptPairList(d, [l.split('\t') for l in open('../data/wordPair/wordnetAnto.txt').read().splitlines()], False)
y = len(X) * ['anto']

negSample = cpe.shuffledConceptPairList(X)
X += negSample
y += len(negSample) * ['not anto']

print len(X), len(y)
clf = cppf.ConceptPairClf(RandomForestClassifier(n_estimators=11, max_depth=7), pf.noPost(cppf.subCarth))
sku.printClassificationReport(clf, X, y)

# sku.detailClassificationError(clf, X, X, y)

