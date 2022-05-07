# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 16:51:37 2020

@author: motilek
"""

import numpy as np
import matplotlib.pyplot as plt

def min_inter_eV_distance_calc(eV):
    inter_eV_array = []
    inter_eV_array = np.array(inter_eV_array)
    
    a = len(eV)

    for n in range(a - 1):
        #print(n + 1)
        temp_inter_eV = eV[n] - eV[n + 1]
        inter_eV_array = np.append(inter_eV_array, temp_inter_eV)
    
    min_inter_eV = min(inter_eV_array)    
    
    return min_inter_eV