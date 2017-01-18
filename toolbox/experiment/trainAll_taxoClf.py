#!/usr/bin/env python
# -*- coding: utf-8 -*-

import __init__

import mlLib.conceptPairFeature as cppf
import mlLib.postFeature as pf

import cpLib.conceptDB as db
import cpLib.concept as cp
import cpLib.conceptExtraction as cpe
import utils.skUtils as sku

from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier

import dill

d = db.DB('../data/voc/npy/wikiEn-skipgram.npy')

animal = ([l.split('\t') for l in open('../data/wordPair/wordnetTaxo_animal.txt').read().splitlines()], 'animal')
animalAll = ([l.split('\t') for l in open('../data/wordPair/wordnetTaxo_animal_all.txt').read().splitlines()], 'animalAll')

for inputDs in [animal, animalAll]:
    for strict in [True, False]:
        strictStr = 'strict' if strict else ''

        X = cpe.buildConceptPairList(d, inputDs[0], strict)
        y = len(X) * ['isParent']

        negSample = cpe.shuffledConceptPairList(X)
        X += negSample
        y += len(negSample) * ['notParent']

        for clfModel in [RandomForestClassifier(n_estimators=11, max_depth=7), KNeighborsClassifier()]:
            for feature in [cppf.subCarth, cppf.subPolar, cppf.subAngular,
                            cppf.concatCarth, cppf.concatPolar, cppf.concatAngular]:
                for post in [pf.noPost, pf.postNormalize]:
                    expStr = '_'.join([inputDs[1], strictStr, str(clfModel.__class__.__name__), str(feature.__name__), str(post.__name__)])
                    savePath = '../data/learnedModel/taxo/' + expStr + '.dill'
                    print '&&&&&&&&&&'
                    print expStr

                    clf = cppf.ConceptPairClf(clfModel, post(feature))
                    sku.printClassificationReport(clf, X, y)

                    clf.fit(X, y)
                    dill.dump(clf, open(savePath, "w"))
