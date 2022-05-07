#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 02:14:27 2020

@author: raketa
"""

import numpy as np
import matplotlib.pyplot as plt

import eV_shift_correction as eV_shift_correction

eV_shift_correction = eV_shift_correction.eV_shift_correction




def matrix_shift_compensation(shift, BE, matrix):
    
    a = np.shape(matrix)[0]
    b = np.shape(matrix)[1]
    
    for n in range(a):
        matrix[n] = eV_shift_correction(BE, matrix[n], shift)

    
    return matrix