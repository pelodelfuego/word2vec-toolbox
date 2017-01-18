#!/usr/bin/env python
# encoding: utf-8

import __init__

import argparse
from path import path

import numpy as np

import cpLib.conceptDB as db
import utils.polarCoord as pc


def lineToPolar(vectorLine):
    return pc.carthToPolar(vectorLine)

def lineToAngular(vectorLine):
    return pc.carthToPolar(vectorLine)[1:]

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Convert a word2vec vocabulary/vector from carthesian to polar')
    parser.add_argument('inputFilePath', help='input database')
    parser.add_argument('outputFolderPath', help='folder path to store the output database')
    parser.add_argument("--angular", help='drop norm of vectors (angular)', action='store_true')
    args = parser.parse_args()

    d = db.DB(args.inputFilePath)
    newVectFile, transformName = [], ''

    if args.angular:
        newVectFile = np.apply_along_axis(lineToAngular, 1, d.vect)
        transformName = '_angular'
    else:
        newVectFile = np.apply_along_axis(lineToPolar, 1, d.vect)
        transformName = '_polar'

    vectInPath, dictInPath = path(args.inputFilePath), path(args.inputFilePath + 'dict')
    outParentPath = path(args.outputFolderPath)
    vectOutPath = path(outParentPath / vectInPath.namebase + transformName + vectInPath.ext)
    dictOutPath = path(outParentPath / dictInPath.namebase + transformName + dictInPath.ext)

    np.save(vectOutPath, newVectFile)
    dictInPath.copy(dictOutPath)
