#!/usr/bin/env python
# -*- coding: utf-8 -*-

import __init__

import mlLib.conceptFeature as cpf
import cpLib.conceptDB as db
import cpLib.concept as cp
import utils.skUtils as sku
import cpLib.conceptExtraction as cpe

from sklearn.neighbors import KNeighborsClassifier

d = db.DB('../data/voc/npy/wikiEn-skipgram.npy')

X, y = [], []
strict = False
a = cpe.buildConceptList(d, open('../data/domain/luu_animal.txt').read().splitlines(), strict)
X = a
y = len(a) * ['animal']

p = cpe.buildConceptList(d, open('../data/domain/luu_plant.txt').read().splitlines(), strict)
X += p
y += len(p) * ['plant']

v = cpe.buildConceptList(d, open('../data/domain/luu_vehicle.txt').read().splitlines(), strict)
X += v
y += len(v) * ['vehicle']

X += d.getSample(len(X))
y += len(y) * ['other']

clf = cpf.ConceptClf(KNeighborsClassifier(), cp.Concept.angularVect)
sku.printClassificationReport(clf, X, y)
