#!/usr/bin/env python
# -*- coding: utf-8 -*-

import __init__

from itertools import izip

import numpy as np

# from sklearn.cross_validation import KFold
from sklearn.model_selection import KFold
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from sklearn.metrics import f1_score

def extractSubSet(fullDataSet, trainIndexList, testIndexList, inv=False):
    if inv:
        return ([fullDataSet[index] for index in testIndexList], [fullDataSet[index] for index in trainIndexList])
    else:
        return ([fullDataSet[index] for index in trainIndexList], [fullDataSet[index] for index in testIndexList])

def printClassificationReport(clf, X, y, nbFold=10, inv=False):
    kf = KFold(n_splits=nbFold, shuffle=True)
    for i, (trainIndexList, testIndexList) in enumerate(kf.split(X)):
        print '\nfold', i
        print '--------'

        xTrain, xTest = extractSubSet(X, trainIndexList, testIndexList, inv)
        yTrain, yTest = extractSubSet(y, trainIndexList, testIndexList, inv)

        print 'learn'
        clf.fit(xTrain, yTrain)
        gtLabelList = clf.classes_

        print 'predict'
        yPred = clf.predict(xTest)
        yTrue = yTest

        print '\n--  REPORT  --'
        print classification_report(yTrue, yPred, target_names = gtLabelList)

def detailClassificationError(clf, data, X, y, displayProba=False):
    yPred = clf.predict(X)
    proba = clf.predict_proba(X)

    for (d, x, yP, pb, yT) in izip(data, X, yPred, proba, y):
        if yP != yT:
            withProba = 'proba:' + str(pb)
            print '  /  '.join(['input: ' + str(d), 'predicted: ' + str(yP), 'true: ' + str(yT), withProba if displayProba else ""])

    gtLabelList = clf.classes_
    print '\n--  REPORT  --'
    print classification_report(y, yPred, target_names = gtLabelList)
