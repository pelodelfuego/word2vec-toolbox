#!/usr/bin/env python
# -*- coding: utf-8 -*-

import __init__

import argparse

import cpLib.conceptDB as db
import cpLib.conceptExtraction as cpe

import utils.skUtils as sku
from utils.utils import pairwise

import dill


def detailConceptClfError(d, clf, annotedConceptStrList, strict):
    cpList, yTrue = [], []
    for cpStrList, className in annotedConceptStrList:
        builtCpList = cpe.buildConceptList(d, cpStrList, strict)
        cpList += builtCpList
        yTrue += [className] * len(builtCpList)

    sku.detailClassificationError(clf, cpList, cpList, yTrue, True)

def extractAnnotedConceptStr(inputConceptPath):
    return open(inputConceptPath[0]).read().splitlines(), inputConceptPath[1]

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='detail concept classifier error')
    parser.add_argument("vocFilePath", help='voc file')
    parser.add_argument("trainedClfPath", help='trained classifier file')
    parser.add_argument("inputConceptPathandClassList", nargs='+', help='concept file list followed by class name')
    parser.add_argument("--compose", help='try to compose concept', action='store_false')
    args = parser.parse_args()

    vocFilePath = args.vocFilePath
    trainedClfPath = args.trainedClfPath
    annotedConceptStrList = [extractAnnotedConceptStr(f) for f in pairwise(args.inputConceptPathandClassList)]
    strict = args.compose

    detailConceptClfError(db.DB(vocFilePath), dill.load(open(trainedClfPath)), annotedConceptStrList, strict)
