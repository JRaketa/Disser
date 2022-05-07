#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 19:39:59 2020

@author: raketa
"""

import numpy as np
import matplotlib.pyplot as plt

import find_an_index as find_an_index 

find_an_index = find_an_index.find_an_index


def liq_peak_difference_calc(eV, solvent, molec, intens_coeff):
    
    eV_12_6 = find_an_index(12.6, eV)
    eV_10 = find_an_index(10, eV)
    eV_12 = find_an_index(11.4, eV)
    
    solvent_12_eV = solvent[eV_12_6]
    molec_12_eV = molec[eV_12_6]
    
    solvent[:] *= intens_coeff
    
    diff_spec = molec - solvent
    
    diff_spec_with_min = diff_spec[eV_12 : eV_10]
    eV_with_min = eV[eV_12 : eV_10]
    solvent_with_min = solvent[eV_12 : eV_10]
    
    av_spec = np.mean(diff_spec_with_min)
    if av_spec < 0:
        min_diff_spec = min(diff_spec_with_min)
    if av_spec > 0:
        min_diff_spec = max(diff_spec_with_min)
    
    ind_min = find_an_index(min_diff_spec, diff_spec_with_min)

    relative_change = min_diff_spec / solvent_with_min[ind_min]
    print(relative_change)

    
    plt.plot(eV, solvent)
    plt.plot(eV, molec)
    plt.plot(eV, diff_spec, '--')
    
    plt.plot(eV_with_min[ind_min], diff_spec_with_min[ind_min], 'o', markersize = 5)
    
    return