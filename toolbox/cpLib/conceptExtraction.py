#!/usr/bin/env python
# -*- coding: utf-8 -*-

import __init__

import cpLib.concept as cp
import cpLib.conceptDB as db

from utils.utils import shuffled


def buildConceptList(d, conceptStrList, strict, removeNone=True):
    conceptList = [_buildConcept(d, c, strict) for c in conceptStrList]
    return filter(lambda v: v is not None, conceptList) if removeNone else conceptList

def buildConceptPairList(d, conceptPairStrList, strict):
    c1StrList, opStrList, c2StrList = zip(*conceptPairStrList)
    c1List, c2List = buildConceptList(d, c1StrList, strict, removeNone=False), buildConceptList(d, c2StrList, strict, removeNone=False)
    return [(c1, op, c2) for (c1, op, c2) in zip(c1List, opStrList, c2List) if c1 is not None and c2 is not None]

def shuffledConceptPairList(conceptPairList):
    c1List, opList, c2List = zip(*conceptPairList)
    return [(c1, op, c2) for (c1, op, c2) in zip(shuffled(c2List), opList, c1List) if c1.word != c2.word]

def _buildConcept(d, conceptStr, strict):
    if d.has(conceptStr):
        return d.get(conceptStr)

    joinedConceptStr = '_'.join(conceptStr.split())
    if d.has(joinedConceptStr):
        return d.get(joinedConceptStr)

    if not strict:
        if _canCompose(d, conceptStr):
            return _composeConcept(d, conceptStr)

    return None

def _canCompose(d, conceptStr):
    for subStr in conceptStr.split():
        if not d.has(subStr):
            return False
    return True

def _composeConcept(d, conceptStr):
    return cp.mean([d.get(c) for c in conceptStr.split()])

