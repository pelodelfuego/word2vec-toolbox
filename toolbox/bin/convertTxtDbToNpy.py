#!/usr/bin/env python
# encoding: utf-8

import __init__

import argparse

import json
import numpy as np

import cpLib.conceptDB as db


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Convert a word2vec vocabulary/vector file from text to numpy format')
    parser.add_argument('txtFile', help='voc and vectors file in text format')
    parser.add_argument('npFile', help='path to store the voc in numpy format')
    args = parser.parse_args()


    inputTxtFilePath = args.txtFile
    npFilePath = args.npFile
    dictFilePath = npFilePath + 'dict'

    if inputTxtFilePath.endswith('.txt') and npFilePath.endswith('.npy'):
        d = db.DB(inputTxtFilePath)

        vocIndexDict = {}

        with open(inputTxtFilePath, 'r') as inputTxtFile:
            print
            print 'vector dim: ' + inputTxtFile.readline()
            for i, line in enumerate(inputTxtFile):
                vocIndexDict[line.split()[0]] = i

        np.save(npFilePath, d.vect)

        with open(dictFilePath, 'w') as dictFile:
            json.dump(vocIndexDict, dictFile)
    else:
        print 'input file error'
