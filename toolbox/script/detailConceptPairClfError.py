#!/usr/bin/env python
# -*- coding: utf-8 -*-

import __init__

import argparse

import cpLib.conceptDB as db
import cpLib.conceptExtraction as cpe

import utils.skUtils as sku
from utils.utils import pairwise

import dill


def detailConceptPairClfError(d, clf, annotedConceptPairStrList, strict):
    cpPairList, yTrue = [], []
    for cpPairStrList, className in annotedConceptPairStrList:
        builtCpPairList = cpe.buildConceptPairList(d, cpPairStrList, strict)
        cpPairList += builtCpPairList
        yTrue += [className] * len(builtCpPairList)

    sku.detailClassificationError(clf, cpPairList, cpPairList, yTrue, True)

def extractAnnotedConceptPairStr(inputConceptPath):
    return [l.split('\t') for l in open(inputConceptPath[0]).read().splitlines()], inputConceptPath[1]

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Predict concept pair class according to a trained classifier')
    parser.add_argument("vocFilePath", help='voc file')
    parser.add_argument("trainedClfPath", help='trained classifier file')
    parser.add_argument("inputConceptPairPathAndClassList", nargs='+', help='concept pair file list followed by class name')
    parser.add_argument("--compose", help='try to compose concept', action='store_false')
    args = parser.parse_args()

    vocFilePath = args.vocFilePath
    trainedClfPath = args.trainedClfPath
    inputConceptPairPathAndClassList = args.inputConceptPairPathAndClassList
    annotedConceptPairStrList = [extractAnnotedConceptPairStr(f) for f in pairwise(args.inputConceptPairPathAndClassList)]
    strict = args.compose

    detailConceptPairClfError(db.DB(vocFilePath), dill.load(open(trainedClfPath)), annotedConceptPairStrList, strict)
