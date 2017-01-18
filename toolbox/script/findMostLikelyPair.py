#!/usr/bin/env python
# encoding: utf-8

import __init__

import argparse
import dill

import cpLib.conceptDB as db
import cpLib.conceptExtraction as cpe


def extractSubDomain(subDomainFile, conceptSource):
    conceptStrSet = set()

    for line in subDomainFile.read().splitlines():
        for conceptStr in line.split('\t'):
            if conceptStr != conceptSource.word:
                conceptStrSet.add(conceptStr)

    return list(conceptStrSet)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Find best pair match given a trained pair classifier')
    parser.add_argument("vocFilePath", help='voc file')
    parser.add_argument("trainedClfPath", help='trained classifier file')
    parser.add_argument("sourceConcept", help='concept source')
    parser.add_argument("targetClass", help='class to search the best match for')
    parser.add_argument("--domain", help='restrict target domain')
    args = parser.parse_args()

    d = db.DB(args.vocFilePath)
    clf = dill.load(open(args.trainedClfPath))
    classIndex = clf.classes_.tolist().index(args.targetClass)

    conceptSource = d.get(args.sourceConcept)

    otherConceptStrList = [c for c in d.voc.keys() if c != conceptSource.word] if args.domain is None else extractSubDomain(open(args.domain), conceptSource)
    conceptPairList =  zip([conceptSource.word] * len(otherConceptStrList), [args.targetClass] * len(otherConceptStrList), otherConceptStrList)

    X = cpe.buildConceptPairList(d, conceptPairList, True)
    yProba = clf.predict_proba(X)

    bestMatchList = sorted(zip(X, yProba), key=lambda x: x[1][classIndex], reverse=True)

    for match in bestMatchList[:50]:
        print match

