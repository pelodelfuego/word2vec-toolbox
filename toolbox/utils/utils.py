#!/usr/bin/env python
# encoding: utf-8

import random

from itertools import izip

def sizeof_fmt(num, suffix='B'):
    for unit in ['','Ki','Mi','Gi','Ti','Pi','Ei','Zi']:
        if abs(num) < 1024.0:
            return "%3.1f%s%s" % (num, unit, suffix)
        num /= 1024.0
    return "%.1f%s%s" % (num, 'Yi', suffix)

def pairwise(iterable):
    a = iter(iterable)
    return izip(a, a)

def shuffled(iterable):
    return sorted(iterable, key=lambda k: random.random())

