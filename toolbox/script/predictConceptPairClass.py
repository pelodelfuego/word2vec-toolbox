#!/usr/bin/env python
# -*- coding: utf-8 -*-

import __init__

import argparse

import cpLib.conceptDB as db
import cpLib.conceptExtraction as cpe
import dill


def printPredictedConceptPairClass(d, clf, cpPairStrList, strict):
    cpPairList = cpe.buildConceptPairList(d, cpPairStrList, strict)

    yPred = clf.predict(cpPairList)
    yProba = clf.predict_proba(cpPairList)
    for x, y, yp in zip(cpPairStrList, yPred, yProba):
        print '\t'.join([str(i) for i in [x, y, yp]])


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Predict concept pair class according to a trained classifier')
    parser.add_argument("vocFilePath", help='voc file')
    parser.add_argument("trainedClfPath", help='trained classifier file')
    parser.add_argument("inputConceptPairPath", help='concept pair file')
    parser.add_argument("--compose", help='try to compose concept', action='store_false')
    args = parser.parse_args()

    vocFilePath = args.vocFilePath
    trainedClfPath = args.trainedClfPath
    inputConceptPairPath = args.inputConceptPairPath
    strict = args.compose

    cpPairStrList = open(inputConceptPairPath).read().splitlines()

    printPredictedConceptPairClass(db.DB(vocFilePath), dill.load(open(trainedClfPath)), [l.split('\t') for l in cpPairStrList], strict)
