#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 23:51:04 2020

@author: motilek
"""

import numpy as np
import matplotlib.pyplot as plt


def spec_matrix(path, 
                full_tof_array,
                column):
    
    spec_matrix = np.array([])
    a = 0
    b = len(full_tof_array)
    
    for n in full_tof_array:
        temp_file = np.genfromtxt(path +'TOF_' + str(n)+'.dat') 
        temp_sgnl = temp_file[:, column]
        spec_matrix = np.append(spec_matrix, temp_sgnl, axis = 0)
        a = len(temp_sgnl)
    
    spec_matrix = np.reshape(spec_matrix, (b, a))    
    
    return spec_matrix