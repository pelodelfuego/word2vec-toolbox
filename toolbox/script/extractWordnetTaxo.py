#!/usr/bin/env python
# encoding: utf-8

import __init__

import argparse

from nltk.corpus import wordnet as wn

def extractSynsetWord(syn):
    return syn.name()[:-5].replace('-', ' ').replace('_', ' ')

def buildTaxo(p, c):
    return '\t'.join([extractSynsetWord(p), '>', extractSynsetWord(c)])

def printHyponyms(symset):
    if len(symset.hyponyms()) == 0:
        return
    else:
        for hypo in symset.hyponyms():
            print buildTaxo(symset, hypo)
            printHyponyms(hypo)

def printAllHyponyms(parentSymsetList):
    symset = parentSymsetList[-1]
    if len(symset.hyponyms()) == 0:
        return
    else:
        for hypo in symset.hyponyms():
            for parent in parentSymsetList:
                print buildTaxo(parent, hypo)
            printAllHyponyms(parentSymsetList + [hypo])

def buildRootSynset(synStr):
    return wn.synset(synStr + '.n.01')

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Extract wordnet taxonomy starting from a word root')
    parser.add_argument('wordRoot', help='root of taxonomy')
    parser.add_argument("--all", help='include all relations', action='store_true')
    args = parser.parse_args()

    if args.all:
        printAllHyponyms([buildRootSynset(args.wordRoot)])
    else:
        printHyponyms(buildRootSynset(args.wordRoot))
