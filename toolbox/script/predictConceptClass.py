#!/usr/bin/env python
# -*- coding: utf-8 -*-

import __init__

import argparse

import cpLib.conceptDB as db
import cpLib.conceptExtraction as cpe
import dill


def printPredictedConceptClass(d, clf, cpStrList, strict):
    cpList = cpe.buildConceptList(d, cpStrList, strict)

    yPred = clf.predict(cpList)
    yProba = clf.predict_proba(cpList)
    for x, y, yp in zip(cpStrList, yPred, yProba):
        print '\t'.join([str(i) for i in [x, y, yp]])


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Predict concept class according to a trained classifier')
    parser.add_argument("vocFilePath", help='voc file')
    parser.add_argument("trainedClfPath", help='trained classifier file')
    parser.add_argument("inputConceptPath", help='concept file')
    parser.add_argument("--compose", help='try to compose concept', action='store_false')
    args = parser.parse_args()

    vocFilePath = args.vocFilePath
    trainedClfPath = args.trainedClfPath
    inputConceptPath = args.inputConceptPath
    strict = args.compose

    cpStrList = open(inputConceptPath).read().splitlines()

    printPredictedConceptClass(db.DB(vocFilePath), dill.load(open(trainedClfPath)), cpStrList, strict)
