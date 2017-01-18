#!/usr/bin/env python
# -*- coding: utf-8 -*-

import __init__

import mlLib.conceptPairFeature as cppf
import mlLib.postFeature as pf
import cpLib.conceptDB as db
import cpLib.concept as cp
import utils.skUtils as sku
import cpLib.conceptExtraction as cpe

from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier

import dill

d = db.DB('../data/voc/npy/wikiEn-skipgram.npy')

simple = ([l.split('\t') for l in open('../data/wordPair/wordnetAnto.txt').read().splitlines()], 'simple')
bidi = ([l.split('\t') for l in open('../data/wordPair/wordnetAnto_bidi.txt').read().splitlines()], 'bidi')

for inputDs in [simple, bidi]:
    for strict in [True, False]:
        strictStr = 'strict' if strict else ''

        X = cpe.buildConceptPairList(d, inputDs[0], strict)
        y = len(X) * ['anto']

        negSample = cpe.shuffledConceptPairList(X)
        X += negSample
        y += len(negSample) * ['notAnto']

        for clfModel in [RandomForestClassifier(n_estimators=11, max_depth=7), KNeighborsClassifier()]:
            for feature in [cppf.subCarth, cppf.subPolar, cppf.subAngular,
                            cppf.concatCarth, cppf.concatPolar, cppf.concatAngular,
                            cppf.pEuclDist, cppf.pManaDist, cppf.pCosSim,
                            cppf.pdEuclDist, cppf.pdManaDist, cppf.pdCosSim]:
                for post in [pf.noPost, pf.postNormalize, pf.postAbs]:
                    expStr = '_'.join([inputDs[1], strictStr, str(clfModel.__class__.__name__), str(feature.__name__), str(post.__name__)])
                    savePath = '../data/learnedModel/anto/' + expStr + '.dill'
                    print '&&&&&&&&&&'
                    print expStr

                    print X[:4]
                    clf = cppf.ConceptPairClf(clfModel, post(feature))
                    sku.printClassificationReport(clf, X, y)

                    clf.fit(X, y)
                    dill.dump(clf, open(savePath, "w"))
