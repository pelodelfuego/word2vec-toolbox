#!/usr/bin/env python
# -*- coding: utf-8 -*-

import __init__

import argparse

from nltk.corpus import wordnet as wn


def buildAnto(p, n):
    return '\t'.join([p.name(), '!=', n.name()])

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Extract wordnet antonyms')
    parser.add_argument("--bidi", help='include bidirectional relations', action='store_true')
    args = parser.parse_args()

    doneAnto = set()
    for i in wn.all_synsets():
        if i.pos() in ['a', 's']:
            for j in i.lemmas():
                if j.antonyms():
                    p = j
                    n = j.antonyms()[0]

                    cleanRelation = buildAnto(j, j.antonyms()[0]).replace('-', ' ').replace('_', ' ')

                    if args.bidi:
                        print cleanRelation
                    else:
                        if not p in doneAnto and not n in doneAnto:
                            print cleanRelation
                        doneAnto.add(p)
                        doneAnto.add(n)
