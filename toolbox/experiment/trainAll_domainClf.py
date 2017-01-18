#!/usr/bin/env python
# -*- coding: utf-8 -*-

import __init__

import mlLib.conceptFeature as cpf
import mlLib.postFeature as pf
import cpLib.concept as cp
import cpLib.conceptDB as db
import cpLib.conceptExtraction as cpe
import utils.skUtils as sku

from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier

import dill

d = db.DB('../data/voc/npy/wikiEn-skipgram.npy')

a = (open('../data/domain/luu_animal.txt').read().splitlines(), 'animal')
p = (open('../data/domain/luu_plant.txt').read().splitlines(), 'plant')
v = (open('../data/domain/luu_vehicle.txt').read().splitlines(), 'vehicle')

for inputDsList in [[a], [p], [v], [a, p], [a, v], [p, v], [a, p, v]]:
    for strict in [True, False]:
        strictStr = 'strict' if strict else ''
        for withOther in [True, False]:
            X, y = [], []
            for sourceDs in inputDsList:
                cpList = cpe.buildConceptList(d, sourceDs[0], strict)
                X += cpList
                y += len(cpList) * [sourceDs[1]]

            usedDsName = [n[1] for n in inputDsList]
            if withOther:
                X += d.getSample(len(X))
                y += len(y) * ['other']
                usedDsName += ['other']

            if len(usedDsName) == 1:
                continue

            for clfModel in [RandomForestClassifier(n_estimators=11, max_depth=7), KNeighborsClassifier()]:
                for feature in [cpf.identity, cpf.polar, cpf.angular]:
                    for post in [pf.noPost, pf.postNormalize, pf.postAbs]:
                        expStr = '_'.join(['-'.join(usedDsName), strictStr, str(clfModel.__class__.__name__), str(feature.__name__), str(post.__name__)])
                        savePath = '../data/learnedModel/domain/' + expStr + '.dill'
                        print '&&&&&&&&&&'
                        print expStr

                        clf = cpf.ConceptClf(clfModel, post(feature))
                        sku.printClassificationReport(clf, X, y)

                        clf.fit(X, y)
                        dill.dump(clf, open(savePath, "w"))







