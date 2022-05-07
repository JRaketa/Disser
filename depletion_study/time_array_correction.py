# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 19:02:05 2020

@author: motilek
"""

import numpy as np
import matplotlib.pyplot as plt


def time_array_correction(spec, time_array, t0):
    
    ref_t0 = t0 * 10
    
    a = 0
    b = len(time_array)
    
    ref_time_array = 1e-9 * time_array
    
    while ref_time_array[a] <  ref_t0:
        a += 1
    
    new_spec = spec[a : b]
    new_time = time_array[a : b]
    
    
    
    return new_time, new_spec