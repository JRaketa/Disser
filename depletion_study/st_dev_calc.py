#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 01:04:56 2020

@author: raketa
"""

import numpy as np
import matplotlib.pyplot as plt






def st_dev_calc(matrix):
    
    av_spec = np.mean(matrix , axis = 0)
    
    a = np.shape(matrix)[0]
    b = np.shape(matrix)[1]
    
    st_def = np.zeros(b)
    
    for n in range(a):
        for m in range(b):
            st_def[m] += (av_spec[m] -  matrix[n][m])**2
    
    st_def[:] = (1/(a - 1) * st_def[:])**0.5
    
    return st_def