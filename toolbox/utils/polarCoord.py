#!/usr/bin/env python
# -*- coding: utf-8 -*-

import __init__

import math
import numpy as np

from scipy.weave import inline

def carthToPolar(carthList):
    carth = np.array(carthList)
    dimCount = len(carthList)

    arr = np.zeros(dimCount, 'f')

    code = """
            float norm = pow(carth[dimCount - 1], 2);

            for(int i = 0; i < dimCount - 1; i++) {
                norm += pow(carth[i], 2);

                float x = carth[i];
                float s = 0.0;

                for(int j = i; j < dimCount; j++) {
                    s += pow(carth[j], 2);
                }

                arr[i+1] = acos(x / sqrt(s));
            }

            arr[0] = sqrt(norm);
            if(carth[dimCount - 1] < 0) {
                arr[dimCount - 1] = 2 * M_PI - arr[dimCount - 1];
            }

            return_val = 1;
    """
    inline(code, ['carth', 'dimCount', 'arr'], headers = ['<math.h>'], compiler = 'gcc')
    return arr


def polarToCarth(polarList):
    polar = np.array(polarList)
    dimCount = len(polarList)

    arr = np.zeros(dimCount, 'f')

    code = """
            float norm = polar[0];

            for(int i = 1; i < dimCount; i++) {

                float pdt = norm;

                for(int j = 1; j < i; j++) {
                    pdt *= sin(polar[j]);
                }

                pdt *= cos(polar[i]);

                arr[i-1] = pdt;
            }

            float pdt = norm;
            for(int i = 1; i < dimCount; i++) {
                pdt *= sin(polar[i]);
            }

            arr[dimCount - 1] = pdt;

            return_val = 1;
    """
    inline(code, ['polar', 'dimCount', 'arr'], headers = ['<math.h>'], compiler = 'gcc')
    return arr

if __name__ == "__main__":
    print 'weave function built'
