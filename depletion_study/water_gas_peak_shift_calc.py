# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 23:19:14 2020

@author: motilek
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

import find_an_index as find_an_index
import gauss as gauss 

gauss = gauss.gauss
find_an_index = find_an_index.find_an_index

def water_gas_peak_shift_calc(eV, spec):
    
    right = find_an_index(12.1, eV)
    left = find_an_index(13.1, eV)
    
    init_vals = [0, 0, 0, 0]
    
    init_vals[0] = 12.6
    init_vals[1] = max(spec[left : right])
    init_vals[2] = 1
    init_vals[3] = 0
    
    popt, parm=curve_fit(gauss, eV[left : right], spec[left : right], p0=init_vals, maxfev=1000000)
    
    t0_current = popt[0]
    dt = 12.62 - t0_current
    
    
    
    return dt