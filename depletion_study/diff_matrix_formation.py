#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 17 01:08:50 2020

@author: raketa
"""

import numpy as np
import matplotlib.pyplot as plt




def diff_matrix_formation(solvent,
                          molec,
                          BE,
                          coeff):
    
    
    len_BE = len(BE)
    a_solvent = np.shape(solvent)[0]
    a_molec = np.shape(molec)[0]
    
    diff_m = np.array([])
    
    i = 0
    j = 0
    
    for n in range(a_solvent):
        temp_solvent = solvent[n]
        
        for m in range(a_molec):
            temp_molec = molec[m]
            temp_diff = temp_molec - temp_solvent * coeff[n][m]
            diff_m = np.append(diff_m, temp_diff) 
    
            
    diff_m = np.reshape(diff_m, (a_solvent * a_molec, len_BE))
    
    
    
    return diff_m