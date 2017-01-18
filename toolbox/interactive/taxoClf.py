#!/usr/bin/env python
# -*- coding: utf-8 -*-

import __init__

import mlLib.conceptPairFeature as cppf
import cpLib.conceptDB as db
import cpLib.concept as cp
import utils.skUtils as sku
import cpLib.conceptExtraction as cpe

from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier

d = db.DB('../data/voc/npy/wikiEn-skipgram.npy')

X, y = [], []
X = cpe.buildConceptPairList(d, [l.split('\t') for l in open('../data/wordPair/wordnetTaxo_animal_all.txt').read().splitlines()], True)
y = len(X) * ['isParent']

negSample = cpe.shuffledConceptPairList(X)
X += negSample
y += len(negSample) * ['notParent']


clf = cppf.ConceptPairClf(RandomForestClassifier(max_depth=7), cppf.subAngular)
sku.printClassificationReport(clf, X, y, inv=True)
sku.detailClassificationError(clf, X, X, y)

