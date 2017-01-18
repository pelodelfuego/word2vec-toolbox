#!/usr/bin/env python
# -*- coding: utf-8 -*-

import __init__

import numpy as np

def noPost(feature):
    def post(x):
        return feature(x)
    return post

def postNormalize(feature):
    def post(x):
        vect = feature(x)
        norm = np.linalg.norm(vect)
        return vect / norm
    return post

def postAbs(feature):
    def post(x):
        return [abs(v) for v in feature(x)]
    return post
