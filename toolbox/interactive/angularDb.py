#!/usr/bin/env python
# -*- coding: utf-8 -*-

import __init__

import cpLib.concept as cp
import cpLib.conceptDB as db
import numpy as np

def printReport(reportName, filePath):
    print '\n', reportName
    d = db.DB(filePath)

    k = d.get('king')
    q = d.get('queen')
    m = d.get('man')
    w = d.get('woman')

    v1 = cp.add(k, w)
    v1 = cp.sub(v1, m)

    print cp.cosSim(v1, q), cp.euclDist(v1, q), cp.manaDist(v1, q)

    print 'cosSim\n', d.find_cosSim(v1)
    print 'euclDist\n', d.find_euclDist(v1)
    print 'manaDist\n', d.find_manaDist(v1)

    print '\n-------\n\n'

printReport('Carth', '../data/voc/npy/text8.npy')
printReport('Polar', '../data/voc/npy/text8_polar.npy')
printReport('Angular', '../data/voc/npy/text8_angular.npy')
