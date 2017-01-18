#!/usr/bin/env python
# -*- coding: utf-8 -*-

import __init__

import argparse

import cpLib.conceptDB as db
import cpLib.conceptExtraction as cpe


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='shuffle a wordPair file')
    parser.add_argument("vocFilePath", help='voc file')
    parser.add_argument("inputConceptPairPath", help='concept pair file')
    args = parser.parse_args()

    vocFilePath = args.vocFilePath
    inputConceptPairPath = args.inputConceptPairPath
    conceptPairStrList = [l.split('\t') for l in open(args.inputConceptPairPath).read().splitlines()]
    strict = args.compose

    d = db.DB('../data/voc/npy/wikiEn-skipgram.npy', False)
    conceptPairList = cpe.buildConceptPairList(d, conceptPairStrList, True)

    shuffledConceptPairList = cpe.shuffledConceptPairList(conceptPairList)

    for conceptPair in shuffledConceptPairList:
        print '\t'.join([str(s) for s in conceptPair])
