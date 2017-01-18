# -*- coding: utf-8 -*-

import os, sys

depth = 2
topPath = os.path.dirname(os.path.abspath(__file__))

for i in range(depth):
    topPath = os.path.dirname(topPath)

sys.path.append(topPath)
